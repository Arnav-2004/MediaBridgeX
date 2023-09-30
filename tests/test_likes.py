import pytest

from app import models


@pytest.fixture
def test_likes(session, test_user, test_posts):
    new_like = models.Like(post_id=test_posts[0].id, user_id=test_user["id"])
    session.add(new_like)
    session.commit()


def test_like(authorized_client, test_posts):
    res = authorized_client.post("/like/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 201


def test_like_twice(authorized_client, test_posts, test_likes):
    res = authorized_client.post("/like/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 409


def test_like_id_not_found(authorized_client):
    res = authorized_client.post("/like/", json={"post_id": 1000000, "dir": 1})
    assert res.status_code == 404


def test_like_unauthorized(client, test_posts):
    res = client.post("/like/", json={"post_id": test_posts[0].id, "dir": 1})
    assert res.status_code == 401


def test_dislike(authorized_client, test_posts, test_likes):
    res = authorized_client.post("/like/", json={"post_id": test_posts[0].id, "dir": 0})
    assert res.status_code == 201


def test_dislike_not_found(authorized_client, test_posts):
    res = authorized_client.post("/like/", json={"post_id": test_posts[0].id, "dir": 0})
    assert res.status_code == 404
