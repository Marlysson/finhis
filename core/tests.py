from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Category, Profile

class ApiTest(APITestCase):

	def setUp(self):
		self.category_url = "/categories/"
		self.profile_url = "/profiles/"

	def test_create_a_category(self):
		
		data = {
			"name":"Health",
			"icon":"https://feathericons.com/node_modules/feather-icons/dist/icons/activity.svg"
		}

		response = self.client.post(self.category_url,data,format='json')

		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		self.assertEqual(Category.objects.count(),1)

	def test_create_a_profile_and_create_a_user_together(self):

		profile_data  = {
			"user":{
				"username"  : "marcos",
				"first_name": "Marcos",
				"last_name" : "Silva",
				"email"     : "marcos@gmail.com",
				"password"  : "1234567890",
			},

			"limit_spending_monthly":6000
		}		

		response = self.client.post(self.profile_url,profile_data,format="json")
		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
