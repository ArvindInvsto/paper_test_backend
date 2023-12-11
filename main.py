from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.paperbrokerage import paperOrdersApi,  paperTradesApi, paperPositionApi, paperHoldingApi
from startup_functions import on_startup
from router import orderbook
from priceDataframe import priceDataframe_api
from priceDatabase import priceDatabase_api


app = FastAPI(title="ORDER-MANAGEMENT-SYSTEM", reload = False)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await on_startup()



app.include_router(priceDatabase_api)
app.include_router(priceDataframe_api)


app.include_router(paperOrdersApi.router)
app.include_router(paperTradesApi.router)
app.include_router(paperPositionApi.router)
app.include_router(paperHoldingApi.router)

app.include_router(orderbook.router)