install:
	pip3 install django

install-yarn:
	npm install -g yarn

dependencies:
	yarn install
	bower install

migrate:
	python3 manage.py migrate

serve:
	python3 manage.py runserver

db:
	sqlite3 db.sqlite3

shell:
	python3 manage.py shell


.PHONY: serve migrate install
