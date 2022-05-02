#!/bin/sh

# echo "Waiting for postgres..."
# while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#     echo $POSTGRES_HOST $POSTGRES_PORT
#     sleep 0.1
# done
# echo "PostgreSQL started"

# python manage.py migrate
# python manage.py collectstatic --noinput

exec "$@"
