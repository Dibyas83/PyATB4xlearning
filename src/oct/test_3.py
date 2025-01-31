import pytest
import allure
import requests

@allure.title("Test get request")
@allure.description("This tests if GET Requst with id works.")
@allure.tag("reg","p0","smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Jim")
@allure.link("https://restful-booker.herokuapp.com/booking/1 ")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_get_singlereqby_id():
    url = "https://restful-booker.herokuapp.com/booking/1 "
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.request)
    assert responseData.status_code == 200

