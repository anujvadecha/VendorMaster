from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userBase.api.serializer import ActivateUserSerializer


class ActivateUser(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        print(request.data)
        print(request.user)
        user = request.user
        print(user)
        serializer = ActivateUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('success',status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
