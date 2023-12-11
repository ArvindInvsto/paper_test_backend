import traceback
from fastapi import HTTPException, status
import psycopg2
from datetime import datetime, timedelta
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def insert_position_paper(userid, tradingsymbol, exchange, product, quantity, average_price, last_price, margin_required, m2m):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "INSERT INTO sharkcap_db_paperpositions(userid, tradingsymbol, exchange, product, quantity, average_price, last_price, margin_required, m2m) VALUES('{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                userid, tradingsymbol, exchange, product, quantity, average_price, last_price, margin_required, m2m)
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
def get_positions_paper():
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperpositions".format()
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
        
def get_positions_by_tradingsymbol_paper(tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "SELECT * FROM sharkcap_db_paperpositions where tradingsymbol = '{}'".format(
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
    
def update_position_paper(quantity, average_price, last_price, tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperpositions set quantity = '{}', average_price = '{}', last_price = '{}' where tradingsymbol = '{}'".format(
                quantity, average_price, last_price, tradingsymbol)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Sucess": "Positon updated!"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def update_position_margin(tradingsymbol, margin_required, m2m):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "Update sharkcap_db_paperpositions set margin_required = '{}', m2m = '{}' where tradingsymbol = '{}'".format(
                margin_required, m2m, tradingsymbol)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Sucess": "Positon updated!"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")
    
def delete_positions_by_tradingsymbol_paper(tradingsymbol):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            query = "DELETE FROM sharkcap_db_paperpositions where tradingsymbol = '{}'".format(
                tradingsymbol)
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
            return {"Sucess": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}
    except Exception as ex:
        print("insert_paper_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")