from django.http import JsonResponse
from django.contrib.auth import get_user_model
from weibo_app.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .forms import SignupForm
from rest_framework.response import Response
from rest_framework import generics

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
        }
    )

    if form.is_valid():
        form.save()

    else:
        message = 'error'

    return JsonResponse({'status':message})


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    permission_classes = (AllowAny,) #  necessary if your default permission class is set to IsAuthenticated
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        # perform additional actions such as sending a welcome email

        return Response(user, status=status.HTTP_200_OK)