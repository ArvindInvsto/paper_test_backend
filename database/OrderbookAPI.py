from fastapi import HTTPException, status
import psycopg2
import traceback
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_username, rds_password, rds_hostname, db_port, rds_db_name , hostname,  db_port, basket_db, basket_user, basket_pass

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"
c2 = f"postgres://{basket_user}:{basket_pass}@{hostname}:{db_port}/{basket_db}"


def get_all_orders(user_id):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            query = f'''SELECT subscriber_strategy_id,exchange_id,instrument_name,brokerage_id,average_price,order_type,updated_at,order_id,user_id,invsto_order_status,quantity,price,stoploss_trigger,order_side
                        FROM orderbook WHERE user_id = {user_id};'''
            
            cur = conn.cursor()
            cur.execute(query)

            column_names = [desc[0] for desc in cur.description]

            rows = cur.fetchall()
            order_list = []

            for row in rows:
                order_dict = {}
                for i, col_name in enumerate(column_names):
                    order_dict[col_name] = row[i]
                order_list.append(order_dict)
            
            return order_list

        except Exception as ex:
            print("get_all_orders: exception in querying")
            print(ex)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="sorry for inconvenience! please contact admin!!")

    except Exception as ex:
        print("get_all_orders: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")


def get_user(user_id: str):
    try:
        conn = psycopg2.connect(c2)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            user_table = "auth_user"
            query = f"SELECT * FROM {user_table} where id ={user_id}"
            cur = conn.cursor()
            cur.execute(query)
            if not cur.fetchone():
                cur.close()
                return False

            cur.close()
            return True

        except Exception as ex:
            print("get user", ex)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="sorry for inconvenience! please contact admin!!")

    except Exception as ex:
        print("get user: exception in connecting to database")
        print(ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="sorry for inconvenience! please contact admin!!")