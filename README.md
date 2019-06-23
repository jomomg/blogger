# Blogger

A simple blogging application built with Python and Flask.

#### Technologies
- Python (3.4+)
- Flask
- PostgreSQL

#### Features

  - Users can create and edit blog posts
  - Users can leave comments on blog posts
  - Users can reply to other comments
  - Users can follow other users they are interested in* (upcoming)

#### Installation

- Clone this repository
- Set up a virtual environment ```python3 -m venv env```
- Install requirements with ```pip install -r requirements```
- Run server with ```flask run```

### Endpoints

The following endpoints are available

| Endpoint | Description |
| ------ | ------ |
| ```POST /auth/register``` | Register a user |
| ```POST /auth/login``` | Login a user |
| ```POST /api/posts``` | Create a blog post |
| ```GET /api/posts``` | Get all blog posts |
| ```GET /api/posts/<post_id>``` | Get a specific blog post |
| ```PATCH /api/posts/<post_id>``` | Edit a blog post |
| ```POST /api/comments``` | Create a comment |
| ```GET /api/comments``` | Get all comments |
| ```GET /api/comments/<comment_id>``` | Get a specific comment |
| ```PATCH /api/comments/<comment_id>``` | Edit a comment |
