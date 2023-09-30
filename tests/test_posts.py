import pytest

from app import schemas


def test_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    posts = list(map(lambda post: schemas.PostLike(**post), res.json()))
    assert res.status_code == 200
    assert len(posts) == len(test_posts)
    for i in range(len(test_posts)):
        assert posts[i].Post.id == test_posts[i].id
        assert posts[i].Post.owner_id == test_posts[i].owner_id


def test_get_one_post(client, test_posts):
    for i in range(len(test_posts)):
        res = client.get(f"/posts/{test_posts[i].id}")
        post = schemas.PostLike(**res.json())
        assert post.Post.id == test_posts[i].id
        assert post.Post.title == test_posts[i].title
        assert post.Post.content == test_posts[i].content
        assert post.Post.owner_id == test_posts[i].owner_id


def test_get_one_post_id_not_found(client):
    res = client.get("/posts/1000000")
    assert res.status_code == 404


@pytest.mark.parametrize(
    "title, content, published",
    [
        ("first test title", "first test content", True),
        ("second test title", "second test content", False),
    ],
)
def test_create_posts(authorized_client, test_user, title, content, published):
    res = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published}
    )
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]


def test_create_posts_default_published(authorized_client, test_user):
    res = authorized_client.post(
        "/posts/", json={"title": "test title", "content": "test content"}
    )
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "test title"
    assert created_post.content == "test content"
    assert created_post.published == True
    assert created_post.owner_id == test_user["id"]


def test_create_posts_unauthorized(client):
    res = client.post(
        "/posts/", json={"title": "test title", "content": "test content"}
    )
    assert res.status_code == 401


def test_delete_posts(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_delete_posts_id_not_found(authorized_client):
    res = authorized_client.delete("/posts/1000000")
    assert res.status_code == 404


def test_delete_posts_different_owner(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[2].id}")
    assert res.status_code == 403


def test_delete_posts_unauthorized(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_update_posts(authorized_client, test_posts):
    res = authorized_client.put(
        f"/posts/{test_posts[0].id}",
        json={"title": "updated title", "content": "updated content"},
    )
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == "updated title"
    assert updated_post.content == "updated content"


def test_update_posts_id_not_found(authorized_client):
    res = authorized_client.put(
        "/posts/1000000", json={"title": "updated title", "content": "updated content"}
    )
    assert res.status_code == 404


def test_update_posts_different_owner(authorized_client, test_posts):
    res = authorized_client.put(
        f"/posts/{test_posts[2].id}",
        json={"title": "updated title", "content": "updated content"},
    )
    assert res.status_code == 403


def test_update_posts_unauthorized(client, test_posts):
    res = client.put(
        f"/posts/{test_posts[0].id}",
        json={"title": "updated title", "content": "updated content"},
    )
    assert res.status_code == 401
