import requests
from jsonschema import validate
from schemas import schema

url = 'https://reqres.in'


def test_create_user_status_code():
    endpoint = '/api/users'
    params = {"name": "morpheus", "job": "leader"}
    response = requests.post(url + endpoint, json=params)

    body = response.json()
    assert response.status_code == 201
    assert body["name"] == 'morpheus'

    validate(body, schema.post_users)


def test_update_user_status_code():
    endpoint = '/api/users/2'
    params = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url + endpoint, json=params)

    body = response.json()
    assert response.status_code == 200
    assert body["job"] == "zion resident"
    validate(body, schema.update_users)


def test_get_list_user_status_code():
    endpoint = '/api/users'
    params = {"page": "2"}
    response = requests.get(url + endpoint, json=params)

    assert response.status_code == 200
    body = response.json()
    validate(body, schema.list_users)


def test_delete_user_status_code():
    endpoint = '/api/users/2'
    response = requests.delete(url + endpoint)

    assert response.status_code == 204
    assert response.text == ""


def test_get_user_not_found_status_code():
    endpoint = '/api/unknown/23'
    response = requests.get(url + endpoint)
    assert response.status_code == 404
    assert response.json() == {}


def test_unsuccessful_registration_user_status_code():
    endpoint = '/api/register'
    params = {"email": "sydney@fife"}
    response = requests.post(url + endpoint, json=params)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"

    validate(body, schema.error_register)


def test_successful_registration_user_status_code():
    endpoint = '/api/register'
    params = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(url + endpoint, json=params)
    body = response.json()
    assert response.status_code == 200
    assert body["id"] == 4
    validate(body, schema.successful_registr)


# регистрация с неверным email
def test_invalid_email_registration_user_status_code():
    endpoint = '/api/register'
    params = {"email": "eve.holt.reqres.in", "password": "pistol"}
    response = requests.post(url + endpoint, json=params)
    assert response.status_code == 400
    assert response.json()["error"] == "Note: Only defined users succeed registration"
