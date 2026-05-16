📝 Task Management System

A modern full-stack Task Management Web Application built using Flask, MySQL, Bootstrap 5, and JavaScript.

This application helps users efficiently organize, manage, and track their daily tasks with features like authentication, task categories, file uploads, priority management, status tracking, dashboard analytics, and responsive UI design.

🚀 Features
🔐 Authentication System
User Registration
Secure Login & Logout
Password Hashing using Flask-Bcrypt
Session-based Authentication
📋 Task Management
Create Tasks
Edit Tasks
Delete Tasks
View All Tasks
Task Search & Filtering
📊 Dashboard Analytics
Total Tasks Count
Pending Tasks Count
In Progress Tasks Count
Completed Tasks Count
🗂️ Categories & Organization
Task Categories
Priority Levels:
Low
Medium
High
Status Tracking:
Pending
In Progress
Completed
📎 File Uploads
Upload Attachments for Tasks
View Uploaded Files
🎨 UI/UX
Responsive Design
Bootstrap 5 Interface
Dark Styled Navbar
Mobile-Friendly Layout
Flash Messages & Alerts
🛠️ Technologies Used
Backend
Python 3
Flask
Flask-MySQLdb
Flask-Bcrypt
Werkzeug
Frontend
HTML5
CSS3
Bootstrap 5
JavaScript
Database
MySQL


📂 Project Structure
task_manager/
│
├── app.py
├── config.py
├── requirements.txt
├── database.sql
├── .env
│
├── models/
├── routes/
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── templates/
│
└── venv/
⚙️ Installation
Clone Repository
git clone https://github.com/your-username/task-manager.git
cd task-manager
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Setup MySQL Database
CREATE DATABASE task_manager;

Import the SQL tables from database.sql.

Configure Environment Variables

Create .env file:

SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=task_manager
Run Application
python app.py

Open browser:

http://127.0.0.1:5000
📌 Future Enhancements
REST API Integration
JWT Authentication
React Frontend
Email Notifications
Calendar View
Admin Dashboard
Dark Mode Toggle
Deployment to Cloud
👨‍💻 Author

Built by Likith Matam using Flask + MySQL Full Stack Development.

Pasted text(4).txt
Document
"" give me README about my project like in the given field
# 📝 Task Management System

A professional full-stack Task Management Web Application built using Flask, MySQL, Bootstrap 5, HTML, CSS, and JavaScript.

This application helps users efficiently manage their daily tasks with features like authentication, dashboard analytics, task filtering, categories, file uploads, priority management, and responsive UI design.

---

# 🚀 Features

## 🔐 Authentication System
- Secure User Registration
- Login & Logout System
- Password Hashing using Flask-Bcrypt
- Session-based Authentication

## 📋 Task Management
- Create Tasks
- Edit Tasks
- Delete Tasks
- View All Tasks
- Search Tasks
- Filter Tasks by Status

## 📊 Dashboard Analytics
- Total Tasks Counter
- Pending Tasks Counter
- In Progress Tasks Counter
- Completed Tasks Counter

## 🗂️ Task Organization
- Task Categories
- Priority Levels:
  - Low
  - Medium
  - High

- Task Status:
  - Pending
  - In Progress
  - Completed

## 📎 File Uploads
- Upload Attachments for Tasks
- View Uploaded Files

## 🎨 UI / UX
- Responsive Design
- Bootstrap 5 Interface
- Modern Dashboard
- Flash Messages
- Mobile Friendly Layout
- Clean Navigation Bar

---

# 📸 Screenshots

## Dashboard
Dashboard Screenshot

## Tasks Management
Tasks Screenshot

## Login Page
Login Screenshot

## Register Page
Register Screenshot

## Profile Page
Profile Screenshot

---

# 🛠️ Technologies Used

## Backend
- Python 3
- Flask
- Flask-MySQLdb
- Flask-Bcrypt
- Werkzeug
- Python-dotenv

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

## Database
- MySQL

---

# 📂 Project Structure

```bash
task_manager/
│
├── app.py
├── config.py
├── requirements.txt
├── database.sql
├── .env
├── .gitignore
│
├── models/
│   ├── __init__.py
│   └── database.py
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── tasks.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── uploads/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── tasks.html
│   ├── edit_task.html
│   └── profile.html
│
└── venv/
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/task-management-system.git

cd task-management-system
2️⃣ Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup MySQL Database

Open MySQL Workbench and run:

CREATE DATABASE task_manager;

Then import the database.sql file.

5️⃣ Configure Environment Variables

Create .env file in project root directory:

SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=task_manager
6️⃣ Run Application
python app.py

Application runs on:

http://127.0.0.1:5000
💻 Usage
Register Account
Open Register Page
Enter Username, Email, Password
Click Register
Login
Enter Email & Password
Click Login
Dashboard
View task statistics
Monitor task progress
Manage Tasks
Add New Task
Edit Existing Tasks
Delete Tasks
Upload Attachments
Filter Tasks
Search Tasks
🐛 Troubleshooting
MySQL Connection Error
Error
Can't connect to MySQL server
Solution
Ensure MySQL Server is running
Check .env credentials
Verify database exists
Module Not Found Error
Error
ModuleNotFoundError
Solution
pip install -r requirements.txt
Port Already in Use
Error
Address already in use
Solution

Change port in app.py:

app.run(debug=True, port=5001)
📝 Future Enhancements
REST API Integration
JWT Authentication
React Frontend
Email Notifications
Calendar View
Admin Panel
Dark Mode Toggle
Export Tasks to PDF/Excel
Mobile Application
👨‍💻 Author:
    BATTULA VENKATA KRISHNA KARTHIK
    LINKEDIN :- https://www.linkedin.com/in/battulavenkatakrishnakarthik/
    EMAIL :- bvenkatakrishnakarthik@gmail.com
