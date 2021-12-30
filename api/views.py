from knox.models import AuthToken
from rest_framework import generics, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from . import models
from .models import Worker
from .serializes import WorkerSerializer, RegisterSerializer, UserSerializer

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'workers': reverse('workers', request=request),
        'register': reverse('register', request=request),
        'login': reverse('login', request=request),
    })


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by('first_name')
    serializer_class = WorkerSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class WorkerView(generics.ListCreateAPIView):

    def get(self, request):
        workers = models.Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response({"workers": serializer.data})


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAdminUser,))
class WorkerList(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_level']