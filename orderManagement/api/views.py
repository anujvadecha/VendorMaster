from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order
from vendorbase.api.serializers import UserMarginsSerializer
from vendorbase.models import VendorMargin


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
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        print(request.data)
        Order.objects.filter(order_id=request.data["order_id"]).delete()
        return Response(status=status.HTTP_200_OK)

class UserMarginsView(APIView):
    def get(self,request):
        print(request.user)
        objects = VendorMargin.objects.filter(user=request.user.id)
        print(objects)
        return Response(UserMarginsSerializer(objects,many=True).data,status=status.HTTP_200_OK)

