"""
we need
put request
 url
 path to bookingid
 token
 payload
 header
"""


import pytest
import allure
import requests
# create  token ,no test case first


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"

    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token

# create booking
def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {

        "firstname": "Tom",
        "lastname": "crown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {

            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    print(type(url))
    print(type(headers))
    print(type(payload))

    assert  response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_request_pos():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    put_URL = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload = {
        "firstname": "Pom",
        "lastname": "crown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=put_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Pom"

def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)









