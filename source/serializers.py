from rest_framework import serializers
from .models import Searching_Detail


class SearchAdminSerializer(serializers.Serializer):
	red = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	green = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	blue = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	date = serializers.ListField(child=serializers.CharField(min_length=1, allow_null=True))
	stage = serializers.IntegerField(required=True)
	pos_left_top = serializers.ListField(child=serializers.DecimalField(max_digits=25, decimal_places=20))
	pos_right_bot= serializers.ListField(child=serializers.DecimalField(max_digits=25, decimal_places=20))

class SearchSerializer(serializers.Serializer):
	pic_search = serializers.CharField(min_length=1, allow_null=True)
	red = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	green = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	blue = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=255))
	date = serializers.ListField(child=serializers.CharField(min_length=1, allow_null=True))
	floor = serializers.ListField(child=serializers.CharField(min_length=1, allow_null=True))
	stage = serializers.IntegerField(required=True)
	company = serializers.IntegerField(allow_null=True)


class SearchResultSerializer(serializers.ModelSerializer):
	account_email = serializers.SerializerMethodField()
	camera_name = serializers.SerializerMethodField()
	camera_token = serializers.SerializerMethodField()
	longitude = serializers.SerializerMethodField()
	latitude = serializers.SerializerMethodField()

	class Meta:
	    model = Searching_Detail
	    fields = ('timestamp', 'face_path', 'account_email', 'camera_name', 'camera_token', 'fullbody_path', 'video_path', 'timelapse', 'longitude', 'latitude')

	def get_account_email(self, SD):
		return SD.account.email if SD.account else "-"

	def get_camera_name(self, SD):
		return SD.camera.name if SD.camera else "-"

	def get_longitude(self, SD):
		return SD.camera.longitude if SD.camera else "-"

	def get_latitude(self, SD):
		return SD.camera.latitude if SD.camera else "-"

	def get_camera_token(self, SD):
		return SD.camera.token if SD.camera else "-"
