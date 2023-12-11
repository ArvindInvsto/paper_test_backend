from fastapi import Header, status, APIRouter

from logics.paperbrokerage import paperOrdersApi
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/orders", tags=["Paper Order"])


@router.get('/get_all_paper_orders', status_code=status.HTTP_200_OK)
def get_orders_api():
    return paperOrdersApi.get_paper_orders()


@router.get('/get_by_orderid')
def get_by_orderid_orders_api(order_id: str):
    print("hello")
    return paperOrdersApi.get_orderHistory_orders(order_id=order_id)

@router.get('/get_order_detail_by_orderid')
def get_by_orderid_orders_api(order_id: str):
    return paperOrdersApi.get_by_orderid_orders_api(order_id=order_id)

@router.get('/get_by_datetime')
def get_by_datetime_orders_api(sdate: str, edate: str, status: str):
    return paperOrdersApi.get_list_orders(sdate=sdate, edate=edate, status=status)



@router.put('/update_status')
def update_status_orders_api(status: str, order_id: str):
    return paperOrdersApi.update_order_status_orders(
        status=status, order_id=order_id)

@router.put('/update_stoploss_price')
def update_stoploss_price_orders_api(stoploss_trigger_price, order_id):
    return paperOrdersApi.update_SLtrigger_price_orders(
        stoploss_trigger=stoploss_trigger_price, order_id=order_id)
    


@router.put('/update_complete_order')
def update_complete_orders_api(order_id, price):
    return paperOrdersApi.update_complete_orders(order_id=order_id, price=price)


@router.delete('/delete_by_orderid')
def delete_by_orderid_orders_api(order_id: str):
    return paperOrdersApi.delete_orderHistory_orders(order_id=order_id)


@router.delete('/delete_by_datetime')
def delete_by_datetime_orders_api(sdate: str, edate: str, status: str):
    return paperOrdersApi.delete_list_orders(
        sdate=sdate, edate=edate, status=status)
    
# signal api
# @router.post('/insertsignal', status_code=status.HTTP_201_CREATED)
# def insert_signal(order_id: str = Header(),
#                       strategy_id_id: str = Header(),
#                       order_side: str = Header(),
#                       order_type: str = Header(),
#                       order_status: str = Header(),
#                       instrument_id: int = Header(None),
#                       order_time_in_force: str = Header(None),
#                       user_token: str = Header(None)
#                       ):
#     signal_created_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
    
#     return paperOrdersApi.insert_signal(order_id=order_id, strategy_id_id=strategy_id_id, instrument_id=instrument_id, order_time_in_force=order_time_in_force, order_side=order_side,
#                                           user_token=user_token, order_type=order_type, order_status=order_status, signal_created_time=signal_created_time)

# testing object login
# from logics.user_threads.user_thread_handler import run_brokerage, my_dict

#V2ApiChanges
# def stop_thread(user_id):
#     my_dict.kill_thread(user_id)

# @router.get('/paper_brokerage_login', status_code=status.HTTP_200_OK)
# def login(userid: str = Header()):
#     brokerage_paper = run_brokerage(user_id=userid)
#     brokerage_paper.start()
#     my_dict.add_thread(userid, brokerage_paper)
#     print(my_dict.print_threads()) 



@router.post('/insert', status_code=status.HTTP_201_CREATED)
def insert_orders_api(userid: str = Header(),
                      trading_symbol: str = Header(),
                      qty: int = Header(),
                      exchange: str = Header(),
                      trans_type: str = Header(),
                      product: str = Header(),
                      order_type: str = Header(),
                      price: float = Header(),
                      stoploss_trigger: float = Header(),
                      status: str = Header(),
                      timestamp: str = Header()):

    return paperOrdersApi.insert_paper_orders(userid=userid, trading_symbol=trading_symbol, qty=qty, exchange=exchange, trans_type=trans_type,
                                          timestamp=timestamp, product=product, order_type=order_type, price=price, stoploss_trigger=stoploss_trigger, status=status)

# @router.post('/placeorder', status_code=status.HTTP_200_OK)
# def place_order(userid: str = Header()):
#     user = my_dict.dictionary[userid]
#     b = user.place_order()
#     print(b, user.userid)


# @router.post('/insert', status_code=status.HTTP_201_CREATED)
# def insert_orders_api(userid: str = Header(),
#                       trading_symbol: str = Header(),
#                       qty: int = Header(),
#                       exchange: str = Header(),
#                       trans_type: str = Header(),
#                       product: str = Header(),
#                       order_type: str = Header(),
#                       price: float = Header(),
#                       stoploss_trigger: float = Header(),
#                       status: str = Header(),
#                       timestamp: str = Header()):
    
#     return paperOrdersApi.insert_paper_orders(userid=userid, trading_symbol=trading_symbol, qty=qty, exchange=exchange, trans_type=trans_type,
#                                           timestamp=timestamp, product=product, order_type=order_type, price=price, stoploss_trigger=stoploss_trigger, status=status)

# from express import brokerage
# from pprint import pprint
# import threading

# class run_brokerage(threading.Thread):
#     def __init__(self, user_id):
#         threading.Thread.__init__(self)
#         self.bro_paper = brokerage.Paper()
#         self.userid = user_id
#         self.ret = None

#     def place_order(self):
#         self.ret = self.bro_paper.place_market_order(instrument="SBIN", exchange="NSE", order_side="BUY", qty=10, validity="DAY", variety="REGULAR", product_type="CNC")
#         return self.ret


# @router.get('/login', status_code=status.HTTP_200_OK)
# def login(userid: str = Header()):
#     brokerage_paper = run_brokerage(user_id=userid)
#     brokerage_paper.start()
#     a = brokerage_paper.place_order()
#     print(a)
#     print(brokerage_paper.userid)

#V2ApiChanges
# @router.post("/deactivate-thread", status_code=status.HTTP_200_OK)
# def DeactivateThread(user_id: str):
#     return my_dict.kill_thread(user_id)