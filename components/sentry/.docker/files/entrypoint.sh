#!/bin/sh

# supervisorctl stop all
sentry upgrade --noinput --lock
# supervisorctl restart all
# sentry createuser --email admin@admin.local --password admin --superuser
# supervisord -n
