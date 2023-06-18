#!/bin/bash

# Specify the process name or command to monitor
process_name="$1"

# Function to convert memory values to bytes
convert_to_bytes() {
  local value=$1
  local unit=${value//[[:digit:].]/}
  value=${value//[[:alpha:]]/}
  case $unit in
    K) echo "$value * 1024" | bc ;;
    M) echo "$value * 1024 * 1024" | bc ;;
    G) echo "$value * 1024 * 1024 * 1024" | bc ;;
    *) echo "$value" ;;
  esac
}

while true; do
  # Retrieve the process ID for the specified process
  process_id=$(pgrep -f "$process_name")

  if [[ -z "$process_id" ]]; then
    echo "Process not found: $process_name"
    exit 1
  fi

  # Get the virtual memory size (VSZ) of the process
  virtual_memory=$(ps -o vsz= -p "$process_id")
  virtual_memory=$(convert_to_bytes "${virtual_memory}K")

  # Get the mapped memory usage of the process
  mapped_memory=$(vmmap "$process_id" | awk '/mapped file/ {print $3}' | tail -1)
  mapped_memory=$(convert_to_bytes "$mapped_memory")

  # Get the shared memory usage of the process
  shared_memory=$(vmmap "$process_id" | awk '/shared memory/ {print $3}' | tail -1)
  shared_memory=$(convert_to_bytes "$shared_memory")

  # Get the unused but dirty shlib __DATA memory usage of the process
  unused_memory=$(vmmap "$process_id" | awk '/unused but dirty shlib __DATA/ {print $6}' | tail -1)
  unused_memory=$(convert_to_bytes "$unused_memory")

  # Get the stack memory usage of the process
  stack_memory=$(vmmap "$process_id" | awk '/Stack/ {print $2}' | tail -1)
  stack_memory=$(convert_to_bytes "$stack_memory")

  # Format the metric payload
  metrics_payload=$(cat <<EOF
# TYPE process_virtual_memory_usage_bytes gauge
process_virtual_memory_usage_bytes{process="$process_name"} $virtual_memory
# TYPE process_mapped_memory_usage_bytes gauge
process_mapped_memory_usage_bytes{process="$process_name"} $mapped_memory
# TYPE process_shared_memory_usage_bytes gauge
process_shared_memory_usage_bytes{process="$process_name"} $shared_memory
# TYPE process_unused_memory_usage_bytes gauge
process_unused_memory_usage_bytes{process="$process_name"} $unused_memory
# TYPE process_stack_memory_usage_bytes gauge
process_stack_memory_usage_bytes{process="$process_name"} $stack_memory
EOF
)

  # Send metrics to the Pushgateway and check the response
  response=$(echo "$metrics_payload" | curl --write-out "%{http_code}" --silent --output /dev/null --data-binary @- http://pushgateway-zxc55y.bunnyenv.com/metrics/job/pushgateway/)

  if [[ "$response" == "200" ]]; then
    echo "Metrics have been sent."
  else
    echo "Failed to send metrics. Response code: $response"
  fi

  sleep 10  # Wait for 10 seconds before sending the next set of metrics
done

