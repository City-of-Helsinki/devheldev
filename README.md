# New dev.hel.fi site's wagtail project

[![Build Status](https://travis-ci.org/City-of-Helsinki/devheldev.svg?branch=master)](https://travis-ci.org/City-of-Helsinki/devheldev)
[![codecov](https://codecov.io/gh/City-of-Helsinki/devheldev/branch/master/graph/badge.svg)](https://codecov.io/gh/City-of-Helsinki/devheldev)
[![Requirements](https://requires.io/github/City-of-Helsinki/devheldev/requirements.svg?branch=master)](https://requires.io/github/City-of-Helsinki/devheldev/requirements/?branch=master)

## Installation

Installation assumes a working PostgreSQL with table creation rights

 * Clone the repository somewhere and change there for the rest
 * pip install -r requirements.txt **or**
  * pip install -r dev_requirements.txt
 * npm install
 * createdb heldev
 * python manage.py migrate
 * python manage.py collectstatic
 * python manage.py compress
 * python manage.py createsuperuser
 * python manage.py runserver
