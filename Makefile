port=12345

setup: venv secrets db

venv:
	virtualenv venv
	venv/bin/pip install -r pip-freeze.txt

secrets: venv
	printf "SECRET_KEY = '" > cert/cert/secrets.py
	cat /dev/urandom |tr -dc "[:alnum:]" | head -c40 >> cert/cert/secrets.py
	printf "'\n" >> cert/cert/secrets.py

db: secrets venv
	mkdir -p cert/db
	venv/bin/python cert/manage.py syncdb

run:
	venv/bin/python cert/manage.py runserver 0.0.0.0:$(port)

