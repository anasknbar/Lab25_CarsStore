from django.contrib import admin
from .models import Car

# Register your models here.

class AdminCar(admin.ModelAdmin):
  list_display = ['model','brand','price','is_bought','buyer_id','buy_time']
  
  
admin.site.register(Car,AdminCar)

