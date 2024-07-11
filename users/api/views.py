from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserSerializer
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data.get("password")
        if password:
            request.data["password"] = make_password(password)
        return super().partial_update(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        # Actualiza el timestamp del último acceso
        request.user.last_activity = timezone.now()
        request.user.save()
        return Response(serializer.data)


class UserStatusView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            # Considera al usuario en línea si su última actividad fue hace menos de 5 minutos
            online_threshold = timezone.now() - timezone.timedelta(minutes=1)
            is_online = user.last_activity > online_threshold
            return Response({"is_online": is_online})
        except User.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
