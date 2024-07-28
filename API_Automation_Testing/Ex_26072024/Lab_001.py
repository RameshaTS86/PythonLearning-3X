#Fixtures
import pytest
import requests
import allure


@allure.title('TC_01 :Get Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating get Booking Details Functionality with BookingID")
@allure.testcase("TC_01")
def test_get_booking_details(test_create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking_id)
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
    print("Get BookingID : ",test_create_booking_id,response_data)



@allure.title('TC_02 :Update Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Update Booking Details Functionality with BookingID")
@allure.testcase("TC_02")
def test_put_request_update_record(test_create_booking_id,create_token_id):
    cookie = "token="+create_token_id
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking_id)
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
    print("Update BookingID : ",test_create_booking_id,response_data)


@allure.title('TC_03 :Partial Update Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Partial Booking Update Functionality with BookingID")
@allure.testcase("TC_03")
def test_patch_request_partial_update_record(test_create_booking_id,create_token_id):
    cookie = "token="+create_token_id
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking_id)
    url = base_url + base_path
    header = {"Content-Type": "application/json",
               "Cookie": cookie}
    pay_load = {
        "firstname": "Ramesha_patch",
        "lastname": "Toremavinahalli Siddesh",
        "totalprice": 1000,
    }
    response = requests.patch(url=url,headers=header,json=pay_load)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["firstname"] == "Ramesha_patch"
    assert response_data["lastname"] == "Toremavinahalli Siddesh"
    assert response_data["totalprice"] == 1000
    print("Partial Update BookingID : ",test_create_booking_id,response_data)

@allure.title('TC_04 :Delete Booking Details')
@allure.tag("Functional Test Case")
@allure.description("Validating Delete Booking Details Functionality with BookingID")
@allure.testcase("TC_04")
def test_delete_booking_details(test_create_booking_id,create_token_id):
    cookie = "token="+create_token_id
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(test_create_booking_id)
    url = base_url + base_path
    header = {"Content-Type": "application/json",
               "Cookie": cookie}
    pay_load = {
        "firstname": "Ramesh",
        "lastname": "Toremavinahalli Siddesh",
    }
    response = requests.delete(url=url,headers=header,json=pay_load)
    assert response.status_code == 201
    print("Deleted BookingID : ", test_create_booking_id)


