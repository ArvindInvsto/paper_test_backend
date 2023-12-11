from datetime import datetime
import random
import string
import requests
import dotenv
import os

dotenv.load_dotenv()
OMS_hostname = os.getenv('OMS_hostname')

class Paper():
    def __init__(self):
        pass
    
    def login(self, userId: str, password: str, factor2: str, vc: str, api_key: str, imei: str):

        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=30))

         # Change return formate
        retDic={
            'time': nowtime,
            'userid': userId,
            'name': 'XYZ',
            'email': 'XYZ@gmail.com',
            'token': token
            }
        
        return retDic

    def set_session(self, user_id, password, token):

        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # Change return formate
        retDic={
            'time': nowtime,
            'userid': user_id,
            'name': 'XYZ',
            'email': 'XYZ@gmail.com',
            }
        
        return retDic

    def get_order_detail(self, orderNumber):
        print("getting order details...")
        '''
        ret: [ { "stat": "Ok", "norenordno": "20121300065716", "uid": "DEMO01", "actid": "DEMO01", "exch": "NSE", "tsym": "ACCELYA-EQ", "qty": "180", "trantype": "B", "prctyp": "LMT", "ret": "DAY", "token": "7053", "pp": "2", "ls": "1", "ti": "0.05", "prc": "800.00", "avgprc": "800.00", "dscqty": "0", "prd": "M", "status": "COMPLETE", "rpt": "Fill", "fillshares": "180", "norentm": "19:59:32 13-12-2020", "exch_tm": "00:00:00 01-01-1980", "remarks": "WC TEST Order", "exchordid": "6858" }, { "stat": "Ok", "norenordno": "20121300065716", "uid": "DEMO01", "actid": "DEMO01", "exch": "NSE", "tsym": "ACCELYA-EQ", "qty": "180", "trantype": "B", "prctyp": "LMT", "ret": "DAY", "token": "7053", "pp": "2", "ls": "1", "ti": "0.05", "prc": "800.00", "dscqty": "0", "prd": "M", "status": "OPEN", "rpt": "New", "norentm": "19:59:32 13-12-2020", "exch_tm": "00:00:00 01-01-1980", "remarks": "WC TEST Order", "exchordid": "6858" }, { "stat": "Ok", "norenordno": "20121300065716", "uid": "DEMO1", "actid": "DEMO1", "exch": "NSE", "tsym": "ACCELYA-EQ", "qty": "180", "trantype": "B", "prctyp": "LMT", "ret": "DAY", "token": "7053", "pp": "2", "ls": "1", "ti": "0.05", "prc": "800.00", "dscqty": "0", "prd": "M", "status": "PENDING", "rpt": "PendingNew", "norentm": "19:59:32 13-12-2020", "remarks": "WC TEST Order" }, { "stat": "Ok", "norenordno": "20121300065716", "uid": "DEMO1", "actid": "DEMO1", "exch": "NSE", "tsym": "ACCELYA-EQ", "qty": "180", "trantype": "B", "prctyp": "LMT", "ret": "DAY", "token": "7053", "pp": "2", "ls": "1", "ti": "0.05", "prc": "800.00", "prd": "M", "status": "PENDING", "rpt": "NewAck", "norentm": "19:59:32 13-12-2020", "remarks": "WC TEST Order" } ]
        '''
        response = requests.get( OMS_hostname + "orders/get_order_detail_by_orderid?order_id=" + f"{orderNumber}")
        order_response = response.json()[0]
        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        randprice = ''.join(random.choices(string.digits, k=4))
        
        # Change the return format
        newretDic={
            'timestamp':order_response["timestamp"],
            'orderno': orderNumber,
            'instrument': order_response["trading_symbol"],
            'exchange': order_response["exchange"],
            'qty': order_response["quantity"],
            'order_side': order_response["transaction_type"], # Get RetParameter from fuction
            'product_type': order_response["order_type"], # Get RetParameter from fuction
            'price': order_response["price"],
            'status': order_response["status"]
        }
        print("order details:",newretDic)
        return newretDic

    def place_market_order(self, instrument, exchange, order_side, qty, validity, variety, product_type):
        
        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        orderno=''.join(random.choices(string.digits, k=10))
        
        # Change the return format
        newretDic={'time':nowtime, 'orderno': orderno}
        return newretDic

    def place_limit_order(self, instrument, exchange, order_side, qty, validity, variety, product_type, limit_price):
        
        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        orderno=''.join(random.choices(string.digits, k=10))
        
        # Change the return format
        newretDic={'time':nowtime, 'orderno': orderno}
        return newretDic


    def position_squareOff(self, id):
        
        nowtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        # Change the return format
        newretDic={'time':nowtime, 'orderno': id}
        return newretDic
