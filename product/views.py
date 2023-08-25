from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import permissions as p
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Window
from .serializers import WindowSerializer
from .services import Service
from .permissions import IsOwner

# @api_view(['GET', 'POST'])
# def window_api(request):
#     try:
#         if request.method == "GET":
#             windows = Window.objects.all()
#             serializer = WindowSerializer(windows, many=True)
#             return Response(data=serializer.data, status=200)
#         else:
#             data = request.data
#             serializer = WindowSerializer(data=data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(data=serializer.data, status=200)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class WindowAPIView(generics.ListCreateAPIView):
    """ Лист всех окон """
    queryset = Service.fetch_all(Window)
    serializer_class = WindowSerializer
    permission_classes = [p.IsAuthenticated, IsOwner]
    authentication_classes =[
        JWTAuthentication    #/users/user_id/window/
    ]


class DetailWindowAPIView(generics.RetrieveUpdateAPIView):
    """ Конкретные окна """
    serializer_class = WindowSerializer
    queryset = Service.fetch_all(Window)
    lookup_field = 'id'
    permission_classes = [IsOwner, p.IsAuthenticated]


class UserWindowsListView(generics.ListAPIView):
    serializer_class = WindowSerializer
    queryset = Window.objects.all()
    permission_classes = []

    def list(self, request, *args, **kwargs):
        username = self.kwargs['username']
        windows = self.queryset.select_related('user').only('user__username').filter(user__username=username)
        serializer = self.serializer_class(windows, many=True)
        return Response(data=serializer.data, status=200)
