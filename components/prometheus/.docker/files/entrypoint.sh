#!/bin/sh

wget -O envsubst https://github.com/a8m/envsubst/releases/download/v1.4.2/envsubst-Linux-x86_64
chmod +x envsubst

./envsubst < raw_config.yaml > /prometheus/prometheus.yml

# while true; do
#   sleep 3
#   cat /prometheus/prometheus.yml
# done

/bin/prometheus
