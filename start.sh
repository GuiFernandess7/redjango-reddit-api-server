#!/bin/bash

python redjango/manage.py collectstatic --noinput
python redjango/manage.py makemigrations
python redjango/manage.py migrate
exec python redjango/manage.py runserver 0.0.0.0:8000
