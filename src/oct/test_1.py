import pytest
import allure


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_verify():
    assert (1 + 1) == 2


@pytest.mark.smoke
def test_verify2():
    assert (1 * 7) == 7


@pytest.mark.smoke
def test_verify3():
    assert (3 * 7) == 7


@pytest.mark.reg
def test_verify4():
    assert (1 * 7) == 7


@pytest.mark.skip(reason="unfinished")
def test_verify5():
    assert (2 * 7) == 13

