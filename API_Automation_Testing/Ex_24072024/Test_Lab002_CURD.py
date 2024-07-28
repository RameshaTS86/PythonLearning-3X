# Full CURD Operations
import pytest
import requests
import allure

# TC_01 : Creat Booking
@allure.title('TC_01 : Create Booking')
@allure.tag("Functional Test Case")
@allure.description("Validating Booking Creation Functionality")
@allure.testcase("TC_01")
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url+base_path
    header = {"Content-Type": "application/json"}
    pay_load = {
        "firstname": "Ramesha",
        "lastname": "T S",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-12-31"
        },
        "additionalneeds": "super bowls"
    }
    response = requests.post(url=url,json=pay_load,headers=header)
    assert response.status_code == 200
    print(response.json())
    response_data = response.json()
    assert response_data["bookingid"] > 0
    assert response_data["bookingid"] is not None
    assert type(response_data["bookingid"]) == int
    return response_data["bookingid"]

@allure.title('TC_02 :Get Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating get Booking Details Functionality with BookingID")
@allure.testcase("TC_02")
def test_get_booking_details():
    booking_id = test_create_booking()
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(booking_id)
    url = base_url + base_path
    header = {"Content-Type": "application/json"}
    response = requests.get(url=url,headers=header)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "Ramesha"
    assert response_data["lastname"] == "T S"
    assert response_data["totalprice"] == 111
    assert response_data["depositpaid"] == True
    assert response_data["bookingdates"]["checkin"] == "2024-01-01"
    assert response_data["bookingdates"]["checkout"] == "2024-12-31"
    print(response_data)


@allure.title('TC_03 :Update Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Update Booking Details Functionality with BookingID")
@allure.testcase("TC_03")
def test_put_request_update_record():
    def create_token():
        url = "https://restful-booker.herokuapp.com/auth"
        header = {"Content-Type": "application/json"}
        pay_load= {
            "username": "admin",
            "password": "password123"
        }
        response=requests.post(url=url,headers=header,json=pay_load)
        assert response.status_code == 200
        response_data = response.json()
        return response_data["token"]

    #Updating the Record (put Request)
    token = create_token()
    cookie = "token="+token
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking())
    url = base_url + base_path
    header = {"Content-Type": "application/json",
               "Cookie": cookie}
    pay_load = {
        "firstname": "Ramesha",
        "lastname": "Toremavinahalli Siddesh",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-06-30"
        },
        "additionalneeds": "2 water bottle "
    }
    response = requests.put(url=url,headers=header,json=pay_load)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "Ramesha"
    assert response_data["lastname"] == "Toremavinahalli Siddesh"
    assert response_data["totalprice"] == 500
    assert response_data["depositpaid"] == True
    assert response_data["bookingdates"]["checkin"] == "2024-01-01"
    assert response_data["bookingdates"]["checkout"] == "2024-06-30"
    print(response_data)


@allure.title('TC_04 :Delete Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Delete Booking Details Functionality with BookingID")
@allure.testcase("TC_04")
def test_delete_booking_details():
    def create_token():
        url = "https://restful-booker.herokuapp.com/auth"
        header = {"Content-Type": "application/json"}
        pay_load= {
            "username": "admin",
            "password": "password123"
        }
        response=requests.post(url=url,headers=header,json=pay_load)
        assert response.status_code == 200
        response_data = response.json()
        return response_data["token"]

    #Updating the Record (put Request)
    token = create_token()
    cookie = "token="+token
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking())
    url = base_url + base_path
    header = {"Content-Type": "application/json",
               "Cookie": cookie}
    pay_load = {
        "firstname": "Ramesh",
        "lastname": "Toremavinahalli Siddesh",
    }
    response = requests.delete(url=url,headers=header,json=pay_load)
    assert response.status_code == 201


@allure.title('TC_04 :Partial Update Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Partial Booking Update Functionality with BookingID")
@allure.testcase("TC_05")
def test_patch_request_partial_update_record():
    def create_token():
        url = "https://restful-booker.herokuapp.com/auth"
        header = {"Content-Type": "application/json"}
        pay_load= {
            "username": "admin",
            "password": "password123"
        }
        response=requests.post(url=url,headers=header,json=pay_load)
        assert response.status_code == 200
        response_data = response.json()
        return response_data["token"]

    #Updating the Record (put Request)
    token = create_token()
    cookie = "token="+token
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking())
    url = base_url + base_path
    header = {"Content-Type": "application/json",
               "Cookie": cookie}
    pay_load = {
        "firstname": "Ramesha",
        "lastname": "Toremavinahalli Siddesh",
        "totalprice": 1000,
    }
    response = requests.patch(url=url,headers=header,json=pay_load)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "Ramesha"
    assert response_data["lastname"] == "Toremavinahalli Siddesh"
    assert response_data["totalprice"] == 1000
    print(response_data)

