FROM sentry:latest as dev

RUN sed -i 's/stretch/buster/g' /etc/apt/sources.list

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get full-upgrade -y && \
    apt-get install --no-install-recommends supervisor postgresql redis -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary==2.8.6

# Copy the Supervisor configuration file
COPY .docker/files/supervisor.d /etc/supervisor/conf.d

# Switch to the postgres user
USER postgres

# Create the init.sql file in the user's home directory
RUN echo "CREATE USER sentry WITH PASSWORD 'sentry';" > /tmp/postgres_init.sql && \
    echo "CREATE DATABASE sentry;" >> /tmp/postgres_init.sql && \
    echo "ALTER USER sentry WITH SUPERUSER;" >> /tmp/postgres_init.sql && \
    echo "GRANT ALL PRIVILEGES ON DATABASE sentry TO sentry;" >> /tmp/postgres_init.sql

# Run the psql command to execute the init.sql script
RUN pg_ctlcluster 11 main start && \
    /etc/init.d/postgresql start && psql -f /tmp/postgres_init.sql

# Switch back to root user
USER root

ENV SENTRY_SECRET_KEY=AmQtco2220reKOzR7mprnmlN1DbfZ0cZ
ENV SENTRY_POSTGRES_HOST=localhost
ENV SENTRY_DB_USER=sentry
ENV SENTRY_DB_PASSWORD=sentry
ENV SENTRY_REDIS_HOST=localhost
ENV C_FORCE_ROOT=1

EXPOSE 9000

RUN supervisord && \
    sentry upgrade --noinput && \
    supervisorctl restart all && \
    sentry createuser --email admin@admin.local --password admin --superuser


# Start Supervisor when the container starts
CMD ["supervisord", "-n"]
