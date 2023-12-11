import traceback
from fastapi import HTTPException, status
import psycopg2
from datetime import datetime, timedelta
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def insert_paper_orders(userid, trading_symbol, qty, exchange, trans_type, timestamp, product, order_type, price, stoploss_trigger, order_status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "INSERT INTO sharkcap_db_paperorders(userid, trading_symbol, quantity, exchange, transaction_type, timestamp, product, order_type, price, stop_loss_trigger_price, status) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') RETURNING order_id".format(
                userid, trading_symbol, qty, exchange, trans_type, timestamp, product, order_type, price, stoploss_trigger, order_status)
            cur.execute(query)
            order_number= cur.fetchone()["order_id"]
            print(order_number)
            conn.commit()
            cur.close()
            conn.close()
            return order_number
        except Exception as ex:
            print(ex)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
        
def get_paper_orders():
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperorders"
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f"{e}, while fetching data"}
    except Exception as ex:
        print("get_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
        
    
def update_SLtrigger_price_orders(stoploss_trigger, order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperorders set stoploss_trigger_price = '{}' where order_id = '{}'".format(
                stoploss_trigger, order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'Sl Updated successfully'}
        except Exception as ex:
            return {'Error': f"{ex}, while updating SL"}
    except Exception as ex:
        print("update_SLtrigger_price_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def update_order_status_orders(status, order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperorders set status = '{}' where order_id = '{}'".format(
                status, order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'Order status updated!!'}
        except Exception as e:
            return {'Error': f'{e}, while updating order Status!!'}
    except Exception as ex:
        print("update_order_status_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def update_complete_orders(order_id, price):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            conn = psycopg2.connect(CONNECTION_AWS)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            query = "update sharkcap_db_paperorders set status = 'COMPLETE', price = '{}' where order_id = '{}'".format(
                price, order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {'Success': 'order Updated!'}
        except Exception as e:
            return {'Error': f'{e}, while updating order!'}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
        
def get_orderHistory_orders(order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select status, '' as status_message FROM sharkcap_db_paperorders where order_id = '{}'".format(
                order_id)
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f"{e}, while Fetching data!!"}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def get_by_orderid_orders_api(order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select * FROM sharkcap_db_paperorders where order_id = '{}'".format(
                order_id)
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f"{e}, while Fetching data!!"}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")

def get_list_orders(sdate, edate, status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select order_id, trading_symbol as instrument, exchange, quantity as qty, transaction_type from sharkcap_db_paperorders where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {"Error": f"{e}, while fetching data!!"}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def delete_orderHistory_orders(order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE FROM sharkcap_db_paperorders where order_id = '{}'".format(
                order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": " Delete Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def delete_list_orders(sdate, edate, status):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE from sharkcap_db_paperorders where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("get_orderHistory_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    

# def insert_signal(order_id, strategy_id_id, instrument_id, order_time_in_force, order_side, user_token, order_type, order_status, signal_created_time):
#     try:
#         conn = psycopg2.connect(CONNECTION_AWS)
#         conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         try:
#             cur = conn.cursor(cursor_factory=RealDictCursor)
#             query = "INSERT INTO sharkcap_db_signal(order_id, strategy_id_id, order_side, user_token, order_type, order_status, signal_created_time) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(
#                 order_id, strategy_id_id, order_side, user_token, order_type, order_status, signal_created_time)
#             cur.execute(query)
#             conn.commit()
#             cur.close()
#             conn.close()
#             return {'Success': "Signal Generated!"}
#         except Exception as ex:
#             print(ex)
#             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail="sorry for inconvenience! please contact admin!!")
#     except Exception as ex:
#         print("insert_signal: exception in connecting to database")
#         print(ex)
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail="sorry for inconvenience! please contact admin!!")