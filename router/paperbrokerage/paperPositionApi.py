from fastapi import Header, status, APIRouter
from logics.paperbrokerage import paperPositionApi
from datetime import datetime, timedelta

router = APIRouter(prefix='/position', tags=['position'])


@router.post('/insert')
def insert_position(userid='XYZ123',
                    tradingsymbol='NIFTYFUT',
                    exchange='NFO',
                    product='FUT',
                    quantity=50,
                    average_price=18019.5,
                    last_price=18100.5):

    return paperPositionApi.insert_position_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                                product=product, quantity=quantity, average_price=average_price, last_price=last_price)


@router.get('/get')
def get_position():

    return paperPositionApi.get_positions_paper()


@router.get('/get_by_tradingsymbol')
def get_position_by_tradingsymbol(tradingsymbol):

    return paperPositionApi.get_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)


@router.put('/update')
def update_position(quantity, average_price, last_price, tradingsymbol):

    return paperPositionApi.update_position_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)


@router.put('/updateMarginAndM2M')
def update_position_margin(tradingsymbol, margin_required, m2m):

    return paperPositionApi.update_position_margin(
        tradingsymbol=tradingsymbol, margin_required=margin_required, m2m=m2m)


@router.delete('/delte_by_tradingsymbol')
def delete_position_by_tradingsymbol(tradingsymbol):
    return paperPositionApi.delete_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
