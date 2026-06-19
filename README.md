# ICSE 2026 Conference Management Portal

A web-based Conference Management System developed using Django for managing conference registrations, paper submissions, speakers, announcements, and schedules.

### Live Website
https://conference-portal-sqa5.onrender.com/

A web-based Conference Management System developed using Django.

---

## Author

Subhashree Aich

B.Tech (AI & ML)

Sambalpur University Institute of Information Technology

---

## Project Overview

The ICSE 2026 Conference Portal is designed to automate the management of an academic conference.

The system allows:

- Participant Registration
- Research Paper Submission
- Speaker Management
- Conference Schedule Management
- Announcement Management
- Conference Statistics Dashboard
- Admin Panel Management

---

## Features

### Home Page

- Conference Information
- Countdown Timer
- Conference Statistics
- Conference Tracks
- Keynote Speakers
- Gallery
- Announcements
- Contact Section
- Sponsors Section

### Registration Module

Participants can:

- Register for conference
- Provide organization details
- Save registration information to database

### Paper Submission Module

Authors can:

- Submit research papers
- Upload PDF files
- Store submission details securely

### Speaker Management

Admin can:

- Add speakers
- Upload speaker photos
- Manage keynote speakers

### Announcement Management

Admin can:

- Create announcements
- Display latest announcements on homepage

### Schedule Management

Admin can:

- Add conference events
- Display conference schedule

### Dashboard

Displays:

- Total Participants
- Total Papers Submitted
- Total Speakers
- Total Announcements

---

## Technology Stack

### Backend

- Python
- Django

### Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript
- Chart.js

### Database

- SQLite3

---

## Project Structure

```text
conference_portal/
│
├── conference/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── home.html
│   ├── register.html
│   ├── submit_paper.html
│   ├── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│
├── media/
│
├── db.sqlite3
│
└── manage.py
```

---

## Database Models

### Registration

- Full Name
- Email
- Phone
- Organization
- Country

### Paper Submission

- Paper Title
- Author Name
- Email
- Abstract
- PDF Upload

### Speaker

- Name
- Designation
- Photo

### Announcement

- Title
- Description
- Date

### Schedule

- Time
- Event

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/conference-portal.git
```

### Move into Project

```bash
cd conference-portal
```

### Install Requirements

```bash
pip install django pillow
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

Admin Panel:

```text
http://127.0.0.1:8000/admin
```

---

## Future Enhancements

- Email Notifications
- Online Payment Gateway
- User Authentication
- Reviewer Management
- Certificate Generation
- AI-Based Paper Recommendation
- Cloud Deployment

---

## License

This project is developed for educational and academic purposes.
