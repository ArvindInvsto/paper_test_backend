import pika
import json
import os
import dotenv
from credentialManagement.credential import getDataFromStrategyId
from expressManagement import loginExpress, placeOrder,loginPaper
from databaseManagement import saveOrderDetails, orderSignal
from order_middleware import pre_commit

dotenv.load_dotenv()
AMAZONMQ_HOST = os.getenv('AMAZONMQ_HOST')
AMAZONMQ_PORT = str(os.getenv('AMAZONMQ_PORT'))
AMAZONMQ_USERNAME = os.getenv('AMAZONMQ_USERNAME')
AMAZONMQ_PASSWORD = os.getenv('AMAZONMQ_PASSWORD')
AMAZONMQ_NAME = os.getenv('AMAZONMQ_NAME')


def callback(ch, method, properties, body):
    try:
        message = body.decode()
        data = json.loads(message)
        pre_commit(data['brokerage'],data)
    except Exception as e:
        print("Rabbitmq Consumer; An error occurred:", str(e))
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)

def consumer_function(queue):
    amazon_mq_url = f'amqps://{AMAZONMQ_USERNAME}:{AMAZONMQ_PASSWORD}@{AMAZONMQ_HOST}:{AMAZONMQ_PORT}'
    print(amazon_mq_url)
    connection = pika.BlockingConnection(pika.URLParameters(amazon_mq_url))
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=25)
    queue_name = queue
    # queue_name = 'order'
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    print(f"Starting Consuming {queue} queue")
    channel.start_consuming()


# def paper_order(data):
#     headers = {
#     'accept': 'application/json',
#     'userid': data["userid"],
#     'trading-symbol': data["trading_symbol"],
#     'qty': data["qty"],
#     'timestamp': data["timestamp"],
#     'exchange': data["exchange"],
#     'trans-type': data["trans_type"],
#     'product': data["product"],
#     'order-type': data["order_type"],
#     'price': data["price"],
#     'stoploss-trigger': data["stoploss_trigger"],
#     'status': data["status"],
#     }
#     order_response = requests.post(BACKEND_LINK + "/orders/insert", headers=headers)
#     print(order_response.text)
#     return order_response.text
