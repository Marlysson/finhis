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

	class Meta:
		model = Profile
		fields = ('user', 'total_amount', 'limit_spending_monthly')
		extra_kwargs = {
			"total_amount":{"read_only":True}
		}

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Category
		fields = ('url','name')

class RequestCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = RequestCategory
		fields = ('name', 'profile', 'approved')

class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profile
		fields = ('url',)

class MovementSerializer(serializers.HyperlinkedModelSerializer):

	operation = serializers.SerializerMethodField()
	profile = ProfileDetailSerializer(read_only=True)
	category = CategorySerializer()

	def get_operation(self,obj):
		return obj.get_type_operation_display()

	class Meta:
		model = Movement
		fields = ('url', 'description','amount','profile','category','date','operation',"type_operation")

		extra_kwargs = {
			"date": {"read_only":True},
			"type_operation":{"write_only":True}
			}
