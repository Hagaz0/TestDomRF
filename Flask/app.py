from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import functions as f

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'Users %r' % self.id

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/handle_form', methods=['POST'])
def handle_form():
    action = request.form.get('action')
    email = request.form.get('email')
    password = request.form.get('password')
    repeat_password = request.form.get('repeat_password')
    name = request.form.get('name')

    if action == 'signup':
        if f.checks(email, password, repeat_password, name) is False:
            return render_template("error_empty.html")

        if f.is_login(email) is None:
            return render_template("error_mail.html")

        if len(password) < 6 and len(password) > 20:
            return render_template("error_pass.html")

        if password != repeat_password:
            return render_template("error_password.html")

        if Users.query.filter(Users.mail == email).first():
            return render_template("error_same_mail.html")

        user = Users(name=name, mail=email, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return render_template("reg_success.html")
        except:
            return "При регистрации произошла ошибка"

    elif action == 'signin':
        result = Users.query.filter(Users.mail == email, Users.password == password).first()
        if result:
            users = Users.query.order_by(Users.id).all()
            return render_template("users.html", users=users)
        else:
            return render_template("error_log.html")

@app.route('/users')
def users():
    users = Users.query.order_by(Users.id).all()
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run()
