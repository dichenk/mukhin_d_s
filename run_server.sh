#!/bin/sh

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for postgres to be ready..."
  sleep 1
done

echo "Postgres is up - executing command"
# python manage.py makemigrations --noinput # Эту строку лучше убрать в продакшене
python manage.py migrate --noinput

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

python manage.py runserver 0.0.0.0:8000