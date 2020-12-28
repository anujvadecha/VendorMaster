from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderStatus
from vendorbase.api.serializers import UserMarginsSerializer
from vendorbase.models import VendorMargin, Symbol
import logging
logger=logging.getLogger(__name__)

@api_view(["POST"])
def placeOrder(request):
    if request.method=="POST":
        serializer=OrderSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getOrderDetails(request):
    if request.method=="GET":
        # orders=Order.objects.filter(order_id__in=request.data["order_id"])
        orders=Order.objects.all()
        return Response(OrderSerializer(orders,many=True).data)

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        orders = Order.objects.all()
        print(request.user)
        return Response(OrderSerializer(orders, many=True).data)

    def post(self,request):
        request.data['user_id']=request.user.id
        serializer = OrderSerializer(data=request.data)
        instrument = Symbol.objects.get(instrument_id=request.data['instrument_id'])
        logger.info(f"Order request received {request.data}")
        margin_object = VendorMargin.objects.filter(user=request.user,vendor_id=instrument.vendor_id).first()
        if(margin_object==None):
            return Response('Margin for this user does not exist')
        if( margin_object.margin_available >= int(request.data['quantity'])):
            logger.info(f"Margin available is {margin_object.margin_available} order quantity {request.data['quantity']}")
            margin_object.margin_available = margin_object.margin_available - int(request.data['quantity'])
            margin_object.save()
        else:
            return Response("Failed due to margin not available",status=status.HTTP_200_OK)
        if( not request.user.is_activated):
            return Response('You need to activate your account')
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_200_OK)

    def delete(self,request):
        print(request.data)
        order=Order.objects.get(order_id=request.data["order_id"])
        margin = VendorMargin.objects.get(user=request.user, vendor_id=order.instrument_id.vendor_id)
        margin.margin_available=margin.margin_available+order.quantity
        margin.save()
        order.status=OrderStatus.CANCELLED
        order.save()
        return Response(status=status.HTTP_200_OK)

class UserMarginsView(APIView):
    def get(self,request):
        print(request.user)
        objects = VendorMargin.objects.filter(user=request.user.id)
        print(objects)
        return Response(UserMarginsSerializer(objects,many=True).data,status=status.HTTP_200_OK)

