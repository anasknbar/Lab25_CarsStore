from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from cars.models import Car
from datetime import date
# command >>  python manage.py populate_cars
class Command(BaseCommand):
    help = 'Populate the database with car data'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        cars_data = [
            {"model": "Civic", "brand": "Honda", "price": 22000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Accord", "brand": "Honda", "price": 28000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Model 3", "brand": "Tesla", "price": 35000.00, "is_bought": True, "buyer_id": 1, "buy_time": date(2024, 5, 1)},
            {"model": "Mustang", "brand": "Ford", "price": 27000.00, "is_bought": True, "buyer_id": 2, "buy_time": date(2024, 6, 15)},
            {"model": "Camry", "brand": "Toyota", "price": 24000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Corolla", "brand": "Toyota", "price": 20000.00, "is_bought": True, "buyer_id": 3, "buy_time": date(2024, 4, 20)},
            {"model": "Impreza", "brand": "Subaru", "price": 23000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Outback", "brand": "Subaru", "price": 27000.00, "is_bought": True, "buyer_id": 4, "buy_time": date(2024, 2, 28)},
            {"model": "3 Series", "brand": "BMW", "price": 41000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "X5", "brand": "BMW", "price": 60000.00, "is_bought": True, "buyer_id": 5, "buy_time": date(2024, 1, 12)},
            {"model": "A4", "brand": "Audi", "price": 39000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Q7", "brand": "Audi", "price": 55000.00, "is_bought": True, "buyer_id": 6, "buy_time": date(2024, 3, 10)},
            {"model": "Altima", "brand": "Nissan", "price": 25000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Rogue", "brand": "Nissan", "price": 27000.00, "is_bought": True, "buyer_id": 7, "buy_time": date(2024, 6, 1)},
            {"model": "F-150", "brand": "Ford", "price": 30000.00, "is_bought": True, "buyer_id": 8, "buy_time": date(2024, 5, 15)},
            {"model": "Silverado", "brand": "Chevrolet", "price": 31000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Malibu", "brand": "Chevrolet", "price": 24000.00, "is_bought": True, "buyer_id": 9, "buy_time": date(2024, 4, 1)},
            {"model": "CX-5", "brand": "Mazda", "price": 26000.00, "is_bought": False, "buyer_id": None, "buy_time": None},
            {"model": "Mazda3", "brand": "Mazda", "price": 21000.00, "is_bought": True, "buyer_id": 10, "buy_time": date(2024, 3, 25)},
            {"model": "S60", "brand": "Volvo", "price": 42000.00, "is_bought": False, "buyer_id": None, "buy_time": None}
        ]

        for car_data in cars_data:
            car = Car(
                model=car_data["model"],
                brand=car_data["brand"],
                price=car_data["price"],
                is_bought=car_data["is_bought"],
                buyer_id=User.objects.get(id=car_data["buyer_id"]) if car_data["buyer_id"] else None,
                buy_time=car_data["buy_time"]
            )
            car.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated the car data'))
