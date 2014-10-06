port=12345

setup: venv db

venv:
	virtualenv venv
	venv/bin/pip install -r pip-freeze.txt

db: venv
	venv/bin/python cert/manage.py syncdb

run:
	venv/bin/python cert/manage.py runserver 0.0.0.0:$(port)

