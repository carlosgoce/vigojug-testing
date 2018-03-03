.DEFAULT_GOAL := install

django/.venv/bin/python:
	cd django && virtualenv .venv

install: django/.venv/bin/python
	cd django && source .venv/bin/activate && pip install -r requirements.txt && python manage.py migrate
	cd laravel && composer install
	cd ruby && gem install bundler && bundle install

testdjango:
	cd django && .venv/bin/python manage.py test

pytestdjango:
	cd django && .venv/bin/pytest

testlaravel:
	cd laravel && vendor/bin/phpunit

testruby:
	cd ruby && rspec
