from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Car(models.Model):
  
  model = models.CharField(max_length=16,blank=False,null=False)
  brand = models.CharField(max_length=16,blank=False,null=False)
  price = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
  is_bought = models.BooleanField(default=False,blank=False,null=False)
  buyer_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,null=True)
  buy_time  = models.DateField(blank=True,null=True)
  
  
  def __str__(self):
    return f"{self.model}, {self.brand} - ${self.price}"
  
  
  def get_absolute_url(self):
    return reverse('car_details', args=[self.id])