from django.urls import path
from .views import IndexView,CarsView,CarDetailsView,CarCreateView,CarUpdateView,CarDeleteView

urlpatterns = [
  path('',IndexView.as_view(),name='index'),
  path('cars/',CarsView.as_view(),name='cars'),
  path('car_details/<int:pk>/',CarDetailsView.as_view(),name='car_details'),
  path('create/',CarCreateView.as_view(),name='car_create'),
  path('update/<int:pk>',CarUpdateView.as_view(),name='car_update'),
  path('<int:pk>/delete',CarDeleteView.as_view(),name='car_delete')
]