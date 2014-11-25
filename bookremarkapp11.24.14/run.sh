#!/bin/bash  

source venv/bin/activate

cat <(sleep 3;open 'http://localhost:8000';) &

python manage.py runserver


