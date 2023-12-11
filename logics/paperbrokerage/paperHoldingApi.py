from database.paperbrokerage import paperHoldingApi

def insert_holding_paper(userid,
                    tradingsymbol,
                    exchange,
                    product,
                    quantity,
                    average_price,
                    last_price):
    

    return paperHoldingApi.insert_holding_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                             product=product, quantity=quantity, average_price=average_price, last_price=last_price)
    


def get_holding_paper():
    

    return paperHoldingApi.get_holding_paper()



def get_holding_by_tradingsymbol_paper(tradingsymbol):
    

    return paperHoldingApi.get_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)



def update_holding_paper(quantity, average_price, last_price, tradingsymbol):
    

    return paperHoldingApi.update_holding_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)
    


def update_quantity_holding_paper(tradingsymbol, quantity, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
    

    return paperHoldingApi.update_quantity_holding_paper(tradingsymbol=tradingsymbol, quantity=quantity, t1_quantity=t1_quantity,
                                                      realised_quantity=realised_quantity, used_quantity=used_quantity, collateral_quantity=collateral_quantity)
    

def delete_holding_by_tradingsymbol_paper(tradingsymbol):
    

    return paperHoldingApi.delete_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    
