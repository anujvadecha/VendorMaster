import json
import time
import logging
from celery import Celery
from instrument_engine import InstrumentEngine
from order_engine import OrderEngine
from websocket_config import create_web_socket

app = Celery('tasks')

def fill_orders(order_ids):
    order_websocket.send(data=json.dumps({
        "type":"order_filled",
        "order_ids":order_ids
    }))

@app.task
def process_orders(tick):
    return OrderEngine.getInstance().process_orders_on_gold_tick(tick)
try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    message=json.loads(message)
    # print(message)
    if(message.get("instruments")):
        message["instruments"]=json.loads(message["instruments"])
        InstrumentEngine.getInstance().load_all_instruments(symbols=message["instruments"])
    if (message.get("orders")):
        message["orders"] = json.loads(message["orders"])
        print("received orders"+str(len(message["orders"])))
        OrderEngine.getInstance().load_orders(orders=message["orders"])
    if(message.get("gold_tick")):
        process_orders(message)
    if(message.get("order_update")):
        message["order_update"]=json.loads(message["order_update"])
        OrderEngine.getInstance().add_order(message["order_update"])
    if(message.get("instrument_update")):
        message["instrument_update"] = json.loads(message["instrument_update"])
        InstrumentEngine.getInstance().update_add_instrument(message["instrument_update"])

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("retrying connection in 1 second")
    time.sleep(1)
    order_websocket=create_web_socket(onmessage=on_message,
                                      onclose=on_close,
                                      onopen=on_open,
                                      onerror=on_error)
    order_websocket.run_forever()
    print("### closed ###")

def on_open(ws):
    ws.send(json.dumps({
                "type": "ticker_request",
                'message': "Please send ticks! I beg you my Vendor Master"
            }))
    ws.send(json.dumps({
                "type": "all_orders_limit_pending",
                'message': "Please send orders! I beg you my Vendor Master"
            }))

order_websocket=create_web_socket(onmessage=on_message,onopen=on_open,onclose=on_close,onerror=on_error)
order_websocket.run_forever()
