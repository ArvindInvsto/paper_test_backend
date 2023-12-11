from database.paperbrokerage import paperOrdersApi


def insert_paper_orders(userid, trading_symbol, qty, exchange, trans_type,
                                          timestamp, product, order_type, price, stoploss_trigger, status):
    return paperOrdersApi.insert_paper_orders(userid=userid, trading_symbol=trading_symbol, qty=qty, exchange=exchange, trans_type=trans_type,
                                          timestamp=timestamp, product=product, order_type=order_type, price=price, stoploss_trigger=stoploss_trigger, order_status=status)



def get_paper_orders():
    return paperOrdersApi.get_paper_orders()


def get_orderHistory_orders(order_id: str):
    return paperOrdersApi.get_orderHistory_orders(order_id=order_id)

def get_by_orderid_orders_api(order_id: str):
    return paperOrdersApi.get_by_orderid_orders_api(order_id=order_id)

def get_list_orders(sdate: str, edate: str, status: str):
    return paperOrdersApi.get_list_orders(sdate=sdate, edate=edate, status=status)



def update_order_status_orders(status: str, order_id: str):
    return paperOrdersApi.update_order_status_orders(
        status=status, order_id=order_id)


def update_SLtrigger_price_orders(stoploss_trigger_price, order_id):
    return paperOrdersApi.update_SLtrigger_price_orders(
        stoploss_trigger=stoploss_trigger_price, order_id=order_id)
    


def update_complete_orders(order_id, price):
    return paperOrdersApi.update_complete_orders(order_id=order_id, price=price)


def delete_orderHistory_orders(order_id: str):
    return paperOrdersApi.delete_orderHistory_orders(order_id=order_id)


def delete_list_orders(sdate: str, edate: str, status: str):
    return paperOrdersApi.delete_list_orders(
        sdate=sdate, edate=edate, status=status)
    
# def insert_signal(order_id, strategy_id_id, instrument_id, order_time_in_force, order_side, user_token, order_type, order_status, signal_created_time):
#     return paperOrdersApi.insert_signal(order_id=order_id, strategy_id_id=strategy_id_id, instrument_id=instrument_id, order_time_in_force=order_time_in_force, order_side=order_side,
#                                           user_token=user_token, order_type=order_type, order_status=order_status, signal_created_time=signal_created_time)