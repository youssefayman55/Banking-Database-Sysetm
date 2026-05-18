# 🏦 Bank Database Management System

A full-stack **Bank Management System** built using **FastAPI**, **PostgreSQL**, and modern database design principles.  
This project simulates real-world banking operations with a complete relational database system and API layer.

---

# 🚀 Project Overview

This system is designed to manage core banking operations such as:

- Customer management
- Accounts management
- Transactions (Deposit / Withdraw / Transfer)
- Loans management
- Branch operations
- Payments tracking

It provides a structured backend system using REST APIs and a normalized relational database.

---

# 🧠 Key Features

## 👤 Customer Management
- Add new customers
- View customer details
- Delete customers

## 💳 Account Management
- Create bank accounts
- Link accounts to customers
- Track balances

## 💸 Transactions System
- Deposit money
- Withdraw money
- Transfer between accounts
- Transaction history tracking

## 🏦 Loans System
- Create loan records
- Track loan status
- Associate loans with customers

## 🏢 Branch Management
- Manage bank branches
- Assign customers and accounts to branches

---

# ⚙️ Tech Stack

## Backend
- FastAPI
- Psycopg (PostgreSQL driver)
- Uvicorn

## Database
- PostgreSQL (Relational Database Design)

---

# 🏗️ System Architecture
- Frontend (Optional UI)
- FastAPI Backend (REST API)
- PostgreSQL Database


---

# 📡 API Endpoints

## 👤 Customers
- GET `/customers`
- POST `/customers`
- DELETE `/customers/{customer_id}`

## 💳 Accounts
- GET `/accounts`
- POST `/accounts`
- DELETE `/accounts/{account_id}`

## 💸 Transactions
- GET `/transactions`
- POST `/transactions`
- DELETE `/transactions/{transaction_id}`

## 🏦 Loans
- GET `/loans`
- POST `/loans`
- DELETE `/loans/{loan_id}`

## 🏢 Branches
- GET `/branches`
- POST `/branches`
- DELETE `/branches/{branch_id}`

---

# 🗄️ Database Schema (Conceptual)

Main tables:

- customers
- accounts
- transactions
- loans
- branches

### Relationships:
- One customer → Many accounts
- One account → Many transactions
- One customer → Many loans
- One branch → Many accounts/customers

---

## 🚀 Future Improvements :
- JWT Authentication (Login System)
- Role-based access (Admin / Staff / Customer)
- Transaction security layer
- Logging system
- Docker deployment
- Cloud hosting (Render / AWS)
- Frontend dashboard (React or Streamlit)

---

##👨‍💻 Author
- Developed by: Youssef Ayman Hamed
- Field: Backend Development / Database Systems / AI Engineering
