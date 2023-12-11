from fastapi import Header, status, APIRouter
from database.paperbrokerage import paperTradesApi

router = APIRouter(prefix='/trades', tags=['Trades'])


def insert_trade(userid,
                      trade_id,
                      order_id,
                      tradingsymbol,
                      exchange,
                      average_price,
                      quantity,
                      transaction_type,
                      timestamp):
    return paperTradesApi.insert_trade(userid=userid, trade_id=trade_id, order_id=order_id, exchange=exchange, tradingsymbol=tradingsymbol,
                                     average_price=average_price, quantity=quantity, transaction_type=transaction_type,
                                     timestamp=timestamp)


def getTrade():

    return paperTradesApi.getTrade()


def GetTradeByOrderID(orderid):

    return paperTradesApi.GetTradeByOrderID(order_id=orderid)


def GetTradeByDate(startdate, enddate):

    return paperTradesApi.GetTradeByDate(startdate=startdate, enddate=enddate)


def deleteTradeByOrderID(orderid):

    return paperTradesApi.deleteTradeByOrderID(order_id=orderid)


def deleteTradeByDate(startdate, enddate):

    return paperTradesApi.deleteTradeByDate(startdate=startdate, enddate=enddate)
