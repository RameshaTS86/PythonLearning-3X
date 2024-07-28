# this is the file which will be running first when we run pytest
#can be used to create common IDs, tokens etc and can be utilise in the other test files

import pytest
import requests



#Token Creations
@pytest.fixture()
def create_token_id():
    url = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    pay_load = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=header, json=pay_load)
    assert response.status_code == 200
    response_data = response.json()
    return response_data["token"]


#BookingID Creation
@pytest.fixture()
def test_create_booking_id():
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
    response_data = response.json()
    assert response_data["bookingid"] > 0
    assert response_data["bookingid"] is not None
    assert type(response_data["bookingid"]) == int
    print("Create Booking ID : ",response_data["bookingid"])
    return response_data["bookingid"]