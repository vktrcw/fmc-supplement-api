# FMC Supplement Store API

A back-end REST API for **FMC**, a supplement brand. The API provides
the data layer and business logic that a future FMC website or mobile
app could connect to. Built for the Nucamp *Modern Software
Engineering with DevOps* portfolio project.

## Overview

The application implements a **2-tier architecture**:

- **Web tier** — a Django + Django REST Framework application
- **Database tier** — a PostgreSQL database

Both tiers run as containers managed by Docker Compose.

## Features

- **Product catalog** — browse FMC supplements, filter by category,
  and search by keyword.
- **Orders** — create customer orders containing one or more products,
  with each order line recording the price at the time of purchase.
- **Admin site** — Django's built-in admin for managing catalog data.

## Tech Stack

- Python 3.9
- Django 4.2 / Django REST Framework
- PostgreSQL 16
- Docker & Docker Compose

## API Endpoints

| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| GET    | `/api/products/`       | List products (`?category=`, `?search=`) |
| GET    | `/api/products/<id>/`  | Retrieve a single product         |
| GET    | `/api/categories/`     | List categories                   |
| GET    | `/api/categories/<id>/`| Retrieve a single category        |
| POST   | `/api/orders/`         | Create an order                   |
| GET    | `/api/orders/`         | List orders                       |
| GET    | `/api/orders/<id>/`    | Retrieve a single order           |

## Running Locally

1. Clone the repository.
2. Create a `.env` file in the project root (see below).
3. Build and start the containers: