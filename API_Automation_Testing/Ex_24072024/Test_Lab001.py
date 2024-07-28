import pytest #pip install pytest
import requests #pip install requests
import allure #pip install allure-pytest

#Testcase to get booking details using bookingid

@allure.title("TestCase_01 :GET: Booking Details ")
@allure.description("Test Case to Get Booking Details.!")
@allure.tag("New Test Case")
@allure.label("Owner","Ramesh")
@allure.testcase("TC_01")
def test_get_booking_data_using_booking_id():
    url="https://restful-booker.herokuapp.com/booking/428"
    response= requests.get(url)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200


@allure.title("TestCase_02: Negative :GET: Booking Details ")
@allure.description("Test Case to Get Booking Details Negative.!")
@allure.tag("New Test Case")
@allure.label("Owner","Ramesh")
@allure.testcase("TC_02")
def test_get_booking_data_using_booking_id_negative():
    url="https://restful-booker.herokuapp.com/booking/invalid"
    response= requests.get(url)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 404


@allure.title("TestCase_03: Negative 2:GET: Booking Details ")
@allure.description("Test Case to Get Booking Details Negative.!")
@allure.tag("New Test Case")
@allure.label("Owner","Ramesh")
@allure.testcase("TC_03")
def test_get_booking_data_using_booking_id_negative2():
    url="https://restful-booker.herokuapp.com/booking/123456"
    response= requests.get(url)
    response_data = response.json()
    print(response_data)
    assert response.status_code != 404

