#!/usr/bin/env bash
# Exit on error
set -o errexit

pipenv install  

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser_if_not_exists

#Populate DB
#python manage.py seed_db


