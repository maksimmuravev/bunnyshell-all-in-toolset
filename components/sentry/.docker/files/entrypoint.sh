#!/bin/bash

supervisord
sentry upgrade --noinput
supervisorctl restart all
sentry createuser --email admin@admin.local --password admin --superuser
supervisord -n
