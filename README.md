# MediaBridgeX

Social Media App using FastAPI

## How to run locally:

To run this project locally follow the following steps :

### Setting up the environment: 

```
git clone https://github.com/Arnav-2004/MediaBridgeX.git
cd MediaBridgeX
python -m venv venv  (optional)
.\venv\Scripts\activate.bat  (Refer: https://docs.python.org/3/library/venv.html#how-venvs-work)
pip install -r requirements.txt
```

### Setting up the environment variables :

Create a .env file in the root folder that is `MediaBridgeX` and populate the following fields :

```
DATABASE_USERNAME=
DATABASE_PASSWORD=
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_NAME=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

To generate a `SECRET_KEY` you can run `openssl rand -hex 32` or `ssh-keygen -t rsa -b 4096 -m PEM -f private.key`

**NOTE :** Must have [mysql community server](https://dev.mysql.com/downloads/mysql/) installed.

### Running the api :
```
uvicorn app.main:app
```

The server will be running at http://127.0.0.1:8000/

To access the documentation go to http://127.0.0.1:8000/docs

## Routes:

1. Post route

- `GET` /posts/  - Fetch all the posts.
- `GET` /posts/{id}  - Fetch a single post by id.
- `POST` /posts/  - Create a post. (Must be authorized)
- `PUT` /posts/{id}  - Update a post by id. (Must be authorized and author of the post)
- `DELETE` /posts/{id}  - Delete a post by id. (Must be authorized and author of the post)

2. Users route

- `POST` /users/  - Regesiter an user.
- `GET` /users/{id}  - Fetch a user by id.

3. Auth route

- `POST` /login  - Login an user. (Generates JSON Web Token)

4. Likes route

- `POST` /like/  - Like and dislike a liked post.
