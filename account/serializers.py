from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes, model_meta

from account.models import Account


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255, allow_blank=False)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=4)
    company = serializers.IntegerField(allow_null=True)


class UserLogInSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=4)


class UserDeleteSerializer(serializers.Serializer):

    user_pk = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)


class UserInActiveSerializer(serializers.Serializer):

    user_pk = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True)


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(min_length=4, required=True)
    new_password = serializers.CharField(min_length=4, required=True)


class ChangeNameSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=255, required=True, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=True, allow_blank=True)


class ImageUploadSerializer(serializers.Serializer):

    number = serializers.CharField(max_length=255, required=True)
    base64 = serializers.CharField(min_length=1, required=True)


class CompanySelectSerializer(serializers.Serializer):

    id = serializers.IntegerField(allow_null=True)


class ViewUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name', 'last_name', 'facepath')


class AccountListSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name', 'last_name', 'role', 'company_name', 'active', 'facepath')

    def get_company_name(self, AC):
        return AC.company.name if AC.company else "-"

    def get_role(self, AC):
        return AC.get_role_display()
