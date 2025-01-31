import pytest
import allure
import requests


@allure.title("Test create booking request")
@allure.description("This tests if created id works.")
@pytest.mark.crud
def test_create_booking_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()
    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    @allure.title("Test blank payload")
    @allure.description("This tests if payload={} works.")
    @pytest.mark.crud
    def test_create_booking_positive():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url + base_path
        headers = {"Content-Type": "application/json"}
        json_payload = {}
        response = requests.post(url=URL, headers=headers, json=payload)
        print(type(URL))
        print(type(headers))
        print(type(json_payload))
        assert response.status_code == 500

    @allure.title("Test if totalprice as null works")
    @allure.description("This tests if totalprice neg or string works.")
    @pytest.mark.crud# bug raise
    def test_create_booking_negetive():
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_url + base_path
        headers = {"Content-Type": "application/json"}
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": -1,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = requests.post(url=URL, headers=headers, json=payload)
        assert response.status_code == 200





