from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userBase.models import NormalUser
from vendorbase.api.serializers import NormalUserSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_normalUser(request):
    validation_user=NormalUser.objects.filter(user=request.user).all()
    return Response(NormalUserSerializer(validation_user,many=True).data,status=status.HTTP_200_OK)


class UserValidationView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        validation_user = NormalUser.objects.filter(user=request.user).all()
        return Response(NormalUserSerializer(validation_user, many=True).data, status=status.HTTP_200_OK)
    def post(self,request):
        normaluser=NormalUserSerializer(data=request.data)
        if normaluser.is_valid():
            normaluser.save()
            return Response(normaluser.data, status=status.HTTP_201_CREATED)
        return Response(normaluser.errors, status=status.HTTP_400_BAD_REQUEST)

