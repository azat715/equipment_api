#!/bin/sh
/code/wait-for-it.sh db:5432 -t 30 -- echo "run db"

# запуск django

if [[ "${GUNICORN}" == "True" ]]; then
  gunicorn --chdir training_avido --bind :8000 equipment_api.wsgi:application
else
  python manage.py runserver 0.0.0.0:8000
fi

