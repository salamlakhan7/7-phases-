
---

# 🚀 Backend Mastery – Django Backend Engineering Roadmap

<div align="center">

<img src="https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/Django%20REST%20Framework-API-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge&logo=jsonwebtokens">
<img src="https://img.shields.io/badge/OAuth-Google-blue?style=for-the-badge&logo=google">
<img src="https://img.shields.io/badge/Stripe-Payments-purple?style=for-the-badge&logo=stripe">
<img src="https://img.shields.io/badge/Celery-Background%20Tasks-brightgreen?style=for-the-badge&logo=celery">
<img src="https://img.shields.io/badge/Redis-Message%20Broker-red?style=for-the-badge&logo=redis">
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge">

</div>

**A practical backend engineering learning journey using Django and Django REST Framework.**

This repository demonstrates how backend systems evolve from **basic CRUD APIs to production-style architecture including authentication, payments, OAuth, and background processing.**

[Features](#-features) • [Phases](#-learning-phases) • [Installation](#-installation) • [Tech Stack](#-tech-stack)

</div>

---

# 🌟 Features

### Backend Engineering Concepts Covered

* 🔧 **Django Project Architecture**
* 🔌 **REST APIs with Django REST Framework**
* 🔐 **Authentication & Authorization**
* 🧑‍💻 **Owner-based Data Access**
* 🛡 **Permission Systems**
* 📷 **File & Image Handling**
* 💳 **Stripe Payment Gateway**
* ⚡ **Background Tasks with Celery**
* 🔑 **JWT Authentication**
* 🌐 **Google OAuth Login**
* 📡 **Secure API Design**

---

# 🧭 Learning Phases

This repository is organized as a **7-phase backend learning roadmap**, where each phase introduces new backend concepts.

---

# Phase 1 – Project Setup

* Django project: `backend_mastery`
* Database: `db.sqlite3`
* Base settings and project configuration
* URL routing and application structure

---

# Phase 2 – CRUD API (`api1_crud`)

### Model

`Task`

Fields:

* title
* description
* is_completed
* created_at

### API

Uses **Django REST Framework ModelViewSet**

### Endpoints

```
GET /tasks/
POST /tasks/
GET /tasks/{id}/
PUT/PATCH /tasks/{id}/
DELETE /tasks/{id}/
```

---

# Phase 3 – Posts API (`api2_posts`)

### Model

`Post`

Fields:

* title
* content
* img
* owner
* created_at

### Features

* Owner automatically assigned from authenticated user
* Queryset filtered to only show **user's own posts**

### Endpoints

```
GET /posts/
POST /posts/
GET /posts/{id}/
PUT/PATCH /posts/{id}/
DELETE /posts/{id}/
```

---

# Phase 4 – Secure Posts API (`api3_secure_posts`)

### Model

`SecurePost`

Fields:

* title
* content
* image
* owner
* created_at

### Security

* `IsAuthenticated` permission
* Image cleanup on update/delete

### Endpoints

```
GET /secure-posts/
POST /secure-posts/
GET /secure-posts/{id}/
PUT/PATCH /secure-posts/{id}/
DELETE /secure-posts/{id}/
```

### Images

![Complete overview diagram for Phase 4 secure posts](req_Images/ZZ%20complete%20phase%204.png)

---

# Phase 5 – Exam Blog (`exam_blog`)

### Model

`Article`

Fields:

* title
* body
* cover_img
* owner
* created_at

### Permissions

* `IsAuthenticatedOrReadOnly`
* `IsOwnerOrReadOnly` (custom permission)

### Features

* Image cleanup on update/delete
* Owner-restricted modifications

### Endpoints

```
GET /articles/
POST /articles/
GET /articles/{id}/
PUT/PATCH /articles/{id}/
DELETE /articles/{id}/
```

---

# Phase 6 – Payment Gateway (`Gateway`)

### Models

**Product**

```
name
description
price
```

**Order**

```
user
product
price_at_purchase
status
```

**Transaction**

```
order
gateway
transaction_id
amount
status
```

### Stripe Integration

Endpoints:

```
POST /create-checkout-session/
POST /webhook/
```

### Celery Background Task

Example:

```
send_welcome_email
```

Located in:

```
Gateway/tasks.py
```

### Images

![Diagram of Stripe payment flow](req_Images/stripe%20flow%20chart%20,%20real.png)

![Postman testing screenshot for Stripe endpoints](req_Images/stripe%20postman.JPG)

![Screenshot of filling Stripe test payment info](req_Images/stripe%20test%20fill%20info.JPG)

![Screenshot of successful Stripe test payment](req_Images/stripe%20test%20success.JPG)

![General Stripe testing screenshot](req_Images/stripe%20test.JPG)

![Illustration of Celery background worker process](req_Images/celery%20background%20worker.png)

---

# Phase 7 – Authentication System (`test1`)

### Models

**Test**

```
owner
test_score
rank
is_medical_clear
```

**Profile**

```
OneToOne with User
token_version
```

### Authentication

* Custom JWT token serializer
* Refresh token blacklisting
* Google OAuth login

### Permissions

* `IsOwnerOrReadOnly`
* `IsAdminGroup`

### Endpoints

```
POST /register/
POST /api/token/
POST /api/logout/
POST /admin-test/
GET /auth/google/login/
GET /auth/google/callback/
CRUD /tests/
```

### Images

![Comparison of cookies, sessions, and JWT](req_Images/1A%20cookies-session-jwt.png)

![Diagram related to authentication flow](req_Images/2A.svg)

![Image illustrating authentication concepts](req_Images/3A.jpg)

![Client-side authentication flow diagram](req_Images/4A%20client%20side%20flow.png)

![OAuth code exchange process](req_Images/B1%20oauth%20code%20exchange.png)

![Authorization code flow diagram](req_Images/B2%20Auth-code-flow-diagram.png)

![Code flow illustration](req_Images/B3%20code-flow-01.svg)

![Logic diagram for authentication](req_Images/B4%20logic.png)

![Token generation process](req_Images/C1%20token%20generation.png)

![Token-related diagram](req_Images/C3.webp)

![Token handling illustration](req_Images/C4.png)

![Cookie-based authentication](req_Images/D1%20Cookie%20based.jpg)

![Token handler diagram](req_Images/D2%20token-handler.svg)

![Authentication diagram](req_Images/D4.png)

![Additional authentication image](req_Images/D45.jpg)

---

# ⚙ Installation

Clone repository

```
git clone https://github.com/salamlakhan7/7-phases-.git
cd 7-phases-
```

Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Run server

```
python manage.py runserver
```

---

# 🛠 Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* JWT (SimpleJWT)
* Google OAuth
* Celery
* Redis
* Stripe API

### Database

* SQLite (development)
* PostgreSQL recommended for production

---

# 📁 Project Structure

```
backend_mastery/
│
├── api1_crud
├── api2_posts
├── api3_secure_posts
├── exam_blog
├── Gateway
├── test1
│
├── backend_mastery/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── req_Images/
├── manage.py
└── README.md
```

---

# 👨‍💻 Author

**Abdul Salam**

GitHub
[https://github.com/salamlakhan7](https://github.com/salamlakhan7)

---

# ⭐ Support

If you find this project useful, consider giving it a **star ⭐ on GitHub.**

---

If you want, I can also show you **one small addition (a system architecture diagram) that would make this README look like a senior backend portfolio project.**
