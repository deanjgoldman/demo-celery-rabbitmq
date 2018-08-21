from celery import Celery
from kombu import Queue

app = Celery('tasks', broker='amqp://dean:dean123@localhost/dean_vhost')

app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default',    routing_key='task.#'),
    Queue('second', routing_key='second.#'),
)
task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.default'

@app.task(queue="default")
def add(x, y):
    return x + y
    
@app.task(queue="second")
def fun(x, y):
    return "OTHER QUEUE WOO {} {}".format(x, y)
