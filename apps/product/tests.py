from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

class ViewEmployeeTestCase(TestCase):
    def setUp(self):
        # """Define the test client and other test variables."""
        self.client = APIClient()
        self.team_data={'id':1,'designation':'python'}
        self.employee_data = {"id":1,"name": "vivek gupta", "team":1, "address":"gwalior","mobile": "8602848510", "email": "vivekram.techies123@gmail.com"}
        self.response = self.client.post(
            reverse('api_team_create'),
            self.team_data,
            format="json")
        self.response = self.client.post(
            reverse('api_employee_create'),
            self.employee_data,
            format="json")
    def test_01_api_can_create_a_employeelist(self):
    #     """Test the api has employee creation capability."""
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class ViewItemTestCase(TestCase):
    def setUp(self):
        # """Define the test client and other test variables."""
        self.client = APIClient()
        self.catagory_data={'id':1,'name':'electronics_gadgets'}
        self.item_data = {"id":1,"name": "pendrive", "model_no":"m1", "status":True, "catagory": 1}
        self.response = self.client.post(
            reverse('api_catagory_create'),
            self.catagory_data,
            format="json")
        self.response = self.client.post(
            reverse('api_item_create'),
            self.item_data,
            format="json")
    def test_02_api_can_create_a_itemlist(self):
    #     """Test the api has employee creation capability."""
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
