from .serializers import CompanySerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Company
from account.permissions import IsSuperAdmin

class CompanyViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [IsSuperAdmin, ]

    def get_permissions(self):
        self.permission_classes = [IsSuperAdmin, ]
        return super(CompanyViewSet, self).get_permissions()

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
