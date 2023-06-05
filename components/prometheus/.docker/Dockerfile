FROM docker.io/prom/prometheus:v2.44.0 as dev

COPY .docker/files/prometheus.yaml raw_config.yaml
COPY .docker/files/entrypoint.sh entrypoint.sh

ENTRYPOINT ["sh", "-c", "/prometheus/entrypoint.sh"]

