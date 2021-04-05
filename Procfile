web: gunicorn --pythonpath django {{ project_name }}.wsgi
release: python django/manage.py migrate && python django/manage.py loaddata django/{{ project_name }}/app_name/migrations/fixture