FROM sentry:latest as dev

RUN sed -i 's/stretch/buster/g' /etc/apt/sources.list
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get full-upgrade -y && \
    apt-get install --no-install-recommends supervisor -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install psycopg2-binary==2.8.6

# Copy the Supervisor configuration file
COPY .docker/files/supervisor.d /etc/supervisor/conf.d
COPY .docker/files/entrypoint.sh /entrypoint.sh

ENV SENTRY_SECRET_KEY=AmQtco2220reKOzR7mprnmlN1DbfZ0cZ
ENV C_FORCE_ROOT=1
EXPOSE 9000

# Start Supervisor when the container starts
RUN chmod +x /entrypoint.sh
CMD ["./entrypoint.sh"]
