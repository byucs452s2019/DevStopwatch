

# to run as web application --
# /... User$ FLASK_APP=app.py flask run


from flask import Flask, request, url_for, render_template, redirect, send_file
app = Flask(__name__)


import sqlite3
# conn = sqlite3.connect('db/data.db')
# c = conn.cursor()

# for row in c.execute('SELECT * FROM User;'):
# 	print(row)


@app.route('/template')
def test():
	return render_template('todo.html')





@app.route('/', methods=['GET'])
def index():
	return send_file('static/base.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return send_file('static/register.html')
	else:
		conn = sqlite3.connect('db/data.db')
		c = conn.cursor()
		c.execute('SELECT * FROM User')
		count = len(c.fetchall())
		for row in c.fetchall():
			if row[1] == request.form['username']:
				print('username already taken')
				return send_file('static/register.html')
		c.execute(
			'''
			INSERT INTO User (id, username, password)
			VALUES ({id}, '{username}', '{password}');
			'''.format(id=(count + 1),
						username=request.form['username'],
						password=request.form['password'])
		)
		conn.commit()
		conn.close()
		return send_file('static/index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method != 'POST':
		print('this isn\'t a post!')
		return send_file('static/login.html')
	else:
		conn = sqlite3.connect('db/data.db')
		c = conn.cursor()
		c.execute(
			'''
			SELECT * FROM User
			WHERE User.username='{username}'
			AND User.password='{password}'
			'''.format(username=request.form['username'], password=request.form['password'])
		)
		row = c.fetchone()
		print(row)
		conn.commit()
		conn.close()

		# row is just a tuple
		print(row[1])

		return redirect("/static/index.html")


@app.route('/insert', methods=['POST'])
def insert():
	return 'Insert data!'


@app.route('/all_users')
def all_users():
	conn = sqlite3.connect('db/data.db')
	c = conn.cursor()
	resp = '<table><tr><th>user id</th><th>username</th><th>password</th></tr>'
	for row in c.execute('SELECT * FROM User;'):
		resp += "<tr>"
		resp += "<td>{}</td>".format(row[0])
		resp += "<td>{}</td>".format(row[1])
		resp += "<td>{}</td>".format(row[2])
		resp += "</tr>"
	resp += '</table><style> table { border-collapse: collapse;} table * * {border'
	return resp