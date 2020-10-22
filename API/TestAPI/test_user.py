from fastapi.testclient import TestClient
import json

import pytest

from main import app

client = TestClient(app)

""" Necesito compartir usuarios para las pruebas.
"""
@pytest.fixture
def users():
    return [
    {
        "email": "superman@justiceleague.com",
        "username": "Clark Kent",
        "password": "kkkkk12323",
    },
    {
        "email": "batman@justiceleague.com",
        "username": "Bruno Diaz",
        "password": "kadssdkkkk",
    },
    {
        "email": "robin@justiceleague.com",
        "username": "RicardoTapia",
        "password": "987979oo68i7",
    },
    {
        "email": "wonderwoman@justiceleague.com",
        "username": "DianaPrince",        
        "password": "421413434234",
    },
    {
        "email": "thor@gmail.com",
        "username": "nothor22",
        "password": "kkkasdskk"
    },
    {
        "email": "thejoker@gmail.com",
        "username": "thejoker",
        "password": "kkkasdskk"
    },

]

""" Guardamos lo que nos haga falta para interactuar autenticados en un diccionario.
    El diccionario tendría la "forma": "user_email" : (status_code_login, json_token)
"""
USERS_AUTH_DICT = {}

"""
Endpoint test: "/user/register/"

Descripción:
Tiene que funcionar la primera vez que lo ejecutan. Si lo ejecutan una segunda vez no funciona, 
ya que el recurso ha sido creado.
Escenario exitoso: 201
Error: 409

"""
def test_register_users(users):
    for user in users:
        user_register = { "email": user["email"], "username": user["username"], "password": user["password"] }
        response = client.post(
            "/user/register/",
            headers = { "accept": "application/json" },
            json    = user_register
        )
        
        assert response.status_code == 201, "User %s created"%(user_register["email"])

"""
Endpoint test: "/user/{email}"

Descripción:
Una vez registrados nuestros usuarios, testeamos si son accesibles por un query.
Escenario exitoso: 200
Error: 404

"""
def test_get_users(users):
    for user in users:
        user_data = { "email": user["email"], "username": user["username"] }
        response = client.get(
            "/user/" + user_data["email"]
        )

        assert response.status_code == 200, "User Ok:\n%s\n"%(response.content.decode())


"""
Endpoint test: "/user/login/"

Descripción:
Queremos ver que nos devuelva la información acordada respecto a la autenticación.
Escenario exitoso: 302
Error: 401

"""
def test_login_users(users):
    for user in users:
        user_data = { "username": user["email"], "password": user["password"] }
        response = client.post(
            "/user/login/",
            headers = { "Content-Type": "application/x-www-form-urlencoded" },
            data = user_data
        )

        assert response.status_code == 302, "Unauthorized: %s\n"%(user_data["username"])

        USERS_AUTH_DICT.update({ user_data["username"]: ( response.status_code, dict(response.headers)["set-cookie"] ) })
    
    for key in list(USERS_AUTH_DICT.keys()):
        if USERS_AUTH_DICT[key][0] == 302:
            print("Login: %s %s"%(key, USERS_AUTH_DICT[key][1]))
