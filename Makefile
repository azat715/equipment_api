init:
	docker-compose up --build --no-start
	docker-compose up -d
	docker-compose exec backend python manage.py migrate

load:
	docker-compose exec backend python manage.py loaddata fixture/all.json
