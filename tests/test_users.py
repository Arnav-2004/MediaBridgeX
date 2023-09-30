import pytest
from jose import jwt
from app import schemas
from app.config import settings


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "testmail@gmail.com", "password": "test123"}
    )
    new_user = schemas.User(**res.json())
    assert res.status_code == 201
    assert new_user.email == "testmail@gmail.com"


def test_login_user(client, test_user):
    res = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert res.status_code == 200
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("invalidmail@gmail.com", "password123", 403),
        ("arnav@gmail.com", "invalidpassword123", 403),
        ("invalidmail@gmail.com", "invalidpassword123", 403),
        ("arnav@gmail.com", None, 422),
        (None, "password123", 422),
    ],
)
def test_invalid_login(client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
