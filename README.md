# Late Show API

A Flask REST API for managing a Late Night TV show system, built with:

- MVC architecture
- PostgreSQL (no SQLite!)
- JWT-based authentication
- Flask-Restful for clean resource routing
- Flask-Migrate for migrations
- Postman for API testing

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Environment Variables](#environment-variables)
  - [PostgreSQL Setup](#postgresql-setup)
  - [Install Dependencies](#install-dependencies)
  - [Database Migrations & Seeding](#database-migrations--seeding)
  - [Running the Server](#running-the-server)
- [Authentication Flow](#authentication-flow)
- [API Routes](#api-routes)
- [Testing with Postman](#testing-with-postman)
- [Sample Requests & Responses](#sample-requests--responses)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User Registration & Login with JWT authentication
- CRUD for Episodes, Guests, Appearances
- Cascade delete: Deleting an episode removes its appearances
- Validation: Ratings must be 1–5, usernames unique, etc.
- Protected endpoints: Only authenticated users can create appearances or delete episodes
- Postman collection for easy API testing

---

## Project Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
│   └── migrations/
├── challenge-4-lateshow.postman_collection.json
├── Pipfile
├── README.md
```

---

## Setup Instructions

### 1. Environment Variables

Create a `.env` file in your project root with:

```
DATABASE_URI=postgresql://<user>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=super-secret-key
```

Or set these in your shell before running the app.

### 2. PostgreSQL Setup

Create the database:

```bash
psql -U <user> -h 127.0.0.1 -p 5432
CREATE DATABASE late_show_db;
```

### 3. Install Dependencies

```bash
pipenv install
pipenv shell
```

If you need to install dependencies manually:

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv flask-restful
```

### 4. Database Migrations & Seeding

From the project root:

```bash
export FLASK_APP=server/app.py
flask db init           # Only once, if migrations/ doesn't exist
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py   # Seed the database with sample data
```

### 5. Running the Server

```bash
python server/app.py
# or
flask run
```

The API will be available at `http://localhost:5555/`

---

## Authentication Flow

- Register: `POST /register` with username & password
- Login: `POST /login` to receive a JWT token
- Protected routes: Send `Authorization: Bearer <token>` in headers

---

## API Routes

| Route                       | Method | Auth Required? | Description                                 |
|-----------------------------|--------|----------------|---------------------------------------------|
| `/register`                 | POST   | No             | Register a new user                         |
| `/login`                    | POST   | No             | Log in and receive JWT token                |
| `/episodes`                 | GET    | No             | List all episodes                           |
| `/episodes/<int:id>`        | GET    | No             | Get episode by ID (with appearances)        |
| `/episodes/<int:id>`        | DELETE | Yes            | Delete episode (cascade delete appearances) |
| `/guests`                   | GET    | No             | List all guests                             |
| `/appearances`              | POST   | Yes            | Create a new appearance                     |

---

## Testing with Postman

1. Import `challenge-4-lateshow.postman_collection.json` into Postman.
2. Register a user (`/register`).
3. Log in (`/login`) and copy the `access_token`.
4. For protected routes, add a header:
   ```
   Authorization: Bearer <access_token>
   ```
5. Test all endpoints, including error cases (e.g., invalid rating, missing token).

---

## Sample Requests & Responses

### Register

**POST** `/register`
```json
{
  "username": "mati",
  "password": "secret"
}
```
**Response:**
```json
{ "message": "User registered" }
```

### Login

**POST** `/login`
```json
{
  "username": "mati",
  "password": "secret"
}
```
**Response:**
```json
{ "access_token": "<JWT_TOKEN>" }
```

### Create Appearance (Protected)

**POST** `/appearances`
Headers: `Authorization: Bearer <JWT_TOKEN>`
```json
{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 5
}
```
**Response:**
```json
{
  "id": 1,
  "guest_id": 1,
  "episode_id": 2,
  "rating": 5
}
```

### Delete Episode (Protected)

**DELETE** `/episodes/1`
Headers: `Authorization: Bearer <JWT_TOKEN>`

**Response:**
```json
{ "message": "Episode deleted" }
```

### Error Example (Invalid Rating)

**POST** `/appearances`
```json
{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 10
}
```
**Response:**
```json
{ "error": "Rating must be between 1 and 5." }
```

---

## Contributing

PRs welcome! Please open an issue or pull request for improvements or bugfixes.

---

## License

MIT

---

## GitHub Repo

[https://github.com/crucialniccur/late-show-api-challenge](https://github.com/crucialniccur/late-show-api-challenge)

---

Questions? Onyi tulia ... Tatakae...Eren Jaeger
