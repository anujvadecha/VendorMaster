from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint

from django.forms import model_to_dict
from orderManagement.models import Order, OrderType, OrderStatus, OrderSide
from order_engine.instrument_engine import InstrumentEngine


# Single order manager per Instrument
class OrderManager():
    # TODO REPLACE IMPLEMENTATION FOR ORDERS WITH BST IMPLEMENTATION TESTED BEFORE, LETS KEEP IT A FOR LOOP FOR NOW
    orders = []

    def processOrders(self, tick):
        print(f"in here inside manager processing orders for {self.engine_instrument} {len(self.orders)} ")
        for order in self.orders:
            if (order.side == OrderSide.BUY):
                price = InstrumentEngine.getInstance().get_bid_price(self.engine_instrument, tick)
                if (order.price >= price):
                    order.status = OrderStatus.OPEN
                    order.save()
                    self.removeOrder(order)

            if (order.side == OrderSide.SELL):
                price = InstrumentEngine.getInstance().get_ask_price(self.engine_instrument, tick)
                if (order.price <= price):
                    order.status = OrderStatus.OPEN
                    order.save()
                    self.removeOrder(order)

    def addOrder(self, order):
        self.orders.append(order)

    def removeOrder(self, order):
        self.orders.remove(order)

    def __init__(self, instrument):
        self.engine_instrument = instrument

    def __str__(self):
        return f"orderManager {self.engine_instrument}"


class OrderEngine():

    var = ""

    def set_var(self, var):
        self.var = var

    instrument_orderengine_map = {}

    def start_order_engines(self):
        instruments = InstrumentEngine.getInstance().get_all_instruments()
        for instrument_id in instruments.keys():
            print("Starting order engine for instrument "+str(instrument_id))
            self.instrument_orderengine_map[instrument_id] = OrderManager(instrument_id)

    #   Single entrypoint once gold tick comes
    #   Will search for the order engine if tick is updated and push the task to thread pool executor to process orders
    def process_orders_on_gold_tick(self, gold_tick):
        print("my var is " + self.var)
        for engine in self.instrument_orderengine_map.values():
            engine.processOrders(gold_tick)
            # TODO:THREAD POOL EXECUTOR BE DONE LATER ONCE CODE IS FINAL SINCE ERRORS WONT BE THROWN FROM THREAD POOL EXECUTOR
            # self.executor.submit(engine.processOrders,gold_tick)

    def add_order(self, order):
        print("adding order")
        self.instrument_orderengine_map.get(model_to_dict(order)["instrument_id"]).addOrder(order)

    def load_orders(self):
        orders = Order.objects.filter(type=OrderType.LIMIT).filter(status=OrderStatus.WAITING_FOR_LIMIT)
        for order in orders:
            self.instrument_orderengine_map.get(model_to_dict(order)["instrument_id"]).addOrder(order)

    # To make class singleton
    def __init__(self):
        # self.executor = ThreadPoolExecutor(max_workers=100)
        InstrumentEngine.getInstance()
        self.start_order_engines()
        self.load_orders()
        """ Virtually private constructor. """
        if OrderEngine.__instance != None:
            raise Exception("This class is a OrderEngine!")
        else:
            OrderEngine.__instance = self

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if OrderEngine.__instance == None:
            OrderEngine()
        print(hex(id(OrderEngine.__instance)))
        return OrderEngine.__instance
