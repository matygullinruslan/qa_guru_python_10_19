import requests
from jsonschema import validate
from schemas.schemas import post_users, list_users, update_users, error_register, successful_registr


def test_create_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/users'
    params = {"name": "morpheus", "job": "leader"}
    response = requests.post(url + endpoint, json=params)
    assert response.status_code == 201
    body = response.json()
    validate(body, post_users)


def test_update_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/users/2'
    params = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url + endpoint, json=params)
    assert response.status_code == 200
    body = response.json()
    validate(body, update_users)


def test_get_list_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/users'
    params = {"page": "2"}
    response = requests.get(url + endpoint, json=params)
    assert response.status_code == 200
    body = response.json()
    validate(body, list_users)


def test_delete_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/users/2'
    response = requests.delete(url + endpoint)
    assert response.status_code == 204
    assert response.text == ""


def test_get_user_not_found_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/unknown/23'
    response = requests.get(url + endpoint)
    assert response.status_code == 404
    assert response.json() == {}


def test_unsuccessful_registration_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/register'
    params = {"email": "sydney@fife"}
    response = requests.post(url + endpoint, json=params)
    assert response.status_code == 400
    body = response.json()
    validate(body, error_register)
    assert response.json() == {"error": "Missing password"}




def test_successful_registration_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/register'
    params = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(url + endpoint, json=params)
    assert response.status_code == 200
    body = response.json()
    validate(body, successful_registr)
    assert response.json() == {"id": 4, "token": "QpwL5tke4Pnpja7X4"}


# регистрация с неверным email
def test_invalid_email_registration_user_status_code():
    url = 'https://reqres.in'
    endpoint = '/api/register'
    params = {"email": "eve.holt.reqres.in", "password": "pistol"}
    response = requests.post(url + endpoint, json=params)
    assert response.status_code == 400
    assert response.json() == {"error": "Note: Only defined users succeed registration"}
