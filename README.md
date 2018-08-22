# Demo Celery RabbitMQ
The simplest multi-queue

## instructions
1. Install rabbitmq, set up a user, password, and virtualhost  
`$ rabbitmq-server` (you may need to set your PATH to understand the command: `PATH=$PATH:/usr/local/sbin`)    
2. Install virtualenv, requirements  
`virtualenv venv`   
`source venv/bin/activate`  
`pip install -r requirements` 
3. run celery worker   
`$ celery -A tasks worker --loglevel=info -Q default,second` 
4. run celery flower   
`celery -A tasks flower --port=5556`

voila! :tanabata_tree: :rabbit:

#### Acknowledgements
Mostly pieced together from the celery docs and this nice post:
https://tests4geeks.com/python-celery-rabbitmq-tutorial/
