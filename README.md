cert-sites
==========

Website for KAIST Student CERT members.
Built on django 1.7.

Requirements
------------

- python 2.x
- pip
- virtualenv

Setup
-----

```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd cert
./manage.py syncdb
```

To apply local setting:
```sh
cd cert/cert/
cp local_settings.py.default local_settings.py
```

Run
---

```sh
cd cert
./manage.py runserver 0.0.0.0:12345
```

