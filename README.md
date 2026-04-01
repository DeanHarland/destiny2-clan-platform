# Destiny 2 Clan Platform

## Overview

The **Destiny 2 Clan Platform** is a full-stack Django web application designed for Destiny 2 players to find, join, and manage clans.

The platform allows users to:

* Create and manage clans
* Post recruitment listings
* Comment and interact with posts
* Join and leave clans
* (Stretch) Organise events and receive notifications

This project focuses on **user roles, relational data, and CRUD functionality**, demonstrating key full-stack development concepts.

---

## Features

### MVP Features

* User authentication (register, login, logout)
* Player profile system
* Clan creation and management
* Clan membership system
* Recruitment post CRUD (Create, Read, Update, Delete)
* Comment system on posts
* Role-based permissions (User, Clan Member, Admin, Leader)

---

### Stretch Features

* Event calendar for clans
* Notifications system
* Post filtering and tagging
* Moderation dashboard

---

## User Roles

* **Visitor** – Can browse posts, clans, and profiles
* **User** – Can create comments, apply to clans, manage profile
* **Clan Member** – Can access clan-specific content
* **Clan Admin** – Can manage posts and members
* **Clan Leader** – Full clan control
* **Moderator/Admin** – Platform-wide management

---

## UX Design

The application is designed with a **simple and intuitive user flow**:

* Visitors can browse content before signing up
* Users can quickly apply to clans from recruitment posts
* Clan management is centralised within clan profile pages
* Navigation is consistent across all pages using a shared layout

---

## Data Model

The project is built around relational data models including:

* User & Profile (One-to-One)
* Clan & Membership (Many-to-Many)
* Recruitment Posts (One-to-Many)
* Comments (One-to-Many)
* Tags (Many-to-Many)

This structure supports scalable relationships and role-based permissions.

---

## Technologies Used

### Backend

* Django
* PostgreSQL

### Frontend

* Django Templates
* Bootstrap 5

### Deployment

* Heroku

---

## Project Structure

```
destiny2-clan-platform/
│
├── users/
├── clans/
├── posts/
├── comments/
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/DeanHarland/destiny2-clan-platform.git
cd destiny2-clan-platform
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file and add:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

### 5. Run migrations

```
python manage.py migrate
```

### 6. Run the server

```
python manage.py runserver
```

---

## Deployment

The project is deployed using **Heroku**.

Key deployment steps:

* Configure PostgreSQL database
* Set environment variables
* Collect static files
* Run migrations on deployment

---

## Testing

Testing includes:

* CRUD functionality
* Authentication and permissions
* Clan membership logic

Django’s built-in testing framework is used.

---

## Future Improvements

* Real-time notifications
* Improved search and filtering
* UI enhancements and animations
* API integration with Bungie (optional)
* Messaging system between players

---

## Credits

* Destiny 2 by Bungie
* Bootstrap for frontend styling
* Django documentation and community resources

---

## Disclaimer

This project is for educational purposes only and is not affiliated with Bungie.