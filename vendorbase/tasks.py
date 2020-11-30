import time
from django.core.cache import cache
from orderManagement.models import Order, OrderType, OrderSide, OrderStatus
from order_engine.instrument_engine import InstrumentEngine
from order_engine.order_engine import OrderEngine
from .celery import  app
from .symbols_functions import get_instrument_data, load_instruments, load_limit_orders_pending

@app.task
def process_limit_orders_gold(tick):
    pass
    # tic = time.perf_counter()
    # instruments = load_instruments()
    # limit_orders=load_limit_orders_pending()
    # toc = time.perf_counter()
    # print(f"loaded eligible orders and instruments in {toc - tic:0.4f} seconds")
    # for order in limit_orders:
    #     if order.side == OrderSide.BUY:
    #         buy_price = get_instrument_data(instrument_id='3439ca7c-cf78-4826-94b0-530b94c203e4').buy_premium + tick['gold_tick']['bid']
    #         if(order.price<=buy_price):
    #             order.status = OrderStatus.OPEN
    #             order.save()
    # toc = time.perf_counter()
    # print(f"executed processing in {toc - tic:0.4f} seconds")
    # print("executed")
    # elif order.side == OrderSide.SELL:
    #     if(order.price>order.instrument_id.get_sell_price_from_tick(tick["gold_tick"])):
    #         order.status = OrderStatus.OPEN
    #         order.save()

