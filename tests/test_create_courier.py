import allure
import pytest
import requests
from faker import Faker




fake = Faker()

class TestCreateCourier:
    @allure.title('Проверяем создание курьера с обязательными полями')
    def test_success_create_new_courier(self):
        new_courier = {
            "login": fake.user_name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=new_courier)
        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title('Проверяем что упадет ошибка при попытки создания курьера который уже есть в системе')
    def test_check_create_identical_couriers(self):

        courier = {
            "login": "gomezamy",
            "password": "7%j2Vigvqf",
            "firstName": "Christina"
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=courier)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."


    @allure.title('Проверяем что упадет ошибка при попытки создания курьера без обязательных полей')
    @pytest.mark.parametrize("login, password", [
    ("", "password123"),
    ("username", "")])
    def test_create_courier_without_required_fields(self, login, password):

        courier = {
            "login": login,
            "password": password
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=courier)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"