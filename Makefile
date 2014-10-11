port=12345

setup: env secrets db

env:
	virtualenv env
	env/bin/pip install -r requirements.txt

secrets: env
	printf "SECRET_KEY = '" > cert/cert/secrets.py
	cat /dev/urandom |tr -dc "[:alnum:]" | head -c40 >> cert/cert/secrets.py
	printf "'\n" >> cert/cert/secrets.py

db: secrets env
	mkdir -p cert/db
	env/bin/python cert/manage.py syncdb

run:
	env/bin/python cert/manage.py runserver 0.0.0.0:$(port)

