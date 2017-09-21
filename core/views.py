#Django
from django.shortcuts import render
from django.contrib.auth.models import User

#Third Party
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.reverse import reverse

#App
from .mixins import CategoryDataRepeated, RequestCategoryDataRepeated
from .models import RequestCategory, Profile
from .serializers import UserSerializer, RequestCategorySerializer, ProfileSerializer

class ProfileViewList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-list'

	def perform_create(self, serializer):

		user_data = {
			"user":{
				"username"  : self.request.data.get("username"),
				"first_name": self.request.data.get("first_name"),
				"last_name" : self.request.data.get("last_name"),
				"email"     : self.request.data.get("email"),
				"password"  : self.request.data.get("password")
			}
		}		
		
		user = User.objects.create_user(**user_data)
		
		serializer.save(
			limit_spending_monthly=self.request.data.get("limit_spending_monthly"),
			user=user
		)


class ProfileViewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-detail'

class CategoryViewList(CategoryDataRepeated,generics.ListCreateAPIView):
	name = 'category-list'

class CategoryViewDetail(CategoryDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'category-detail'

class RequestCategoryViewList(RequestCategoryDataRepeated,generics.ListCreateAPIView):
	name = 'request-category-list'

class RequestCategoryViewDetail(RequestCategoryDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'request-category-detail'


class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self,request,*args,**kwargs):
    	
    	data_api = {
            'profiles': reverse(ProfileViewList.name,request=request),
            'categories': reverse(CategoryViewList.name,request=request),
            'requests': reverse(RequestCategoryViewList.name,request=request)
    	}

    	return Response(data_api)