import time
from databaseManagement import saveData
import requests
import os
import dotenv
from datetime import datetime, timedelta

dotenv.load_dotenv()
OMS_hostname = os.getenv('OMS_hostname')

def paper_order(data, user_data):
    headers = {
    'accept': 'application/json',
    'userid': str(user_data["user_id"]),
    'trading-symbol': data["instrument"], #data["trading_symbol"],
    'qty': data["qty"],
    'timestamp': data["timestamp"],
    'exchange': data["exchange"],
    'trans-type': data["order_side"],
    'product': data["product_type"],
    'order-type': data["order_type"],
    'price': str(data["price"]), # data["price"],
    'stoploss-trigger': str(data["stoploss_trigger"]), # data["stoploss_trigger"],
    'status': "COMPLETE", # data["status"],
    }

    order_response = requests.post(OMS_hostname + "orders/insert", headers=headers)
    print("Order No: ", order_response.text)
    return order_response.text

def placeOrder(broker, msg, user_data):
    # Placing the orders
    if msg['order_type']=='MKT':
        ret=broker.place_market_order(
            instrument=msg['instrument'],
            order_side=msg['order_side'],
            qty=msg['qty'],
            product_type=msg['product_type'],
            validity=msg['validity'],
            variety=msg['variety'],
            exchange=msg['exchange'])
        
    elif msg['order_type']=='limit':
        ret=broker.place_limit_order(
            instrument=msg['instrument'],
            order_side=msg['order_side'],
            qty=msg['qty'],
            limit_price=msg['limit_price'],
            product_type=msg['product_type'],
            validity=msg['validity'],
            variety=msg['variety'],
            exchange=msg['exchange'])
        
    elif msg['order_type']=='squareoff':
        ret=broker.position_squareOff(id=msg['order_number'])
    if broker.brokerName == 'paperbrokerage':
        orderno = paper_order(msg, user_data)
        ret["orderno"] = orderno
    return ret

# Order Tracker
orderStatus=dict()
def trackOrder(broker, orderDetail):
    global orderStatus

    getOrderStatus=broker.get_order_detail(orderNumber=orderDetail['orderno'])
    orderStatus[orderDetail['orderno']]=getOrderStatus['status']

    # Run loop for 5 Mins
    from datetime import datetime,timedelta
    end_time = datetime.now()+timedelta(minutes=5)
    while end_time > datetime.now():

        # Loopover the orderNumbers and get the status
        for ordernumber in orderStatus.keys():
            if orderStatus[ordernumber]!='COMPLETE':
                ret=broker.get_order_detail(orderNumber=ordernumber)
                orderStatus[ordernumber]=ret['status']

        # orders are incompleted then continue
        for ordernumber in orderStatus.keys():
            if orderStatus[ordernumber]!='COMPLETE':
                break
        
        if orderStatus[ordernumber]!='COMPLETE':
            time.sleep(2)
            continue
        
        # if all the orders are completed then break
        break
        

    # Cancel the order
    for ordernumber in orderStatus.keys():
        if orderStatus[ordernumber]!='COMPLETE':
            # Cancel the order if not completed
            broker.cancel_order(ordernumber)
            print(f"Canceling Order {ordernumber} as not completed yet")
        else:
            ret=broker.get_order_detail(orderNumber=ordernumber)
            # Get the details from orderdata
            ordertime=ret['time']
            orderno=ret['orderno']
            instrument=ret['instrument']
            price=ret['price']
            qty=ret['qty']
            orderside=ret['order_side']
            status=ret['status']
            try:
                saveData(time=ordertime, orderno=orderno, instrument=instrument,
                        price=price, qty=qty, orderside=orderside, status=status)
            except Exception as e:
                print(e, "! error while saving data to the database")   