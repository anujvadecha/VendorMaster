from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userBase.models import NormalUser
from vendorbase.api.serializers import NormalUserSerializer, FavouriteSerializer
from vendorbase.models import Favourite
from vendorbase.models import Symbol
from vendorbase.api.serializers import NormalUserSerializer, SymbolSerializer

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

    def get(self,request):
        favourites=Favourite.objects.filter(user_id=request.user)
        return Response(FavouriteSerializer(favourites,many=True).data,status=status.HTTP_200_OK)

    def post(self,request):
        print(request.user)
        print(request.data)
        data=request.data
        # Favourite(user_id=request.user, instrument_id=request.data["instrument_id"]).save()
        favourite = FavouriteSerializer(data={"user_id":request.user.id, "instrument_id": request.data["instrument_id"]})
        if favourite.is_valid():
            favourite.save()
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(favourite.errors)

    def delete(self, request):
        print(request.user)
        print(request.data)
        Favourite.objects.filter(user_id=request.user, instrument_id=request.data).delete()
        return Response("Instrument has been deleted from favourites")