# 📝 Task Management System

A professional full-stack Task Management Web Application built using Flask, MySQL, Bootstrap 5, HTML, CSS, and JavaScript.

This application helps users efficiently manage their daily tasks with features like authentication, dashboard analytics, task filtering, categories, file uploads, priority management, and responsive UI design.

---

# 🚀 Features

## 🔐 Authentication System
✅ Secure User Registration  
✅ Login & Logout System  
✅ Password Hashing using Flask-Bcrypt  
✅ Session-based Authentication  

---

## 📋 Task Management
✅ Create Tasks  
✅ Edit Tasks  
✅ Delete Tasks  
✅ View All Tasks  
✅ Search Tasks  
✅ Filter Tasks by Status  

---

## 📊 Dashboard Analytics
✅ Total Tasks Counter  
✅ Pending Tasks Counter  
✅ In Progress Tasks Counter  
✅ Completed Tasks Counter  

---

## 🗂️ Task Organization
✅ Task Categories  
✅ Priority Levels:
- Low
- Medium
- High

✅ Task Status:
- Pending
- In Progress
- Completed

---

## 📎 File Uploads
✅ Upload Attachments for Tasks  
✅ View Uploaded Files  

---

## 🎨 UI / UX
✅ Responsive Design  
✅ Bootstrap 5 Interface  
✅ Modern Dashboard  
✅ Flash Messages  
✅ Mobile Friendly Layout  
✅ Clean Navigation Bar  

---

# 🛠️ Technologies Used

## 🔹 Backend
- Python 3
- Flask
- Flask-MySQLdb
- Flask-Bcrypt
- Werkzeug
- Python-dotenv

---

## 🔹 Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Font Awesome

---

## 🔹 Database
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
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone your_repository_link
cd task-management-system
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### ▶️ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup MySQL Database

```sql
CREATE DATABASE task_manager;
```

Import the `database.sql` file.

---

## 5️⃣ Configure Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=task_manager
```

---

## 6️⃣ Run Application

```bash
python app.py
```

Application runs on:

```text
http://127.0.0.1:5000
```

---

# 💻 Usage

## 👤 Register Account
✅ Open Register Page  
✅ Enter Username, Email, Password  
✅ Click Register  

---

## 🔑 Login
✅ Enter Email & Password  
✅ Click Login  

---

## 📊 Dashboard
✅ View Task Statistics  
✅ Monitor Task Progress  

---

## 📋 Manage Tasks
✅ Add New Task  
✅ Edit Existing Tasks  
✅ Delete Tasks  
✅ Upload Attachments  
✅ Filter Tasks  
✅ Search Tasks  

---

# 🐛 Troubleshooting

## ❌ MySQL Connection Error

### Error

```text
Can't connect to MySQL server
```

### Solution

✅ Ensure MySQL Server is running  
✅ Check `.env` credentials  
✅ Verify database exists  

---

## ❌ Module Not Found Error

### Error

```text
ModuleNotFoundError
```

### Solution

```bash
pip install -r requirements.txt
```

---

## ❌ Port Already in Use

### Error

```text
Address already in use
```

### Solution

```python
app.run(debug=True, port=5001)
```

---

# 🔮 Future Enhancements

✅ REST API Integration  
✅ JWT Authentication  
✅ React Frontend  
✅ Email Notifications  
✅ Calendar View  
✅ Admin Panel  
✅ Dark Mode Toggle  
✅ Export Tasks to PDF/Excel  
✅ Mobile Application  

---

# 👨‍💻 Author

✨ BATTULA VENKATA KRISHNA KARTHIK
✨ Linkedin -> https://www.linkedin.com/in/battulavenkatakrishnakarthik/
✨ Email -> bvenkatakrishnakarthik@gmail.com
