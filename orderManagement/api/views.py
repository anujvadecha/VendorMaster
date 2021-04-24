from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderStatus, OrderType, BestLimitUserMapping
from orderManagement.utils import unique_transaction_id_generator, unique_best_limit_id_generator
from vendorbase.api.serializers import UserMarginsSerializer
from vendorbase.models import VendorMargin, Symbol
import logging
from datetime import date
logger = logging.getLogger(__name__)

# @api_view(["POST"])
# def placeOrder(request):
#     if request.method=="POST":
#         serializer=OrderSerializer(data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(["GET"])
# def getOrderDetails(request):
#     if request.method=="GET":
#         # orders=Order.objects.filter(order_id__in=request.data["order_id"])
#         orders = Order.objects.all()
#         return Response(OrderSerializer(orders,many=True).data)

'''
    {
        'quantity':
        'instrument_id':['231423',234234,234324324]
        'side':
        'order_type':'BEST_LIMIT'
    }
'''
class OrderView(APIView):
    permission_classes = [ IsAuthenticated ]

    def add_order(self, order, user):
        print(f' adding order {order} ')
        serializer = OrderSerializer(data=order)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            print(serializer.errors)
            return None

    def patch(self,request):
        order =Order.objects.get(user_id=request.user,order_id=request.data["order_id"])
        order.comments = request.data['comment']
        order.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user)
        return Response(OrderSerializer(orders, many=True).data)

    def check_margin_for_order(self, order_request, user,instrument):
        margin_object = VendorMargin.objects.filter(user=user, vendor_id=instrument.vendor_id).first()
        if (margin_object == None):
            return Response('Margin for this user does not exist')
        if (margin_object.margin_available >= int(order_request['quantity'])):
            logger.info(f"Margin available is {margin_object.margin_available} order quantity {order_request['quantity']}")
            # margin_object.margin_available = margin_object.margin_available - int(order_request['quantity'])
            # margin_object.save()
            return True
        else:
            return False

    def post(self, request):
        print(request.data)
        request.data['user_id'] = request.user.id
        order_request = request.data
        if not request.user.is_activated:
            return Response('You need to activate your account')
        if (order_request['type'] == OrderType.BEST_LIMIT):
            order = None
            best_limit_mapping = BestLimitUserMapping.objects.create(user=request.user)
            order_request['best_limit_id'] = best_limit_mapping.pk
            for instrument in request.data['instrument_id']:
                order_request['instrument_id'] = instrument
                instrument = Symbol.objects.get(instrument_id=order_request['instrument_id'])
                margin_valid = self.check_margin_for_order(order_request, request.user,instrument)
                if not margin_valid:
                    return Response("Failed due to margin not available", status=status.HTTP_200_OK)
                else:
                    order = self.add_order(order_request, request.user)
            if order:
                return Response(order, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_200_OK)
        else:
            instrument = Symbol.objects.get(instrument_id=order_request['instrument_id'])
            margin_valid = self.check_margin_for_order(order_request, request.user,instrument)
            quantity_valid = self.check_quantity_for_order(order_request,instrument)
            # time_range_valid = self.check_time_range(order_request,instrument)
            if not margin_valid:
                return Response("Failed due to margin not available", status=status.HTTP_200_OK)
            elif not quantity_valid:
                return Response("Order less than minimum quantity", status=status.HTTP_200_OK)
            else:
                order = self.add_order(order_request, request.user)
                if order:
                    return Response(order, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_200_OK)

    def check_quantity_for_order(self, order_request, instrument):
        if(int(order_request['quantity']) >= int(instrument.quantity)):
            return True
        else:
            return False

    def time_in_range(start, end, x):
        """Return true if x is in the range [start, end]"""
        if start <= end:
            return start <= x <= end
        else:
            return start <= x or x <= end

    def check_time_range(self, order_request, instrument):
        if date.today().weekday() == 0 or date.today().weekday() == 1 or date.today().weekday() == 2 or date.today().weekday() == 3 or date.today().weekday() == 4 or date.today().weekday() == 5 :
            return self.time_in_range(datetime.time(9, 0, 0),datetime.time(11, 45, 0),datetime.now().time())


    def delete(self, request):
            order = Order.objects.get(order_id=request.data["order_id"])
            # margin = VendorMargin.objects.get(user=request.user, vendor_id=order.instrument_id.vendor_id)
            # margin.margin_available = margin.margin_available + order.quantity
            # margin.save()
            order.status = OrderStatus.CANCELLED
            order.save()
            return Response(status=status.HTTP_200_OK)



class UserMarginsView(APIView):
    def get(self, request):
        print(request.user)
        objects = VendorMargin.objects.filter(user=request.user.id)
        print(objects)
        return Response(UserMarginsSerializer(objects, many=True).data, status=status.HTTP_200_OK)


