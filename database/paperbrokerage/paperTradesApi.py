import traceback
from fastapi import HTTPException, status
import psycopg2
from datetime import datetime, timedelta
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def insert_trade(trade_id, userid, order_id, exchange, tradingsymbol, average_price, quantity, transaction_type, timestamp):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "INSERT INTO sharkcap_db_papertraders(userid, trade_id, order_id, exchange, trading_symbol, average_price, quantity, transaction_type, timestamp)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(userid,
                                                                                                                                                                                                                    trade_id, order_id, exchange, tradingsymbol, average_price, quantity, transaction_type, timestamp)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Inserted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def GetTradeByDate(startdate, enddate):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select * from sharkcap_db_papertraders where timestamp between '{}' and '{}'".format(
                startdate, enddate)
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def GetTradeByOrderID(order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT average_price, timestamp as exchange_timestamp, trading_symbol FROM sharkcap_db_papertraders where order_id = '{}'".format(
                order_id)
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def getTrade():
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Select * from sharkcap_db_papertraders"
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def deleteTradeByDate(startdate, enddate):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Delete from sharkcap_db_papertraders where timestamp between '{}' and '{}'".format(
                startdate, enddate)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def deleteTradeByOrderID(order_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Delete FROM sharkcap_db_papertraders where order_id = '{}'".format(
                order_id)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")