from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Category, RequestCategory, Movement

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email','password')
		extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):

	user = UserSerializer()

	def create(self,validated_data):
		print(validated_data.pop("user"))

		return None
	class Meta:
		model = Profile
		fields = ('user', 'limit_spending_monthly')

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('name', 'icon')

class RequestCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = RequestCategory
		fields = ('name', 'profile', 'approved')

class MovementSerializer(serializers.ModelSerializer):

	type_operation = serializers.SerializerMethodField()

	class Meta:
		model = Movement
		fields = ('description','amount','profile','category','date','type_operation')

	def get_type_operation(self,obj):
		return self.type_operation.get_type_operation_display()
