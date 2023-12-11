from fastapi import Header, status, APIRouter

from logics import OrderbookAPI

router = APIRouter(tags=["orderbook"])


@router.get("/orderbook", status_code=status.HTTP_200_OK)
async def get_data(userid: str = Header(None)):
    return OrderbookAPI.get_orders(userid)