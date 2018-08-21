# Demo Celery RabbitMQ

## commands to run
-------------------
`$ rabbitmq-server`
`$ venv/bin/celery -A tasks flower --port=5554`
`$ celery -A tasks worker --loglevel=info -Q default,second`
