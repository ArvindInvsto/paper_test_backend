from fastapi import HTTPException, status, Request
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor
from database import rds_hostname, db_port, rds_db_name, rds_username, rds_password
import pandas as pd

CONNECTION_AWS = f"postgres://{rds_username}:{rds_password}@{rds_hostname}:{db_port}/{rds_db_name}"


def saveCredential(
        strategySubscriberId,
        userId,
        strategyId,
        BrokerageName = "paper",
        BrokeraguserId = None,
        password = None,
        factor2 = None,
        api_key = None,
        api_secret =None,
        vc = None,
        imei =None,
        auth_code=None,
        isActive=False,
        token=None):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            # add data
            query=f'INSERT INTO Users Values("{strategySubscriberId}", "{userId}", "{strategyId}", "{BrokerageName}", "{BrokeraguserId}", "{password}", "{factor2}", "{api_key}", "{api_secret}", "{vc}", "{imei}", "{auth_code}", "{isActive}","{token}")'
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
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
        


# def paperAuth(brokerage_user_id, password, factor2, vc, api_key, imei):
#     try:
#         conn = psycopg2.connect(CONNECTION_AWS)
#         conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         try:
#             query="""SELECT EXISTS(SELECT 1 FROM sharkcap_db_brokerage_setting WHERE brokerage_user_id = %s AND password = %s AND factor2 = %s AND vc = %s AND api_key = %s AND imei = %s)"""
#             cur = conn.cursor(cursor_factory=RealDictCursor)
#             cur.execute(query, (brokerage_user_id, password, factor2, vc, api_key, imei))
#             result = cur.fetchone()
#             conn.commit()
#             cur.close()
#             conn.close()
#             print(result)
#             return result
#         except Exception as ex:
#                 print("getData: exception in querying")
#                 print(ex)
#                 raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                                     detail="sorry for inconvenience! please contact admin!!")
#     except Exception as ex:
#         print("getData: exception in connecting to database")
#         print(ex)
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail="sorry for inconvenience! please contact admin!!")
#     if result is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
#     return result


def saveToken(brokerage_user_id, token):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            # add data
            query="""Update sharkcap_db_strategy_subscriber set token = %s WHERE brokerage_user_id=%s"""
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query, (token, brokerage_user_id))
            conn.commit()
            cur.close()
            conn.close()
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

# def getDataFromStrategyId(strategyId):
    # try:
    #     conn = psycopg2.connect(CONNECTION_AWS)
    #     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #     try:
    #         query=f"""SELECT * FROM brokerage_credentials where strategy_id = %s;"""
    #         cur = conn.cursor(cursor_factory=RealDictCursor)
    #         cur.execute(query, (strategyId,))
    #         # Convert to the dataframe
    #         data=pd.DataFrame(cur.fetchall(), columns=["strategy_subscriber_id", "user_id", "strategy_id", "brokerage_name", "brokerage_user_id", "password", "factor_two", "api_key", "api_secret", "verification_code", "imei", "authorization_code", "is_active","token"])
    #         conn.commit()
    #         cur.close()
    #         conn.close()
    #         return data
    #     except Exception as ex:
    #             print("getData: exception in querying")
    #             print(ex)
    #             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                                 detail="sorry for inconvenience! please contact admin!!")
    # except Exception as ex:
    #     print("getData: exception in connecting to database")
    #     print(ex)
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                         detail="sorry for inconvenience! please contact admin!!")
    
def getDataFromStrategyId(strategyId):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            query=f"""SELECT * FROM sharkcap_db_strategy_subscriber where strategy_id = %s;"""
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query, (strategyId,))
            # Convert to the dataframe
            data=pd.DataFrame(cur.fetchall(), columns=["strategy_subscription_id", "user_id", "strategy_id", "brokerage_setting_id", "password", "factor2", "vc", "api_key", "api_secret_key", "imei", "token", "brokerage", "is_active", "brokerage_user_id"])
            conn.commit()
            cur.close()
            conn.close()
            return data
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
    

def getDataFromUserId(userId,brokerage):
    try:
        conn = psycopg2.connect(CONNECTION_AWS)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        try:
            # get data
            print(userId)
            query=f"SELECT * FROM sharkcap_db_brokerage_setting  where user_id = {userId} and brokerage = {brokerage}"
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            # Convert to the dataframe
            print(cur)
            data=pd.DataFrame(cur.fetchall(), columns=["brokerage_setting_id", "brokerage","user_id", "strategy_id",  "password", "factor2","vc", "api_key", "api_secret_key", "imei", "token","brokerage_user_id", "is_active"])
            conn.commit()
            cur.close()
            conn.close()
            print(data)
            return data
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
    

if __name__=="__main__":
    # saveCredential("FC1021", "US11", "S001", "paper", "KMNP", "password", "akfhf", "ahioa", isActive=True)
    pass