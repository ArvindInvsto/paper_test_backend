from database.paperbrokerage import paperPositionApi

def insert_position_paper(userid,
                    tradingsymbol,
                    exchange,
                    product,
                    quantity,
                    average_price,
                    last_price):

    return paperPositionApi.insert_position_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                                product=product, quantity=quantity, average_price=average_price, last_price=last_price)


def get_positions_paper():

    return paperPositionApi.get_positions_paper()


def get_positions_by_tradingsymbol_paper(tradingsymbol):

    return paperPositionApi.get_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)


def update_position_paper(quantity, average_price, last_price, tradingsymbol):

    return paperPositionApi.update_position_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)


def update_position_margin(tradingsymbol, margin_required, m2m):

    return paperPositionApi.update_position_margin(
        tradingsymbol=tradingsymbol, margin_required=margin_required, m2m=m2m)


def delete_positions_by_tradingsymbol_paper(tradingsymbol):
    return paperPositionApi.delete_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
