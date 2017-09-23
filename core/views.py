from decimal import Decimal

#Django
from django.shortcuts import render
from django.contrib.auth.models import User

#Third Party
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser 

#App
from .mixins import CategoryDataRepeated, RequestCategoryDataRepeated, MovementDataRepeated,ProfileDataRepeated
from .models import RequestCategory, Profile, Movement
from .serializers import UserSerializer, RequestCategorySerializer, ProfileSerializer


class ProfileViewList(ProfileDataRepeated, generics.ListCreateAPIView):
	name = 'profile-list'

	def perform_create(self, serializer):

		data = self.request.data

		if "user.username" in data:
		
			user = {
				"username" : data.get("user.username"),
				"first_name": data.get("user.first_name"),
				"last_name": data.get("user.last_name"),
				"password": data.get("user.password"),
				"email": data.get("user.email")
			}

		else:			
			user = data.get("user")

		print(user)
		
		user = User.objects.create_user(**user)
		Token.objects.get_or_create(user=user)

		serializer.save(
			total_amount=0,
			limit_spending_monthly=self.request.data.get("limit_spending_monthly"),
			user=user
		)

class ProfileViewDetail(ProfileDataRepeated, generics.RetrieveUpdateDestroyAPIView):
	name = 'profile-detail'
	search_fields = ('name')

class CategoryViewList(CategoryDataRepeated,generics.ListCreateAPIView):
	name = 'category-list'
	ordering_fields = ('name')

class CategoryViewDetail(CategoryDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'category-detail'

class RequestCategoryViewList(RequestCategoryDataRepeated,generics.ListCreateAPIView):
	name = 'request-category-list'
	permission_classes = (IsAdminUser, IsAuthenticated,)

class RequestCategoryViewDetail(RequestCategoryDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'request-category-detail'
	permission_classes = (IsAdminUser, IsAuthenticated,)

class MovementViewList(MovementDataRepeated, generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)	
	name = 'movement-list'
	search_fields = ('description')

	def perform_create(self,serializer):
		
		import datetime

		if self.request.data.get("type_operation") == "IN":
			self.request.user.profile.total_amount += Decimal(self.request.data.get("amount"))
		else:
			self.request.user.profile.total_amount -= Decimal(self.request.data.get("amount"))

		self.request.user.profile.save()


		serializer.save(profile=self.request.user.profile,date=datetime.datetime.now())

	def get_queryset(self):
		return Movement.objects.filter(profile=self.request.user.profile)

class MovementViewDetail(MovementDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'movement-detail'

class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self,request,*args,**kwargs):
    	
    	data_api = {
            'profiles': reverse(ProfileViewList.name,request=request),
            'categories': reverse(CategoryViewList.name,request=request),
            'requests': reverse(RequestCategoryViewList.name,request=request),
            'movements': reverse(MovementViewList.name,request=request)
    	}

    	return Response(data_api)