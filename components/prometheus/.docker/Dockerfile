FROM docker.io/prom/prometheus:v2.44.0 as dev

COPY .docker/files/prometheus.yaml raw_config.yaml

RUN wget -O envsubst https://github.com/a8m/envsubst/releases/download/v1.4.2/envsubst-Linux-x86_64 && \
    chmod +x envsubst && \
    ./envsubst < raw_config.yaml > /etc/prometheus/prometheus.yml
