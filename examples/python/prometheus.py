from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Create a registry to hold the metrics
registry = CollectorRegistry()

# Create a Gauge metric
gauge_metric = Gauge("hello_world_metric", "Example metric for Hello World", registry=registry)

# Set the value of the metric
gauge_metric.set(42)

# Push the metrics to the Prometheus Pushgateway
push_to_gateway("https://prometheus-cshdie.bunnyenv.com/metrics", job="pushgateway", registry=registry)
