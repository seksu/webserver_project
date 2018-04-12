from rest_framework import serializers
from .models import Company, Camera_Detail

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class CameraSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    class Meta:
        model = Camera_Detail
        fields = ('id', 'token', 'company_name', 'company', 'floor', 'name', 'latitude', 'longitude')

    def get_company_name(self, CD):
        return CD.company.name if CD.company else "-"


class CameraAddSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100, allow_null=True)
    longitude = serializers.CharField(min_length=1)
    latitude = serializers.CharField(min_length=1)
    name = serializers.CharField(max_length=100, allow_null=True)
    floor = serializers.CharField(max_length=20, allow_null=True)
    company = serializers.IntegerField(allow_null=True)


class CameraDeleteSerializer(serializers.Serializer):
    camera_id = serializers.IntegerField(required=True)


class CompanyAddSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class CompanyDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class CompanySelectSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
