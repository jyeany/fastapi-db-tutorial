# FastAPI DB Connection Tutorial

### Overview
Code from the SQL (Relational) Databases of 
FastAPI documentation with added alembic migration scripts.
Also, requests in .http format have been added in http-requests folder.

### Running Migrations
```
alembic upgrade head
```

### Running application
```
uvicorn main:app --reload
```
