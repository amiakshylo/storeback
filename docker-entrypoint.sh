#!/bin/bash

#set -e  # Exit immediately if any command fails

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Populate database
#echo "Populating database..."
#python manage.py seed_db

# Start server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
