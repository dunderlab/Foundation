#!/bin/bash

source /app/venv311/bin/activate
if [ -f "/app/djangorun/requirements.txt" ]; then
    pip install --no-cache-dir -r /app/djangorun/requirements.txt
fi

cd /app/djangorun
if [ -f "./startup.sh" ]; then
    . ./startup.sh
fi

ntpd
python manage.py runserver 0.0.0.0:80
