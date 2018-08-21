# Demo Celery RabbitMQ
The simplest multi-queue

## instructions
1. Install rabbitmq, set up a user, password, and virtualhost  
`$ rabbitmq-server`
2. Install virtualenv, requirements  
`virtualenv venv`   
`source venv/bin/activate`  
`pip install -r requirements` 
3. run celery worker   
`$ celery -A tasks worker --loglevel=info -Q default,second` 
4. run celery flower   
`celery -A tasks flower --port=5556`

voila! :tanabata_tree: :rabbit:
