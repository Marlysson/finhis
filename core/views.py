#Django
from django.shortcuts import render
from django.contrib.auth.models import User

#Third Party
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

#App
from .mixins import CategoryDataRepeated, RequestCategoryDataRepeated
from .models import RequestCategory, Profile
from .serializers import UserSerializer, RequestCategorySerializer, ProfileSerializer

class ProfileViewList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-list'

	def perform_create(self, serializer):
		
		user = User.objects.create_user(**self.request.data.get("user"))
		Token.objects.get_or_create(user=user)

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
	permission_classes = (IsAuthenticated,)

class RequestCategoryViewDetail(RequestCategoryDataRepeated,generics.RetrieveUpdateDestroyAPIView):
	name = 'request-category-detail'
	permission_classes = (IsAuthenticated,)

class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self,request,*args,**kwargs):
    	
    	data_api = {
            'profiles': reverse(ProfileViewList.name,request=request),
            'categories': reverse(CategoryViewList.name,request=request),
            'requests': reverse(RequestCategoryViewList.name,request=request)
    	}

    	return Response(data_api)