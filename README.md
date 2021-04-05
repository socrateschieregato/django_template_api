# {{ project_name }}

## Running Commands
## Install Dependencies
`pipenv install django`
fechar o terminal e abrir novamente ou activate virtualenv
`django-admin startproject --template ..\django_template_api api_project . --extension=py,md,yml,ini,sh --name=Makefile,.coveragerc,.gitignore`
`pipenv install`
alterar o nome do projeto no arquivo 'docker-compose'
`docker-compose up -d`
criar migrations
`python django\manage.py makemigrations --settings=api_project.settings.development`
executar migrations (local)
`python django\manage.py migrate --settings=api_project.settings.development`

#### Tests
`pytest django`

#### Coverage
`pytest --cov={{ project_name }} django`

#### Isort
`isort -rc .`

#### Lint
`flake8 django`

#### Load Data to DB (local)
`python django/manage.py loaddata django/app_name/migrations/fixture_model --settings={{ project_name }}.settings.development`
