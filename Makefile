DJANGO_SETTINGS_MODULE:=shamengo.settings.dev

export DJANGO_SETTINGS_MODULE

install:
	pip3 install django

install-yarn:
	npm install -g yarn

dependencies:
	yarn install
	yarn add bower

colorfield:
	pip3 install django-colorfield

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

serve:
	python3 manage.py runserver

db:
	sqlite3 db.sqlite3

shell:
	python3 manage.py shell

.PHONY: serve migrate install
