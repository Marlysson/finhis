from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Category, RequestCategory

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email','password')
		extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):

	user = UserSerializer()

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