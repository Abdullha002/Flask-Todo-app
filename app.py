# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret-key'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    checked = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('login'))

# Authentication routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return "User already exists."
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Todo routes
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            todo = Todo(name=name, user_id=user_id)
            db.session.add(todo)
            db.session.commit()
        return redirect(url_for('home'))

    todos = Todo.query.filter_by(user_id=user_id).order_by(Todo.id.desc()).all()
    return render_template('index.html', todos=todos)


@app.route('/checked/<int:todo_id>', methods=['POST'])
def checked(todo_id):
    todo = Todo.query.get(todo_id)
    if todo and todo.user_id == session.get('user_id'):
        todo.checked = not todo.checked
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo and todo.user_id == session.get('user_id'):
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/update/<int:todo_id>", methods=["GET", "POST"])
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == "POST":
        todo.name = request.form.get("name")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", todo=todo)


if __name__ == '__main__':
    app.run(debug=True)
