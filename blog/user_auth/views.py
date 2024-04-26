from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from user_auth.serializers import UserSerializer

# Create your views here.


class UserView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        obj = self.request.user

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
