#!/bin/bash

python redjango/manage.py collectstatic --noinput
exec python redjango/manage.py runserver 0.0.0.0:8000
