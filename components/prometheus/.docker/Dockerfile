FROM docker.io/prom/prometheus:v2.44.0 as dev

COPY .docker/files/prometheus.yaml raw_config.yaml
COPY .docker/files/entrypoint.sh entrypoint.sh

# COPY files/prometheus.yaml raw_config.yaml
# COPY files/entrypoint.sh entrypoint.sh

ENTRYPOINT cat entrypoint.sh | sh
CMD []
