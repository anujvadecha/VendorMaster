from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order


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
        print(request.user.id)
        orders=Order.objects.filter(user_id=request.user)
        return Response(OrderSerializer(orders,many=True).data)
        # orders=Order.objects.filter(order_id__in=request.data["order_ids"])
        # return Response(OrderSerializer(orders,many=True).data)

