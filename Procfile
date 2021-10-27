web: gunicorn developstoday.wsgi:application --log-level debug
worker: celery -A developstoday worker --beat --concurrency 10 -l info