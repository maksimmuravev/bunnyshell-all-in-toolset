FROM docker.io/otel/opentelemetry-collector:0.76.1 as dev

COPY .docker/files/opentelemetry.yaml /opt/opentelemetry/opentelemetry.yaml
ENTRYPOINT /otelcol --config /opt/opentelemetry/opentelemetry.yaml
