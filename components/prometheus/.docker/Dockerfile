FROM docker.io/prom/prometheus:v2.44.0 as dev

COPY .docker/files/prometheus.yaml /prometheus/raw_config.yaml
COPY .docker/files/entrypoint.sh /prometheus/entrypoint.sh

ENTRYPOINT ["sh", "-c", "entrypoint.sh"]

