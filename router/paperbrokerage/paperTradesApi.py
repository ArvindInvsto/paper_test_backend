from fastapi import Header, status, APIRouter
from logics.paperbrokerage import paperTradesApi
from datetime import datetime, timedelta

router = APIRouter(prefix='/trades', tags=['Trades'])


@router.post('/insert')
def insert_trades_api(userid='XYZ123',
                      trade_id='01091',
                      order_id='10911',
                      tradingsymbol='NIFTYFUT',
                      exchange='NFO',
                      average_price=18019.5,
                      quantity=50,
                      transaction_type='BUY',
                      timestamp=datetime.utcnow() + timedelta(hours=5, minutes=30)):
    return paperTradesApi.insert_trade(userid=userid, trade_id=trade_id, order_id=order_id, exchange=exchange, tradingsymbol=tradingsymbol,
                                     average_price=average_price, quantity=quantity, transaction_type=transaction_type,
                                     timestamp=timestamp)


@router.get('/get')
def get_trades_api():

    return paperTradesApi.getTrade()


@router.get('/get_by_orderid')
def get_trade_by_orderid_api(orderid):

    return paperTradesApi.GetTradeByOrderID(order_id=orderid)


@router.get('/get_by_datetime')
def get_trade_by_datetime(startdate, enddate):

    return paperTradesApi.GetTradeByDate(startdate=startdate, enddate=enddate)


@router.delete('/delete_by_orderid')
def delete_trade_by_orderid_api(orderid):

    return paperTradesApi.deleteTradeByOrderID(order_id=orderid)


@router.delete('/delete_by_datetime')
def delete_trade_by_datetime(startdate, enddate):

    return paperTradesApi.deleteTradeByDate(startdate=startdate, enddate=enddate)
