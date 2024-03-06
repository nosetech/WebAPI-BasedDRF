from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User
from .permissions import IsMyselfOrAdmin, IsStaffOrReadOnly
from .serializer import UserSerializer


class MeView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        value = User.objects.get(uuid=request.user.uuid)
        return Response(
            data=UserSerializer(value).data,
            status=status.HTTP_200_OK,
        )


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsMyselfOrAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
