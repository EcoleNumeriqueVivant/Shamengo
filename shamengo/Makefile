USERNAME:=joe
EMAIL:=joe@email.com 

install:
	pip3 install django

migrate:
	python3 manage.py migrate

serve:
	python3 manage.py runserver

db-console:
	sqlite3 db.sqlite3

create-superuser:
	python3 manage.py createsuperuser --username=${USERNAME} --email=${EMAIL}

.PHONY: serve migrate install db-console create-superuser
