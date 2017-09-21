from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Category, Profile
import unittest

class ApiTest(APITestCase):

	def setUp(self):
		self.category_url = reverse("category-list")
		self.profile_url = reverse("profile-list")
		self.token_url = reverse("auth-token")

	@unittest.skip("pass")
	def test_should_be_obtain_token(self):

		user = User.objects.create_user(username="marlysson",email="marlysson5@gmail.com",password="hellodjango")
		token = Token.objects.get_or_create(user=user)

		data = {
			"username":user.username,
			"password":user.password
		}

		print(data)

		token_response = self.client.post(self.token_url,data,format="json")

		self.assertEqual(token_response.status_code,status.HTTP_201_CREATED)

	def test_create_a_category(self):
		
		data = {
			"name":"Health",
			"icon":"health-icon"
		}

		response = self.client.post(self.category_url,data,format='json')

		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		self.assertEqual(Category.objects.count(),1)

	@unittest.skip("pass")
	def test_create_a_profile_and_create_a_user_together(self):

		profile_data  = {
			"user":{
					"username"  : "maria",
					"first_name": "Marcos",
					"last_name" : "Silva",
					"email"     : "marcos@gmail.com",
					"password"  : "1234567890"
				},
			"limit_spending_monthly":6000
		}
			

		response = self.client.post(self.profile_url,profile_data,format="json")
		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
