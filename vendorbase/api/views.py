from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orderManagement.models import Order
from userBase.models import NormalUser
from vendorbase.api.serializers import FavouriteSerializer, UserMarginsSerializer, \
    SupportSerializer, VendorDetailsSerializer, VendorRatingTextSerializer
from vendorbase.models import Favourite, VendorMargin, VendorDetails, VendorRatingText
from vendorbase.models import Symbol, Vendor
from vendorbase.api.serializers import NormalUserSerializer, SymbolSerializer, VendorSerializer

# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_normalUser(request):
#     validation_user=NormalUser.objects.filter(user=request.user).all()
#     return Response(NormalUserSerializer(validation_user,many=True).data,status=status.HTTP_200_OK)
#

# class UserValidationView(APIView):
# permission_classes = [IsAuthenticated]

# def get(self, request):
#     validation_user = NormalUser.objects.filter(user=request.user).all()
#     return Response(NormalUserSerializer(validation_user, many=True).data, status=status.HTTP_200_OK)
#
# def post(self,request):
#     normaluser=NormalUserSerializer(data=request.data)
#     if normaluser.is_valid():
#         normaluser.save()
#         return Response(normaluser.data, status=status.HTTP_201_CREATED)
#     return Response(normaluser.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourites = Favourite.objects.filter(user_id=request.user)
        return Response(FavouriteSerializer(favourites, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        # Favourite(user_id=request.user, instrument_id=request.data["instrument_id"]).save()
        favourite = FavouriteSerializer(
            data={"user_id": request.user.id, "instrument_id": request.data["instrument_id"]})
        if favourite.is_valid():
            favourite.save()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(favourite.errors)

    def delete(self, request):
        Favourite.objects.filter(
            user_id=request.user, instrument_id=request.data['instrument_id']).delete()
        return Response("Instrument has been deleted from favourites")


class SupportView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['user_id'] = request.user.id
        support = SupportSerializer(data=request.data)
        if(support.is_valid()):
            support.save()
            return Response("success", status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VendorRatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        vendor = VendorRatingTextSerializer(
            data={'vendor_id': request.data["vendor_id"], "user": request.user.pk, "rating_text": request.data["rating_text"]})
        if vendor.is_valid():
            vendor.save()
        else:
            print(vendor.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        order = Order.objects.filter(order_id=data['order_id']).first()
        order.is_rated = True
        order.save()
        vendor_obj = VendorDetails.objects.filter(
            vendor_id=data['vendor_id']).first()
        no_of_ratings = vendor_obj.no_of_ratings
        rating = vendor_obj.avg_rating*no_of_ratings
        no_of_ratings = no_of_ratings+1
        avg_rating = (rating+data['rating'])/no_of_ratings
        vendor_obj.no_of_ratings = no_of_ratings
        vendor_obj.avg_rating = avg_rating
        # vendor=VendorDetailsSerializer(data={'vendor_id': data['vendor_id'], 'avg_rating': avg_rating, 'no_of_ratings': no_of_ratings})
        vendor_obj.save()
        return Response("success", status.HTTP_200_OK)


class VendorRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self):
        return Response(VendorSerializer(Vendor.objects.filter(enabled=True), many=True).data, status=status.HTTP_200_OK)


class TickerRequestView(APIView):
    def get(self):
        pass


class UserMarginCron(APIView):
    def post(self, request):
        margins = VendorMargin.objects.all()
        # print(margins)
        for m in margins:
            m.margin_available = m.margin
            m.save()
        return Response("success", status.HTTP_200_OK)


class BankRateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data = request.data
        vendor=Vendor.objects.filter(user_id=request.user).first()
        print(vendor)
        vendor.gold_premium=data["gold_premium"]
        vendor.gold_999_premium=data["gold_999_premium"]
        vendor.silver_premium=data["silver_premium"]
        vendor.gold_conv=data["gold_conv"]
        vendor.gold_999_conv=data["gold_999_conv"]
        vendor.silver_conv=data["silver_conv"]
        vendor.gold_custom=data["gold_custom"]
        vendor.gold_999_custom=data["gold_999_custom"]
        vendor.silver_custom=data["silver_costom"]
        vendor.gold_dollar_premium=data["gold_dollar_premium"]
        vendor.gold_999_dollar_premium=data["gold_999_dollar_premium"]
        vendor.silver_dollar_premium=data["silver_dollar_premium"]
        vendor.gold_tax=data["gold_tax"]
        vendor.gold_999_tax=data["gold_999_tax"]
        vendor.silver_tax=data["silver_tax"]
        vendor.save()
        return Response("success",status=status.HTTP_200_OK)
