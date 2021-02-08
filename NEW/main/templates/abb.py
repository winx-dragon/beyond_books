# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:54:56 2019

@author: buzz buzz
"""

msg = ''
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', [username,password])
        login = cursor.fetchone()
       
        if login:
            session['loggedin'] = True
            session['id'] = login['uid']
            session['username'] = login['username']
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        
        else:
             msg = 'Incorrect username/password!'
    elif 'loggedin' in session:
        msg = 'You have already logged in. PLease log out'
    return render_template('login.html', msg=msg)



if request.method=="POST":
		username=request.form.get("name")
		password=request.form.get("password")

		usernamedata=db.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
		passworddata=db.execute("SELECT password FROM users WHERE username=:username",{"username":username}).fetchone()

		if usernamedata is None:
			flash("No username","danger")
			return render_template('login.html')
		elif passworddata:
					session["log"]=True
					flash("You are now logged in!!","success")
					return redirect(url_for('hello')) #to be edited from here do redict to either svm or home
	    else:
					flash("incorrect password","danger")
					return render_template('login.html')

	return render_template('login.html')