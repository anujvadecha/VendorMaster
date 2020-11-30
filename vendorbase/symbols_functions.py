from django.core.cache import cache
from typing import List

from django.forms import model_to_dict

from base.decorators import timer
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderType, OrderStatus
from vendorbase.models import Symbol

def load_instruments():
    symbols=list(Symbol.objects.all())
    for symbol in symbols:
        cache.set(str(symbol.instrument_id),symbol)
        print("setting symbol"+str(symbol.instrument_id))
    return symbols
def get_instrument_data(instrument_id):
    symbol = cache.get(str(instrument_id))
    if symbol is None:
        print("loading from db")
        symbol = Symbol.objects.filter(instrument_id=instrument_id).first()
        cache.set(str(symbol.instrument_id), symbol)
    return symbol

def load_limit_orders_pending():
    orders=OrderSerializer(Order.objects.filter(type=OrderType.LIMIT).filter(status=OrderStatus.WAITING_FOR_LIMIT),many=True)
    cache.set("orders",orders)
    return orders


