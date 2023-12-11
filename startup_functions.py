from threading import Thread
from rabbitmq_consumer import consumer_function
import os
import dotenv

dotenv.load_dotenv()
AMAZONMQ_NAME = os.getenv('AMAZONMQ_NAME').split()

async def on_startup():
    for queue in AMAZONMQ_NAME:
        thread = Thread(target=consumer_function, args=(queue,))
        thread.start()