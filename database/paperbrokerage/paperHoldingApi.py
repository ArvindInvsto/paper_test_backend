import traceback
from fastapi import HTTPException, status
import psycopg2
from datetime import datetime, timedelta
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def insert_holding_paper(userid, tradingsymbol, exchange, product, quantity, average_price, last_price, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            pnl = float(quantity)*(float(last_price)-float(average_price))
            query = "INSERT INTO sharkcap_db_paperholding(userid, tradingsymbol, exchange, product, quantity, average_price, last_price, pnl, t1_quantity, realised_quantity, used_quantity, collateral_quantity) VALUES('{}','{}','{}','{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                userid, tradingsymbol, exchange, product, quantity, average_price, last_price, pnl, t1_quantity, realised_quantity, used_quantity, collateral_quantity)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Data inserted successfully!"}
        except Exception as e:
            return {'Error': f"{e}, while inserting data!"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def get_holding_paper():
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperholding".format()
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {"Error": f"{e}, while fetching data!"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def get_holding_by_tradingsymbol_paper(tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperholding where tradingsymbol = '{}'".format(
                tradingsymbol)
            cur.execute(query)
            data = cur.fetchone()
            cur.close()
            conn.close()
            return data
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def update_holding_paper(quantity, average_price, last_price, tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            pnl = float(quantity)*(float(last_price)-float(average_price))
            query = "Update sharkcap_db_paperholding set quantity = '{}', average_price = '{}', last_price = '{}', pnl='{}' where tradingsymbol = '{}'".format(
                quantity, average_price, last_price, pnl, tradingsymbol)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Sucess": "Holding updated!"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def update_quantity_holding_paper(tradingsymbol, quantity, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = f"Update sharkcap_db_paperholding set quantity='{quantity}', t1_quantity='{t1_quantity}', realised_quantity='{realised_quantity}', used_quantity='{used_quantity}', collateral_quantity='{collateral_quantity}' where tradingsymbol='{tradingsymbol}'"
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Holding quantity updated!"}
        except Exception as e:
            return {"Error": f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
def delete_holding_by_tradingsymbol_paper(tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE FROM sharkcap_db_paperholding where tradingsymbol = '{}'".format(
                tradingsymbol)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")