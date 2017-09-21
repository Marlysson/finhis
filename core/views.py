#Django
from django.shortcuts import render
from django.contrib.auth.models import User

#Third Party
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.reverse import reverse

#App
from .mixins import ProfileDataRepeated, CategoryDataRepeated, RequestCategoryDataRepeated
from .models import RequestCategory
from .serializers import RequestCategorySerializer

class ProfileViewList(ProfileDataRepeated, generics.ListCreateAPIView):

	name = 'profile-list'

	def perform_create(self,serializer):
		
		user_data = {
			"username"  : request.data.get("username"),
			"first_name": request.data.get("first_name"),
			"last_name" : request.data.get("last_name"),
			"email"     : request.data.get("email"),
			"password"  : request.data.get("password"),
		}		

		profile_data = {
			"limit_spending_monthly": request.data.get("limit_spending_monthly")
		}

		user_serializer = UserSerializer(data=user_data)

		if user_serializer.is_valid():

			user = User.objects.create_user(**user_serializer.validated_data)
			
			serializer.save(
				limit_spending_monthly=request.data.get("limit_spending_monthly"),
				user=user
			)

			return Response(profile_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

		return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProfileViewDetail(ProfileDataRepeated,generics.RetrieveUpdateDestroyAPIView):
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