from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile, Category, RequestCategory

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'password')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

	user = UserSerializer()

	class Meta:
		model = Profile
		fields = ('user', 'limit_spending_monthly')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Category
		fields = ('url','name', 'icon',)

class RequestCategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = RequestCategory
		fields = ('name', 'profile', 'approved')