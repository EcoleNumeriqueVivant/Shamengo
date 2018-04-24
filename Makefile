DJANGO_SETTINGS_MODULE:=shamengo.settings.dev

export DJANGO_SETTINGS_MODULE 

install:
	pip3 install django

install-yarn:
	npm install -g yarn

dependencies:
	yarn install
	yarn add bower

migrate:
	python3 manage.py migrate

serve:
	python3 manage.py runserver

db:
	sqlite3 db.sqlite3

shell:
	python3 manage.py shell

<<<<<<< HEAD
herokumigrate:
	heroku run python3 manage.py migrate


=======
>>>>>>> 1445fc4a076b968fc82a79be2af088e63c35e2ba
.PHONY: serve migrate install
