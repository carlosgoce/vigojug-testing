testdjango:
	cd django && .venv/bin/python manage.py test

testlaravel:
	cd laravel && vendor/bin/phpunit
