from request import Api_Request
from Phone_model import Phone_Model
from Inn_model import Inn_Model


#response validation by pydantic
def test_valid_number():

    number = "[89218494940]"
    request = Api_Request().phone_request(number)
    response = Phone_Model(**request)

    assert response.type == "Мобильный"
    assert response.country == "Россия"


#response validation by pydantic
def test_invalid_number():

    number = "[123]"
    request = Api_Request().phone_request(number)
    response = Phone_Model(**request)

    assert response.phone == None
    assert response.country == None


#request validation by pydantic
def test_valid_inn():

    body = Inn_Model(query=7707083893, kpp=773601001)

    request = Api_Request().inn_request(body.json())

    #failed test


#request validation by pydantic
def test_failed_validation_request():
    body = Inn_Model()

    request = Api_Request().inn_request(body.json())

    assert request is not None


#request validation by pydantic
def test_with_optional_parameter_request():
    body = Inn_Model(query=7707083893)

    request = Api_Request().inn_request(body.json())

    assert request is not None




