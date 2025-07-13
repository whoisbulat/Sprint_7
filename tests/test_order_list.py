import requests
import allure




class TestOrderList:
    @allure.title('Проверка получения списка заказа')
    def test_order_list(self):

        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")

        assert response.status_code == 200 and 'id' in response.json()['orders'][0]
