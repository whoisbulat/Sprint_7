import allure
import pytest
import requests
import random
import datetime
from faker import Faker




fake = Faker()

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize("color", [("BLACK",), ("GREY",), ("BLACK", "GREY"), ("",)])
    def test_create_order_with_(self, color):
        order_data = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randint(0, 100),
            "phone": fake.phone_number(),
            "rentTime": random.randint(0, 100),
            "deliveryDate": (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d"),
            "comment": fake.text(),
            "colors": list(color)
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", json=order_data)

        assert response.status_code == 201 and 'track' in response.json()









