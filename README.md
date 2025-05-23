# 📝 Flask Todo App with Authentication

A simple and elegant Todo List application built using Flask and SQLite. It includes user registration and login functionality so that each user can manage their own todos securely.

## ✨ Features

- User registration and login
- Session-based authentication
- Create, update, delete, and check/uncheck todos
- Todos are user-specific
- Clean and responsive UI with dark theme
- Fully functional using HTML, CSS (no JS required)

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-todo-auth.git
cd flask-todo-auth
```

### 2. Create Virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, install manually:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```

### 4. Run the App

```bash
python app.py
```

Open your browser and go to:  
📍 `http://127.0.0.1:5000`

---

## 🗃️ Project Structure

```
flask-todo-auth/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── update.html
│
├── static/
│   └── style.css
```

---

## 🔐 Authentication Flow

1. Users must **register** before they can login.
2. Only **logged-in users** can access the todo home page.
3. If not logged in, all requests to `/home` will redirect to `/login`.

---

## 📸 Screenshots

> You can include screenshots of your app here for better presentation.

---

## 📄 License

This project is licensed under the MIT License - feel free to use and modify!

---

## 💡 Suggestions

Want to improve this app?
- Add due dates and categories
- Use JavaScript for animations
- Switch to PostgreSQL or MySQL for production
- Deploy on Render, Heroku, or Vercel

---

## 👤 Author

**Abdullha Mulla**  
📧 abdullahmulla002@gmail.com  
📱 9986366573
