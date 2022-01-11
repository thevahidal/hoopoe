#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic

python manage.py init_telegram_client
echo "Telegram client started"

exec "$@"
