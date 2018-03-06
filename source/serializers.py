from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class Search(serializers.Serializer):
	name_search = serializers.CharField(max_length=30, allow_blank=True) 
	color_search = serializers.CharField(max_length=30, allow_blank=True)
	date_search = serializers.CharField(max_length=30, allow_blank=True)
	floor_search = serializers.CharField(max_length=30, allow_blank=True)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')