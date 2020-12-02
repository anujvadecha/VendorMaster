from concurrent.futures.thread import ThreadPoolExecutor
from instrument_engine import InstrumentEngine

class OrderSide():
    BUY="BUY"
    SELL="SELL"

class OrderStatus():
    OPEN="OPEN"
    EXECUTED="EXECUTED"
    CLOSED="CLOSED"
    CANCELLED="CANCELLED"
    WAITING_FOR_LIMIT="WAITING_FOR_LIMIT"

class OrderType():
    MARKET = "MARKET"
    LIMIT = "LIMIT"

class OrderManager():
    # TODO REPLACE IMPLEMENTATION FOR ORDERS WITH BST IMPLEMENTATION TESTED BEFORE, LETS KEEP IT A FOR LOOP FOR NOW
    # WINKS A FOR LOOP ITSELF PROCESSES IN 1 MS FOR 200 milliseconds
    orders = {}
    def processOrders(self, tick):
        print(f"processing orders for instrument {self.engine_instrument} {len(self.orders)} ")
        orders_to_fill=[]
        from tasks import fill_orders
        for order in self.orders.values():
            if(order["type"]==OrderType.LIMIT):
                if (order["side"] == OrderSide.BUY):
                    price = InstrumentEngine.getInstance().get_bid_price(self.engine_instrument, tick)
                    if (order["price"] >= price):
                        order["status"] = OrderStatus.OPEN
                        print("need to fill order "+order["order_id"])
                        orders_to_fill.append(order["order_id"])
                if (order["side"] == OrderSide.SELL):
                    price = InstrumentEngine.getInstance().get_ask_price(self.engine_instrument, tick)
                    if (order["price"] <= price):
                        order["status"] = OrderStatus.OPEN
                        orders_to_fill.append(order["order_id"])
        if(len(orders_to_fill)>0):
            fill_orders(orders_to_fill)
        for order_id in orders_to_fill:
            self.orders.pop(order_id)

    def addOrder(self, order):
        self.orders[order["order_id"]]=order

    def clear_orders(self):
        self.orders.clear()

    def __init__(self, instrument):
        self.engine_instrument = instrument

    def __str__(self):
        return f"orderManager {self.engine_instrument}"

class OrderEngine():
    instrument_ordermanager_map = {}
    def start_order_engines(self):
        instruments = InstrumentEngine.getInstance().get_all_instruments()
        print("instruments for starting"+str(instruments))
        for instrument_id in instruments.keys():
            print("Starting order engine for instrument "+str(instrument_id))
            self.instrument_ordermanager_map[instrument_id] = OrderManager(instrument_id)

    #   Single entrypoint once gold tick comes
    #   Will search for the order engine if tick is updated and push the task to thread pool executor to process orders
    def process_orders_on_gold_tick(self, gold_tick):
        for engine in self.instrument_ordermanager_map.values():
            engine.processOrders(gold_tick)
            # TODO:THREAD POOL EXECUTOR BE DONE LATER ONCE CODE IS FINAL SINCE ERRORS WONT BE THROWN FROM THREAD POOL EXECUTOR
            # self.executor.submit(engine.processOrders,gold_tick)

    def add_order(self, order):
        self.instrument_ordermanager_map.get(order["instrument_id"]).addOrder(order)

    def clear_all_orders(self):
        for engine in self.instrument_ordermanager_map.values():
            engine.clear_orders()

    def load_orders(self,orders):
        self.clear_all_orders()
        for order in orders:
            self.instrument_ordermanager_map.get(order["instrument_id"]).addOrder(order)

    def __init__(self):
        # self.executor = ThreadPoolExecutor(max_workers=100)
        InstrumentEngine.getInstance()
        self.start_order_engines()
        """ Virtually private constructor. """
        if OrderEngine.__instance != None:
            raise Exception("This class is a OrderEngine SINGLETON!")
        else:
            OrderEngine.__instance = self

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if OrderEngine.__instance == None:
            OrderEngine()
        return OrderEngine.__instance
