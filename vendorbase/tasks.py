import time
from django.core.cache import cache
from orderManagement.models import Order, OrderType, OrderSide, OrderStatus
from .celery import  app
from .models import Symbol
from .symbols_functions import get_instrument_data, load_instruments, load_limit_orders_pending

@app.task
def process_limit_orders_gold(tick):
    pass

@app.task
def update_high_low(tick):
    tick=tick["gold_tick"]
    instruments=cache.get("instruments")
    for instrument in instruments:
        bid_price = tick["bid"] + instrument.buy_premium
        ask_price = tick["ask"] + instrument.sell_premium
        previous_high = cache.get(instrument.instrument_id).get("high")
        previous_low = cache.get(instrument.instrument_id).get("low")
        high=max(previous_high,bid_price,ask_price)
        low=min(previous_low,bid_price,ask_price)
        tostore={"high":high,"low":low,"bid":bid_price,"ask":ask_price}
        cache.set(instrument.instrument_id,tostore)
