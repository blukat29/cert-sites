cert-sites
==========

Website for KAIST Student CERT members.
Built on django 1.7.

Requirements
------------

- pip
- virtualenv
- GNU make

Setup
-----

```sh
virtualenv venv
source venv/bin/activate
pip install -r pip-freeze.txt
cd cert
./manage.py syncdb
```

OR just
```sh
make setup
```

Run
---

```sh
cd cert
./manage.py runserver 0.0.0.0:12345
```
OR
```sh
make run port=12345
```

