from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userBase.api.serializer import ActivateUserSerializer

@api_view(["PUT"])
def activateUser(request):
    print(request)
    serializer=ActivateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)