from flask import Flask , render_template , url_for , flash , redirect
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo

app = Flask(__name__,template_folder='template')

@app.route("/")
def first():
    return render_template('first.html')

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired() , Length(min = 2 , max = 50)])
    lastname = StringField('Last Name', validators = [DataRequired() , Length(min = 2 , max = 50)])
    email = StringField('Email_ID' , validators = [DataRequired() , Email()])
    password = PasswordField('Password(Min Length = 8)' , validators = [DataRequired() , Length(min = 8)])
    conform_password = PasswordField('Conform Password' , validators = [DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email_ID' , validators = [DataRequired() , Email()])
    password = PasswordField('Password(Min Length = 8)' , validators = [DataRequired() , Length(min = 8)])
    submit = SubmitField('Log In')

@app.route("/SignUp" , methods = ['GET' , 'POST'])
def sign():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('first'))
    return render_template('sign.html' , form = form)

@app.route("/result")
def result():
      return render_template("result.html")

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug = True)