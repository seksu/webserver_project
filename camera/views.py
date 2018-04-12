from .serializers import CompanySerializer, CameraSerializer, CameraAddSerializer, CameraDeleteSerializer, \
                        CompanyAddSerializer, CompanyDeleteSerializer, CompanySelectSerializer
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Company, Camera_Detail
from source.models import Searching_Detail
from account.models import Account
from account.permissions import IsSuperAdmin, IsUserAdmin
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

class CompanyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperAdmin, ]

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

class AddCompanyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyAddSerializer
    permission_classes = [IsSuperAdmin, ]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.create(
                name = serializer.data['name']
            )
            company.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCompanyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyDeleteSerializer
    permission_classes = [IsSuperAdmin, ]

    def create(self, request):
        import shutil
        import os
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company_id = serializer.data['id']
            company = Company.objects.filter(id=company_id).first()
            if company:
                try:
                    print('/home/pansek/webserver/media/'+company.name)
                    shutil.rmtree('/home/pansek/webserver/media/'+company.name)
                except:
                    print("can't delete folder")
                for obj_account in Account.objects.filter(company=company_id):
                    for obj_search in Searching_Detail.objects.filter(account=obj_account.id):
                        if obj_search.fullbody_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.fullbody_path)
                                os.remove('/home/pansek/workspace/'+obj_search.fullbody_path)
                            except:
                                print('no such file fullbody')
                        if obj_search.face_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.face_path)
                                os.remove('/home/pansek/workspace/'+obj_search.face_path)
                            except:
                                print('no such file face')
                        if obj_search.video_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.video_path)
                                os.remove('/home/pansek/workspace/'+obj_search.video_path)
                            except:
                                print('no such file video')
                for obj_camera in Camera_Detail.objects.filter(company=company_id):
                    for obj_search in Searching_Detail.objects.filter(camera=obj_camera.id):
                        if obj_search.fullbody_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.fullbody_path)
                                os.remove('/home/pansek/workspace/'+obj_search.fullbody_path)
                            except:
                                print('no such file fullbody')
                        if obj_search.face_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.face_path)
                                os.remove('/home/pansek/workspace/'+obj_search.face_path)
                            except:
                                print('no such file face')
                        if obj_search.video_path:
                            try:
                                print('/home/pansek/workspace/'+obj_search.video_path)
                                os.remove('/home/pansek/workspace/'+obj_search.video_path)
                            except:
                                print('no such file video')
                company.delete()
            else:
                return Response("not have company", status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera_Detail.objects.all()
    serializer_class = CompanySelectSerializer
    permission_classes = [IsUserAdmin, ]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            queryset = self.get_queryset()
            if request.user.role == 2:
                queryset = queryset.filter(company=request.user.company.id)
            elif request.user.role == 1:
                queryset = queryset.filter(company=serializer.data['id'])
            serializer = CameraSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddCameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera_Detail.objects.all()
    serializer_class = CameraAddSerializer

    def get_permissions(self):
        self.permission_classes = [IsUserAdmin, ]
        return super(AddCameraViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if request.user.role == 1:
                company = Company.objects.filter(id=serializer.data['company']).first()
            elif request.user.role == 2:
                company = Company.objects.filter(id=request.user.company.id).first()

            camera = Camera_Detail.objects.create(
                token = serializer.data['token'],
                longitude = serializer.data['longitude'],
                latitude = serializer.data['latitude'],
                date = timezone.now(),
                name = serializer.data['name'],
                floor = serializer.data['floor'],
                company=company,
            )
            camera.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCameraViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Camera_Detail.objects.all()
    serializer_class = CameraDeleteSerializer

    def get_permissions(self):
        self.permission_classes = [IsUserAdmin, ]
        return super(DeleteCameraViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            camera = Camera_Detail.objects.filter(id=serializer.data['camera_id']).first()
            for obj_search in Searching_Detail.objects.filter(camera=camera.id):
                if obj_search.fullbody_path:
                    try:
                        print('/home/pansek/workspace'+obj.fullbody_path)
                        os.remove('/home/pansek/workspace'+obj.fullbody_path)
                    except:
                        print('no such file fullbody')
                if obj_search.face_path:
                    try:
                        print('/home/pansek/workspace'+obj.face_path)
                        os.remove('/home/pansek/workspace'+obj.face_path)
                    except:
                        print('no such file face')
                if obj_search.video_path:
                    try:
                        print('/home/pansek/workspace'+obj.video_path)
                        os.remove('/home/pansek/workspace'+obj.video_path)
                    except:
                        print('no such file video')

            camera.delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
