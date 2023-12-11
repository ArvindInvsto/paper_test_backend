from fastapi import Header, status, APIRouter

from logics.paperbrokerage import paperHoldingApi
from datetime import datetime, timedelta

router = APIRouter(prefix='/holding', tags=['holding'])

@router.post('/insert')
def insert_position(userid='XYZ123',
                    tradingsymbol='NIFTYFUT',
                    exchange='NFO',
                    product='FUT',
                    quantity=50,
                    average_price=18019.5,
                    last_price=18100.5):
    

    return paperHoldingApi.insert_holding_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                             product=product, quantity=quantity, average_price=average_price, last_price=last_price)
    


@router.get('/get')
def get_position():
    

    return paperHoldingApi.get_holding_paper()



@router.get('/get_by_tradingsymbol')
def get_position_by_tradingsymbol(tradingsymbol):
    

    return paperHoldingApi.get_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)



@router.put('/update')
def update_position(quantity, average_price, last_price, tradingsymbol):
    

    return paperHoldingApi.update_holding_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)
    


@router.put('/update_quantity')
def update_position(tradingsymbol, quantity, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
    

    return paperHoldingApi.update_quantity_holding_paper(tradingsymbol=tradingsymbol, quantity=quantity, t1_quantity=t1_quantity,
                                                      realised_quantity=realised_quantity, used_quantity=used_quantity, collateral_quantity=collateral_quantity)
    


@router.delete('/delete_by_tradingsymbol')
def delete_position_by_tradingsymbol(tradingsymbol):
    

    return paperHoldingApi.delete_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    
