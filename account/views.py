from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, NotAuthenticated
from rest_framework.decorators import list_route

from .authenticate import CsrfExemptSessionAuthentication
from .serializers import UserLogInSerializer, RegisterSerializer, UserDeleteSerializer, \
                        ChangePasswordSerializer, ChangeNameSerializer
from camera.models import Company
from account.models import Account
from .permissions import IsSuperAdmin, IsUserAdmin, IsUserEmployee


class RegisterViewSet(viewsets.GenericViewSet):

    queryset = Account.objects.all()
    serializer_class = RegisterSerializer

    def get_permissions(self):
        if self.action == 'employee_register':
            self.permission_classes = [IsUserAdmin, ]
        elif self.action == 'useradmin_register':
            self.permission_classes = [IsSuperAdmin, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(RegisterViewSet, self).get_permissions()

    @list_route(methods=['post'], url_path='employee_register')
    def employee_register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if request.user.role == 1:
                company = Company.objects.filter(id=serializer.data['company']).first()
            elif request.user.role == 2:
                company = Company.objects.filter(id=request.user.company.id).first()

            account = Account.objects.create_user(
                email=serializer.data['email'],
                first_name=serializer.data['first_name'],
                last_name=serializer.data['last_name'],
                password=serializer.data['password'],
                company=company,
                role=3
            )
            account.set_password(serializer.data['password'])
            account.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'], url_path='useradmin_register')
    def useradmin_register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.filter(id=serializer.data['company']).first()
            account = Account.objects.create_user(
                email=serializer.data['email'],
                first_name=serializer.data['first_name'],
                last_name=serializer.data['last_name'],
                password=serializer.data['password'],
                company=company,
                role=2
            )
            account.set_password(serializer.data['password'])
            account.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Account.objects.all()
    serializer_class = UserDeleteSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]
        return super(UserDeleteViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            check_user = authenticate(email=request.user.email, password=serializer.data['password'])
            if not check_user:
                return Response({'error': 'password not match'}, status=status.HTTP_404_NOT_FOUND)

            user_target = Account.objects.filter(id=serializer.data['user_pk']).first()
            if not user_target:
                return Response({'error': 'user for delete not found'}, status=status.HTTP_404_NOT_FOUND)

            if request.user.role == 1:
                if user_target.role == 3:
                    user_target.delete()
                elif user_target.role == 2:
                    for employee in Account.objects.filter(company=user_target.company):
                        employee.delete()
                    user_target.delete()
            elif request.user.role == 2:
                if user_target.role == 3:
                    user_target.delete()

        return Response(status=status.HTTP_200_OK)


class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Account.objects.all()
    allow_redirects = True
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication,)
    serializer_class = UserLogInSerializer

    def create(self, request, *args, **kwargs):
        import re
        if request.user.is_authenticated:
            raise PermissionDenied('Please logout.')

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email', None)
            password = serializer.data.get('password')

            email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if email_regex.match(email):
                msg = 'This email or password is not valid.'
            else:
                msg = 'This email is wrong format'

            user = authenticate(email=email, password=password)
            if not user:
                return Response({"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

            login(request, user)
            request.session['ip'] = request.META.get('REMOTE_ADDR')
            request.session.set_expiry(3153600000)

            response = { "role": user.role }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountViewSet(viewsets.GenericViewSet):

    queryset = Account.objects.all()

    action_serializers = {
        'change_password': ChangePasswordSerializer,
        'change_name': ChangeNameSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
            return super().get_serializer_class()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]
        return super(AccountViewSet, self).get_permissions()

    @list_route(methods=['post'], url_path='change-password')
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            check_user = authenticate(email=request.user.email, password=serializer.data['old_password'])
            if not check_user:
                return Response({'error': 'password not match'}, status=status.HTTP_404_NOT_FOUND)
            check_user.set_password(serializer.data['new_password'])
            check_user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'], url_path='change-name')
    def change_name(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = Account.objects.filter(id=request.user.id).first()
            if serializer.data['first_name']:
                user.first_name = serializer.data['first_name']
            if  serializer.data['last_name']:
                user.last_name = serializer.data['last_name']
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        else:
            raise NotAuthenticated('Please login.')
