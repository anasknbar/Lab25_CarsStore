from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DeleteView,DetailView,CreateView,UpdateView
from .models import Car
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
  template_name = 'cars/index.html'
  

class CarsView(ListView):
  model = Car
  template_name = 'cars/cars.html'
  context_object_name = 'cars'
  
class CarDetailsView(DetailView):
  model = Car
  template_name = 'cars/car_details.html'
  context_object_name = 'car'
  
class CarCreateView(CreateView):
  model = Car
  template_name = 'cars/car_create.html'
  fields = ['model','brand','price','is_bought','buyer_id','buy_time']
  context_object_name = 'car'
  
class CarUpdateView(UpdateView):
  model = Car
  template_name = 'cars/car_update.html'
  fields = ['model','brand','price','is_bought','buyer_id','buy_time']
  context_object_name = 'updated_car'
  
  
class CarDeleteView(DeleteView):
    model=Car
    template_name='cars/car_delete.html'
    success_url = reverse_lazy('cars')




# def CarDeleteView(request,pk):
#   car_to_delete = get_object_or_404(Car,pk=pk)
#   car_to_delete.delete()
#   return redirect('cars')
  

  
  

