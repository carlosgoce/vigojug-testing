install:
	cd django && virtualenv .venv && act && pip install -r requirements.txt && python manage.py migrate
	cd laravel && composer install
	cd ruby && gem install bundler && bundle install

testdjango:
	cd django && .venv/bin/python manage.py test

testlaravel:
	cd laravel && vendor/bin/phpunit

testruby:
	cd ruby && rspec
