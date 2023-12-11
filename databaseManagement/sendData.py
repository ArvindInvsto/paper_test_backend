import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
import pandas as pd
from database import rds_hostname, db_port, rds_db_name, rds_username, rds_password, BACKEND_LINK
from fastapi import HTTPException,status
from datetime import datetime, timedelta
import requests

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def saveData(order_id,user_id,order_side,created_at,instrument_name,price,quantity,invsto_order_status,exchange_id,order_type,brokerage,strategy_id,stoploss_trigger):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            print("saving data")
            cur = conn.cursor(cursor_factory=RealDictCursor)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # query = f"""INSERT INTO order_details (time_stamp, strategy_subscriber_id, order_number, instrument_name, price, quantity, order_side, order_status) VALUES ('{time}', '{strategySubscriberId}','{orderno}', '{instrument}', '{price}', '{qty}', '{orderside}', '{status}');"""
            if (brokerage == 'paperbrokerage'):
                query = f"""INSERT INTO orderbook (order_id,user_id,order_side,created_at,instrument_name,price,quantity,invsto_order_status,exchange_id,order_type,updated_at,subscriber_strategy_id,stoploss_trigger,average_price,brokerage_id,brokerage_order_status) 
                                    VALUES ('{order_id}', '{user_id}','{order_side}', '{created_at}', '{instrument_name}', '{price}', '{quantity}', '{invsto_order_status}', '{exchange_id}', '{order_type}', '{current_time}', '{strategy_id}', '{stoploss_trigger}',{(price*quantity)/quantity}, '{brokerage}', '{invsto_order_status}');"""
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            print("order details saved.")
        except Exception as ex:
                print("getData: exception in querying")
                print(ex)
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                    detail="sorry for inconvenience! please contact admin!!")
    except Exception as ex:
        print("getData: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")

def saveOrderDetails(broker, orderPlaced,msg):
    ret=broker.get_order_detail(orderNumber=orderPlaced['orderno'])
    # Get the details from orderdata
    ordertime=msg['timestamp']
    orderno=ret['orderno']
    instrument=ret['instrument']
    price=ret['price']
    qty=ret['qty']
    orderside=ret['order_side']
    order_status=ret['status']
    user_id = msg["userid"]
    exchange_id = msg["exchange"]
    order_type = msg["order_type"]
    brokerage = msg["brokerage"]
    strategy_id = int(msg["strategy_id"]["strategy_id"])
    stoploss_trigger = msg['stoploss_trigger']
    try:
        saveData(order_id = orderno,user_id = user_id,order_side = orderside ,created_at = ordertime ,instrument_name = instrument ,price = price,
                 quantity = qty ,invsto_order_status = order_status ,exchange_id = exchange_id ,order_type = order_type , brokerage = brokerage,strategy_id=strategy_id,stoploss_trigger = stoploss_trigger)
    except Exception as e:
        print(e, "! error while saving data to the database")


def getData():
    global cursor, sqliteConnection

    # get data
    query='SELECT * FROM OrderData'
    cursor.execute(query)
    # Convert to the dataframe
    data=pd.DataFrame(cursor.fetchall(), columns=['Time', 'OrderNo', 'Instrument', 'Price', 'Qty', 'OrderSide', 'Status'])
    sqliteConnection.commit()    
    return data

def orderSignal(data, order_id):
    if int(order_id) < 1 :
        data["status"] = "NOT ACTIVE"
    else:
        data["status"] = "ACTIVE"
    signal_json = {
    'accept': 'application/json',
    'order-id': str(order_id),
    'strategy-id-id': data["strategyId"],
    'order-side': data["order_side"],
    'order-type': data["order_type"],
    'order-status': data["status"],
    }
    response = requests.post(BACKEND_LINK + "/orders/insertsignal", headers=signal_json)
    print("signal: ", response.json())
    return response

if __name__=='__main__':
    data=getData()
    print(data)