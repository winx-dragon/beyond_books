# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:50:07 2019

@author: buzz buzz
"""




''' msg = ''
   if 'loggedin' in session:
       msg = 'You have logged in already. Why would you register again?'
   elif request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
       username = request.form['username']
       password = request.form['password']
       email = request.form['email']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM users WHERE username = %s', [username])
       register = cursor.fetchone()
       
       if register:
            msg = 'Account already exists!'
       elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
       elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
       elif not username or not password or not email:
            msg = 'Please fill out the form!'
       else:
         
            cursor.execute('INSERT INTO users VALUES (NULL,%s, %s, %s)', [username, password, email])
            mysql.connection.commit()
            flash('You have successfully registered! Thank you for registering.')
            return redirect(url_for('home'))
   elif request.method == 'POST':
            msg = 'Please fill out the form!'
   
    
   return render_template('REGISTER2.html', msg=msg)
    '''