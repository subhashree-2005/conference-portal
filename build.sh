#!/usr/bin/env bash
# Render runs this automatically before every deploy.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
