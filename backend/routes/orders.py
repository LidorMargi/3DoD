from fastapi import APIRouter, HTTPException
from models.orders import Order
import redis
import json

order = APIRouter()

redis_client = redis.Redis(host="redis", port=6379, db=0)


@order.get('/orders_list')
def find_all_orders():
    keys = redis_client.keys('order:*')
    orders = redis_client.mget(*keys)
    return [json.loads(order) for order in orders]

@order.post('/place_order')
def create_order(order: Order):
    order_id = f"order:{order.id}"
    order_data = json.dumps(order.model_dump())
    redis_client.set(order_id, order_data)
    name_key = f'orders_by_name:{order.name}'
    redis_client.sadd(name_key, order_id)
    return json.loads(order_data)

@order.put('/update_order/{order_id}')
def update_order(order_id: str, order: Order):
    order_key = f"order:{order_id}"
    exists = redis_client.exists(order_key)
    if not exists:
        raise HTTPException(status_code=404, detail="Order not found")
    updated_order_data = json.dumps(order.model_dump())
    redis_client.set(order_key, updated_order_data)
    return json.loads(updated_order_data)

@order.delete('/delete_order/{order_id}')
def delete_order(order_id: str):
    order_key = f"order:{order_id}"
    response = redis_client.delete(order_key)
    if response == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}