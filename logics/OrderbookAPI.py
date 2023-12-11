from fastapi import HTTPException, status
from database.OrderbookAPI import get_user, get_all_orders

def get_orders(userid):
    if get_user(userid):
        return get_all_orders(userid)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")