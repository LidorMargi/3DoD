from fastapi import FastAPI
from routes.orders import order

app = FastAPI()

app.include_router(order)

@app.get('/')
def read_root():
    return "Hello 3DoD"