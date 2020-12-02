# '''
#     SingleTon instance that keeps track of all instruments in memory and updates their premium
# '''
# #   Used as a provider and updater for every instrument related feature for order_engine
# class InstrumentEngine():
#
#     instrument_map={}
#
#     def get_bid_price(self,instrument,tick):
#         #TODO ADD BANKRATE CALCULATIONS IF SYMBOL SOURCE IS BANKRATE
#         return self.instrument_map.get(instrument).get("buy_premium")+tick["gold_tick"]["bid"]
#
#     def get_ask_price(self,instrument,tick):
#         # TODO ADD BANKRATE CALCULATIONS IF SYMBOL SOURCE IS BANKRATE
#         return self.instrument_map.get(instrument.instrument_id).get("sell_premium") + tick["gold_tick"]["ask"]
#
#     def update_add_instrument(self,symbol):
#         self.instrument_map[symbol["instrument_id"]] =symbol
#
#     def load_all_instruments(self,symbols):
#         for symbol in symbols:
#             self.instrument_map[symbol["instrument_id"]]=symbol
#
#     def __init__(self):
#         if InstrumentEngine.__instance != None:
#             raise Exception("This class is a InstrumentEngine SingleTon!")
#         else:
#             InstrumentEngine.__instance = self
#
#     __instance = None
#     @staticmethod
#     def getInstance():
#         """ Static access method. """
#         if InstrumentEngine.__instance == None:
#             InstrumentEngine()
#         return InstrumentEngine.__instance
#
#     def get_all_instruments(self):
#         return self.instrument_map
