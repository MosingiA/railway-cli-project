# 🚉 Railway Station CLI Project

A Python **Command-Line Interface (CLI)** application for managing a railway station system.  
It allows you to manage **stations, trains, and passengers**, with booking, random ticket assignment, and multiple payment options (cash or phone STK simulation).

---

## 📌 Features
- Manage **stations, trains, and passengers** using SQLAlchemy ORM.
- Add passengers with:
  - Name, Age, Phone Number
  - Randomly generated **ticket number**
  - Train selection (choose from available trains)
- Payment options:
  - **STK Push simulation** (phone-based confirmation)
  - **Cash payment** (instant acceptance)
  - **Skip payment** (still adds passenger, useful for pending transactions)
- SQLite database (`railway.db`) for persistence.
- Alembic migrations for schema updates.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **SQLAlchemy ORM**
- **Alembic** (database migrations)
- **SQLite3** (database)

---

## 📂 Project Structure
