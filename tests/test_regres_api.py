import requests
from jsonschema import validate

from schemas.schemas import post_users, list_users, update_users, error_register, successful_registr


# SCHEMA_INIT = os.path.abspath(schemas.__file__)
# SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)

# На каждый из методов GET/POST/PUT/DELETE ручек reqres.in


def test_create_user_status_code():
    response = requests.post('https://reqres.in/api/users', json={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201
    body = response.json()
    validate(body, post_users)


def test_update_user_status_code():
    response = requests.put('https://reqres.in/api/users/2', json={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
    body = response.json()
    validate(body, update_users)


def test_get_list_user_status_code():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert response.status_code == 200
    body = response.json()
    validate(body, list_users)


def test_delete_user_status_code():
    response = requests.delete('https://reqres.in/api/users?page=2')
    assert response.status_code == 204
    assert response.text == ""


def test_get_user_not_found_status_code():
    response = requests.get('https://reqres.in/api/users/23')
    assert response.status_code == 404
    assert response.json() == {}


def test_unsuccessful_registration_user_status_code():
    response = requests.post('https://reqres.in/api/register', json={"email": "sydney@fife"})
    assert response.status_code == 400
    body = response.json()
    validate(body, error_register)


def test_successful_registration_user_status_code():
    response = requests.post('https://reqres.in/api/register',
                             json={"email": "eve.holt@reqres.in", "password": "pistol"})
    assert response.status_code == 200
    body = response.json()
    validate(body, successful_registr)


def test_successful_registration_user_status_code():
    response = requests.post('https://reqres.in/api/register',
                             json={"email": "eve.holt///reqres.in", "password": "pistol"})
    assert response.status_code == 400
    body = response.json() == {
    "error": "Note: Only defined users succeed registration"
}

