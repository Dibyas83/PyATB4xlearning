import pytest
# fixture = reusable functions

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1
@pytest.fixture()
def read_excel_file():
    return "xyz"
@pytest.fixture()
def read_json():
    return "{}"

def test_consume(create_token,create_booking_id,read_excel_file,read_json):
    print(create_token)
    print(create_booking_id)
    print(read_json)
    print(read_excel_file)















