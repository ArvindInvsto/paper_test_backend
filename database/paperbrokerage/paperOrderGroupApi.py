import sqlite3
import traceback
from fastapi import HTTPException, status
import psycopg2
from datetime import datetime, timedelta
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"


def insert_paper_order_groups(userid, order_id, tradingsymbol_one, tradingsymbol_two, tradingsymbol_three, tradingsymbol_four, quantity_one, quantity_two, quantity_three, quantity_four, exchange, transaction_type_one, transaction_type_two, transaction_type_three, transaction_type_four, timestamp, product, order_type_one, order_type_two, order_type_three, order_type_four, price_one, price_two, price_three, price_four, stoploss_trigger_price_one, stoploss_trigger_price_two, stoploss_trigger_price_three, stoploss_trigger_price_four, status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "INSERT INTO sharkcap_db_paperordergroup(userid, order_id, tradingsymbol_one, tradingsymbol_two, tradingsymbol_three, tradingsymbol_four, quantity_one, quantity_two, quantity_three, quantity_four, exchange, transaction_type_one, transaction_type_two, transaction_type_three, transaction_type_four, timestamp, product, order_type_one, order_type_two, order_type_three, order_type_four, price_one, price_two, price_three, price_four, stoploss_trigger_price_one, stoploss_trigger_price_two, stoploss_trigger_price_three, stoploss_trigger_price_four, status) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                userid, order_id, tradingsymbol_one, tradingsymbol_two, tradingsymbol_three, tradingsymbol_four, quantity_one, quantity_two, quantity_three, quantity_four, exchange, transaction_type_one, transaction_type_two, transaction_type_three, transaction_type_four, timestamp, product, order_type_one, order_type_two, order_type_three, order_type_four, price_one, price_two, price_three, price_four, stoploss_trigger_price_one, stoploss_trigger_price_two, stoploss_trigger_price_three, stoploss_trigger_price_four, status)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'Inserted data successfully'}
        except Exception as e:
            return {'Error': f'{e}, while inserting data to the {rds_db_name}!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")


def get_paper_order_groups():
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperordergroup"
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f'{e}, while fetching data from {rds_db_name}'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def update_SLtrigger_price_orders(stoploss_trigger_price_one, stoploss_trigger_price_two, stoploss_trigger_price_three, stoploss_trigger_price_four, order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperordergroup set stoploss_trigger_price_one = '{}', stoploss_trigger_price_two = '{}', stoploss_trigger_price_three = '{}', stoploss_trigger_price_four = '{}' where order_id = '{}'".format(
                stoploss_trigger_price_one, stoploss_trigger_price_two, stoploss_trigger_price_three, stoploss_trigger_price_four, order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'StopLoss Updated!!'}
        except Exception as e:
            return {'Error': f'{e}, while updating stopLoss!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def update_order_status_orders(status, order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperordergroup set status = '{}' where order_id = '{}'".format(
                status, order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'Order Status Updated!!'}
        except Exception as e:
            return {'Error': f'{e}, while updating order status!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def update_complete_orders(orderid, price_one, price_two, price_three, price_four):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "update sharkcap_db_paperordergroup set status = 'COMPLETE', price_one = '{}', price_two = '{}', price_three = '{}', price_four = '{}' where order_id = '{}'".format(
                price_one, price_two, price_three, price_four, orderid)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': "Order Updated!!"}
        except Exception as e:
            return {'Error': f'{e}, While Updating order!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def get_orderHistory_orders(orderid):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select status, '' as status_message FROM sharkcap_db_paperordergroup where order_id = '{}'".format(
                orderid)
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f'{e}, while fetching data!!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def get_list_orders(sdate, edate, status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select * from sharkcap_db_paperordergroup where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f'{e}, while fetching data!!'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def delete_orderHistory_orders(orderid):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE FROM sharkcap_db_paperordergroup where order_id = '{}'".format(
                orderid)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Sucess": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f'{e}'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def delete_list_orders(sdate, edate, status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE from sharkcap_db_paperordergroup where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f'{e}'}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")