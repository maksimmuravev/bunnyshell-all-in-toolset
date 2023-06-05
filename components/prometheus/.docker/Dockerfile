FROM docker.io/prom/prometheus:v2.44.0 as dev

COPY --chown=0755 .docker/files/prometheus.yaml raw_config.yaml
COPY --chown=0755 .docker/files/entrypoint.sh entrypoint.sh

ENTRYPOINT ["sh", "-c", "entrypoint.sh"]
