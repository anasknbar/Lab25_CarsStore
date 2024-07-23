from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime
from .models import Car

class PetsTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars/cars.html')
        self.assertTemplateUsed(response, 'cars/base.html')

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username= 'test_user',
            email="test@email.com",
            password="1234"
        )

        self.car = Car.objects.create(
            model='test_model',
            brand='test_brand',
            price=10000.0,  # Ensure this is a float
            is_bought=True,
            buyer_id=self.user,  # Assign the user instance
            buy_time=datetime(2020, 3, 7)  # Use datetime for date fields
        )

def test_str_method(self):
    expected_str = f"{self.car.model}, {self.car.brand} - ${self.car.price}"
    self.assertEqual(str(self.car), expected_str)


    
    def test_details_view(self):
        url = reverse('car_details', args=[self.car.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'cars/car_details.html')

    def test_create_view(self):

        obj= {
            "model": "test_model",
            "brand":"test_brand",
            "price":10000.0,
            "is_bought":True,
            "buyer_id":self.user.id,
            "buy_time": "2020-03-07",
            
        }
        
        
        url = reverse('car_create')
        response = self.client.post(path = url, data= obj, follow= True)
        # self.assertEqual(len(Pet.objects.all()), 2)
        self.assertRedirects(response, reverse('car_details', args=[2]))