# Backend Mastery

This repository is a step-by-step learning progression across 7 phases, each represented by a Django app.

---

## Phase 1 – Project setup
- Django project: `backend_mastery`
- Database: `db.sqlite3`
- Base settings, URL routing, and app registration.

---

## Phase 2 – CRUD API (api1_crud)
- App: `api1_crud`
- Model: `Task` (title, description, is_completed, created_at)
- API: DRF `ModelViewSet` for full CRUD on tasks
- Endpoints (via router):
  - `GET /tasks/`
  - `POST /tasks/`
  - `GET /tasks/{id}/`
  - `PUT/PATCH /tasks/{id}/`
  - `DELETE /tasks/{id}/`

---

## Phase 3 – Posts API (api2_posts)
- App: `api2_posts`
- Model: `Post` (title, content, img, owner, created_at)
- Owner is set automatically from the authenticated user
- Queryset is filtered to only return posts owned by requester
- Endpoints (via router):
  - `GET /posts/` (owner-only)
  - `POST /posts/` (owner auto-assigned)
  - `GET /posts/{id}/`
  - `PUT/PATCH /posts/{id}/`
  - `DELETE /posts/{id}/`

---

## Phase 4 – Secure Posts API (api3_secure_posts)
- App: `api3_secure_posts`
- Model: `SecurePost` (title, content, image, owner, created_at)
- Uses `IsAuthenticated` permission for all endpoints
- Handles image cleanup on update/delete
- Endpoints (via router):
  - `GET /secure-posts/` (owner-only)
  - `POST /secure-posts/` (owner auto-assigned)
  - `GET /secure-posts/{id}/`
  - `PUT/PATCH /secure-posts/{id}/` (cleans up old image)
  - `DELETE /secure-posts/{id}/` (removes image file)

### Images
![Complete overview diagram for Phase 4 secure posts](req_Images/ZZ%20complete%20phase%204.png)

---

## Phase 5 – Exam Blog (exam_blog)

## Phase 5 – Exam Blog (exam_blog)
- App: `exam_blog`
- Model: `Article` (title, body, cover_img, owner, created_at)
- Permissions:
  - `IsAuthenticatedOrReadOnly` for general access
  - `IsOwnerOrReadOnly` custom permission (only owner can modify/delete)
- Handles image cleanup on update/delete
- Endpoints (via router):
  - `GET /articles/` (open to all)
  - `POST /articles/` (auth required)
  - `GET /articles/{id}/`
  - `PUT/PATCH /articles/{id}/` (owner only)
  - `DELETE /articles/{id}/` (owner only)

---

## Phase 6 – Gateway (Gateway)
- App: `Gateway`
- Models:
  - `Product` (name, description, price)
  - `Order` (user, product, price_at_purchase, status)
  - `Transaction` (order, gateway, transaction_id, amount, status)
- Stripe integration:
  - `POST /create-checkout-session/` creates Stripe checkout session and order
  - `POST /webhook/` handles Stripe webhook, marks order paid, creates transaction
- Celery task example: `send_welcome_email` in `Gateway/tasks.py`

### Images
![Diagram of Stripe payment flow](req_Images/stripe%20flow%20chart%20,%20real.png)
![Postman testing screenshot for Stripe endpoints](req_Images/stripe%20postman.JPG)
![Screenshot of filling Stripe test payment info](req_Images/stripe%20test%20fill%20info.JPG)
![Screenshot of successful Stripe test payment](req_Images/stripe%20test%20success.JPG)
![General Stripe testing screenshot](req_Images/stripe%20test.JPG)
![Illustration of Celery background worker process](req_Images/celery%20background%20worker.png)

---

## Phase 7 – Test1 (test1)
- App: `test1`
- Models:
  - `Test` (owner, test_score, rank, is_medical_clear)
  - `Profile` (OneToOne with User, token_version)
- Authentication / JWT:
  - Custom JWT claims via `MyTokenObtainPairSerializer`
  - Login/logout with JWT blacklisting
  - Google OAuth login flow (redirect & callback)
- Permissions:
  - `IsOwnerOrReadOnly` (resource owner can modify)
  - `IsAdminGroup` (requires user in "Admin" group)
- Endpoints:
  - `POST /register/` (register new user)
  - `POST /api/token/` (obtain JWT)
  - `POST /api/logout/` (blacklist JWT refresh token)
  - `POST /admin-test/` (admin group only)
  - `GET /auth/google/login/` (redirect to Google OAuth)
  - `GET /auth/google/callback/` (handle OAuth callback)
  - `CRUD /tests/` (TestViewSet)

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
