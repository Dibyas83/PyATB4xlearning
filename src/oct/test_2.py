import pytest
import allure


@allure.title("Test Authentication")
@allure.description("This is a smoke test .")
@pytest.mark.smoke
def test_verify():
    assert (1 + 1) == 2


@allure.title("Test Authentication if 1*7 = 7")
@allure.description("This is a smoke test .")
@pytest.mark.smoke
def test_verify2():
    assert (1 * 7) == 7


@allure.title("Test Authentication multiply")
@allure.description("This is a smoke test .")
@pytest.mark.smoke
def test_verify3():
    assert (3 * 7) == 7


@allure.title("Test Authentication ")
@allure.description("This is a smoke test .")
@pytest.mark.reg
def test_verify4():
    assert (1 * 7) == 7


@allure.title("Test Authentication")
@allure.description("This is a smoke test .")
@pytest.mark.skip(reason="unfinished")
def test_verify5():
    assert (2 * 7) == 13