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

	# def create(self,validated_data):

		# user = User(username=validated_data["username"],
		# 			first_name=validated_data["first_name"],
		# 			last_name=validated_data["last_name"],
		# 			email=validated_data["email"]
		# )

		# user.set_password(validated_data["password"])
		# user.save()

		# profile = Profile.objects.create(user=user,limit_spending_monthly=validated_data["limit_spending_monthly"])

		# return profile

	class Meta:
		model = Profile
		fields = ('user', 'limit_spending_monthly')

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('name', 'icon',)

class RequestCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = RequestCategory
		fields = ('name', 'profile', 'approved')