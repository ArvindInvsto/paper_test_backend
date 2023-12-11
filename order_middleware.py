import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_hostname, db_port, rds_db_name, rds_username, rds_password, BACKEND_LINK
from credentialManagement.credential import getDataFromStrategyId,getDataFromUserId
from expressManagement import loginExpress, placeOrder,loginPaper
from databaseManagement import saveOrderDetails, orderSignal


CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"

def pre_commit(brokerage,data):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        if brokerage == 'paperbrokerage':
            can_commit(conn,brokerage,data)
        else:
            try:
                cred = getDataFromUserId(data["userid"],brokerage)
                loginExpress(cred)
                can_commit(conn,brokerage,data)
            except Exception as ex:
                print(ex)



    except Exception as ex:
        print("getData: exception in connecting to database")
        print(ex)


def can_commit(conn,brokerage,data):
    try:
        if brokerage == 'paperbrokerage':
            commit(conn,brokerage,data)
        else:
            #reserve balance
            pass
    except Exception as ex:
        print(ex)

def commit(conn,brokerage,data):
    try:
        bro_paper=loginPaper(data["brokerage"])
        user = {"user_id":data["userid"]}
        orderPlaced = placeOrder(broker = bro_paper, msg = data, user_data = user)
        saveOrderDetails(broker=bro_paper, orderPlaced=orderPlaced,msg = data)
    except Exception as ex:
        print(ex)