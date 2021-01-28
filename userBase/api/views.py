from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userBase.api.serializer import ActivateUserSerializer
from vendorbase.api.serializers import UserRatingTextSerializer
from vendorbase.models import NormalUser


class ActivateUser(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        print(request.data)
        print(request.user)
        user = request.user
        print(user)
        request.data['requested_registration'] = True
        serializer = ActivateUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('success',status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserRatingView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        data = request.data
        user=UserRatingTextSerializer(data={'vendor_id': data['vendor_id'], 'user': request.user.pk, 'rating_text': data['rating_text']})
        if user.is_valid():
            user.save()
        else:
            print(user.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_obj=NormalUser.objects.filter(username=request.user).first()
        # print(user_obj)
        no_of_ratings=user_obj.no_of_ratings
        # print(no_of_ratings)
        rating=user_obj.avg_rating*no_of_ratings
        no_of_ratings=no_of_ratings+1
        avg_rating=(rating+data['rating'])/no_of_ratings
        # print(avg_rating)
        user_obj.no_of_ratings = no_of_ratings
        user_obj.avg_rating = avg_rating
        user_obj.save()
        return Response("success", status.HTTP_200_OK)