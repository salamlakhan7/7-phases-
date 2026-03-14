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
- `ZZ complete phase 4.png`: Complete overview diagram for Phase 4 secure posts

---

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
- `stripe flow chart , real.png`: Diagram of Stripe payment flow
- `stripe postman.JPG`: Postman testing screenshot for Stripe endpoints
- `stripe test fill info.JPG`: Screenshot of filling Stripe test payment info
- `stripe test success.JPG`: Screenshot of successful Stripe test payment
- `stripe test.JPG`: General Stripe testing screenshot
- `celery background worker.png`: Illustration of Celery background worker process

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
- `1A cookies-session-jwt.png`: Comparison of cookies, sessions, and JWT
- `2A.svg`: Diagram related to authentication flow
- `3A.jpg`: Image illustrating authentication concepts
- `4A client side flow.png`: Client-side authentication flow diagram
- `B1 oauth code exchange.png`: OAuth code exchange process
- `B2 Auth-code-flow-diagram.png`: Authorization code flow diagram
- `B3 code-flow-01.svg`: Code flow illustration
- `B4 logic.png`: Logic diagram for authentication
- `C1 token generation.png`: Token generation process
- `C3.webp`: Token-related diagram
- `C4.png`: Token handling illustration
- `D1 Cookie based.jpg`: Cookie-based authentication
- `D2 token-handler.svg`: Token handler diagram
- `D4.png`: Authentication diagram
- `D45.jpg`: Additional authentication image
