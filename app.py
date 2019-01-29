from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session	
app = Flask(__name__)

app.secret_key = "lksfjdklshfsdkl"

from databases import *


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/cars')
def cars():
	return render_template ("cars.html")

@app.route('/fps')
def fps():
	return render_template ("fps.html")

@app.route('/mmorpg')
def mmorpg():
	return render_template ("mmorpg.html")

@app.route('/moba')
def moba():
	return render_template ("moba.html")

@app.route('/',methods=['POST','GET'])
def home():
	if request.method=='POST':
		user = query_user_by_email(request.form['email'])
		if user != None and user.password==request.form['password']:
			login_session['name'] = user.name
			login_session['email'] = user.email
			return redirect(url_for('home'))
		return redirect('/')
	if request.method=='GET':
		return render_template('home.html')

@app.route('/signup',methods=['POST','GET'])
def sign_up():
	if request.method=='POST':
		add_user(request.form['name'],
			request.form['email'],
			request.form['password'])
		return redirect(url_for('home'))
	if request.method=='GET':
		return render_template('signup.html')

@app.route('/homepage', methods=['GET','POST'])
def login():
	if request.method=='GET':
		if 'email' in login_session:
			user=query_user_by_email(login_session['email'])
			return render_template('homepage.html', user=user)
		else:
			return render_template('homepage.html')

@app.route('/logout')
def logout():
	if 'name' in login_session: 
		del login_session['name']
	if 'email' in login_session:
		del login_session['email']
	return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)