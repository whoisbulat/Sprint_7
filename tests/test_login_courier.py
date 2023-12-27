import allure
import pytest
import requests
from faker import Faker




fake = Faker()

class TestLoginCourier:
    @allure.title('Проверяем что упадет ошибка при попытки логина курьера без обязательных полей')
    @pytest.mark.parametrize("login, password", [
        ("", "password"),
        ("username", "")])
    def test_login_courier_without_required_fields(self, login, password):
        courier = {
            "login": login,
            "password": password
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=courier)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"


    @allure.title('Проверяем что упадет ошибка при попытки логина несуществующего курьера')
    def test_login_courier(self):
        courier = {
            "login": fake.user_name(),
            "password": fake.password()
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=courier)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"


    @allure.title('Проверяем логин курьера')
    def test_login_courier_(self):
        courier = {
            "login": "gomezamy",
            "password": "7%j2Vigvqf"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=courier)
        assert response.status_code == 200 and 'id' in response.json()