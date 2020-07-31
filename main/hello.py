from flask import Flask, render_template, redirect, url_for, request,session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import MySQLdb
from base64 import b64encode



app = Flask(__name__)

app.secret_key = "allthelettersofthealphabet"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'anki@123janvi'
app.config['MYSQL_DB'] = 'pythonregister'


mysql=MySQL(app)
mysql = MySQL()
conn = MySQLdb.connect("localhost","root","anki@123janvi","pythonregister" )
cursor = conn.cursor()
cursor2=conn.cursor()
list1=[]
@app.route('/')
def home():
    qry = 'SELECT Image FROM book'
    cursor.execute(qry)    
    data = cursor.fetchall()
    ct=len(data)
    for x in range(0,ct):
            A=data[x][0]
            ph=b64encode(A).decode("utf-8")
            if [ph,x+1] not in list1:
                list1.append([ph,x+1])   
    return render_template("home.html",list1=list1)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/search/', methods=['GET', 'POST'])
def search():
    msg=''
    if request.method == "POST":
        search = request.form['search']
        ''' query1= "SELECT id,Name,Author FROM book WHERE book.Name = %s UNION ALL SELECT id,Name,MusicianBand FROM music WHERE music.Name = %s UNION ALL SELECT id,Name,Director FROM movies WHERE movies.Name = %s"
        cursor.execute(query1,[search,search,search])
        data = cursor.fetchall() '''
        q1="SELECT id,Name,Author FROM book WHERE Name LIKE %s"
        q2="SELECT id,Name,Director FROM movie WHERE Name LIKE %s"
        q3="SELECT id,Name,MusicianBand FROM music WHERE Name LIKE %s"
        cursor.execute(q1,[search+'%']) 
        if cursor.rowcount>0:
            data1=cursor.fetchall()       
            return render_template('search22.html',data1=data1)
        cursor.execute(q2,[search+'%'])
        if cursor.rowcount>0:
             data2=cursor.fetchall()
             return render_template('search22.html',data2=data2)
        cursor.execute(q3,[search+'%'])
        if cursor.rowcount>0:
             data3=cursor.fetchall()
             return render_template('search22.html',data3=data3)
        else:
             msg='Sorry no such book,movie or music'
    return render_template('search22.html',msg=msg)
    
@app.route('/userlogin/',methods=["GET","POST"])
def userlogin():
    msg= ''
    
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
             msg ='Incorrect username/password!'
    elif 'loggedin' in session:
        msg = 'You have already logged in. PLease log out'
    return render_template('userlogin.html', msg=msg) 

@app.route('/adminlogin/',methods=["GET","POST"])
def adminlogin():
    msg= ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', [username,password])
        login = cursor.fetchone()
       
        if login:
            session['adminloggedin'] = True
            session['id'] = login['id']
            session['username'] = login['username']
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        
        else:
             msg = 'Incorrect username/password!'
    elif 'loggedin' in session or 'adminloggedin' in session:
        msg = 'You have already logged in. PLease log out'
    return render_template('adminlogin.html', msg=msg)

@app.route('/login/',methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route('/logre/',methods=["GET","POST"])
def logre():
    if 'loggedin' in session or 'adminloggedin' in session:
        flash('You have already logged in.')
        return redirect(url_for('home'))
    return render_template('logre.html')


'''@app.route('/deleteuser/<id>', methods=['GET', 'POST'])
def deleteuser(id):
    l=[]
    qry = 'SELECT * FROM users WHERE uid=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()   
   
    if request.method =='POST':
        qry='select uid from users where uid> %s'
        cursor.execute(qry,[id])
        conn.commit()
        if cursor.rowcount==0:
            qry = 'DELETE FROM users WHERE uid=%s'
            cursor.execute(qry,[id])
            conn.commit()            
        else:                        	
            number=cursor.fetchall()
            for x in number:
                l.append(x[0])
            a=l[0]
            l.insert(0,a-1)            
            qry = 'DELETE FROM users WHERE uid=%s'
            cursor.execute(qry,[id])
            conn.commit()        
            for i in range(len(l)):            
                    qry="UPDATE users SET uid=%s WHERE uid=%s"
                    cursor.execute(qry,[l[i],l[i]+1])
                    conn.commit()
           
        qry = 'SELECT * FROM users'
        cursor.execute(qry)
        data=cursor.fetchall()
        return redirect(url_for('users', value=data))
    return render_template('deleteuser.html',value=data)'''

l=[]
@app.route('/deletebook/<id>', methods=['GET', 'POST'])
def deletebook(id): 
    l=[]
    qry = 'SELECT * FROM book WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()   
   
    if request.method =='POST':
        qry='select id from book where id> %s'
        cursor.execute(qry,[id])
        conn.commit()
        if cursor.rowcount==0:
            qry = 'DELETE FROM book WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()            
        else:                        	
            number=cursor.fetchall()
            for x in number:
                l.append(x[0])
            a=l[0]
            l.insert(0,a-1)            
            qry = 'DELETE FROM book WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()        
            for i in range(len(l)):            
                    qry="UPDATE book SET id=%s WHERE id=%s"
                    cursor.execute(qry,[l[i],l[i]+1])
                    conn.commit()
           
        qry = 'SELECT * FROM book'
        cursor.execute(qry)
        data=cursor.fetchall()
        return redirect(url_for('book', value=data))

    return render_template('deletebook.html', value=data)
@app.route('/editbook/<id>',methods=["GET","POST"])
def editbook(id):
    qry = 'SELECT * FROM book WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()
    if request.method =='POST':        
        Name=request.form['name']
        Author=request.form['author']
        Publisher=request.form['publisher']
        Year=request.form['year']
        Description=request.form['description']
        Genre=request.form['genre']
        Quantity=request.form['quantity']
        qry = 'SELECT name FROM book WHERE id=%s'
        aqry= 'SELECT author FROM book WHERE id=%s'
        pqry = 'SELECT publisher FROM book WHERE id=%s'
        yqry = 'SELECT year FROM book WHERE id=%s'
        dqry = 'SELECT description FROM book WHERE id=%s'
        gqry = 'SELECT genre FROM book WHERE id=%s'
        qqry = 'SELECT quantity FROM book WHERE id=%s'
        if Name!= qry:
            qry="UPDATE book SET name=%s Where id=%s"
            cursor.execute(qry,[Name,id])
            conn.commit()
            
        if Author!= aqry:
            qry="UPDATE book SET author=%s Where id=%s"
            cursor.execute(qry,[Author,id])
            conn.commit()
            
        if Publisher!= pqry:
            qry="UPDATE book SET publisher=%s Where id=%s"
            cursor.execute(qry,[Publisher,id])
            conn.commit()
        if Year!= yqry:
            qry="UPDATE book SET year=%s Where id=%s"
            cursor.execute(qry,[Year,id])
            conn.commit()
        if Description!= dqry:
            qry="UPDATE book SET description=%s Where id=%s"
            cursor.execute(qry,[Description,id])
            conn.commit()
        if Genre!= gqry:
            qry="UPDATE book SET genre=%s Where id=%s"
            cursor.execute(qry,[Genre,id])
            conn.commit()
        if Quantity!= qqry:
            qry="UPDATE book SET quantity=%s Where id=%s"
            cursor.execute(qry,[Quantity,id])
            conn.commit()
        
        qry='SELECT * FROM book WHERE id=%s'
        cursor.execute(qry,[id])
        data=cursor.fetchall()
        msg = 'The changes have been made'
        return render_template('editbook.html',value=data,msg=msg)
    msg='No changes are detected.'    
    return render_template('editbook.html',value=data,msg=msg)



@app.route('/editmovie/<id>',methods=["GET","POST"])
def editmovie(id):
    qry = 'SELECT * FROM movie WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()
    if request.method =='POST':        
        Name=request.form['name']
        Director=request.form['director']
        Year=request.form['year']
        Description=request.form['description']
        Genre=request.form['genre']
        Quantity=request.form['quantity']
        qry = 'SELECT name FROM movie WHERE id=%s'
        aqry= 'SELECT director FROM movie WHERE id=%s'
        yqry = 'SELECT year FROM movie WHERE id=%s'
        dqry = 'SELECT description FROM movie WHERE id=%s'
        gqry = 'SELECT genre FROM movie WHERE id=%s'
        qqry = 'SELECT quantity FROM movie WHERE id=%s'
        if Name!= qry:
            qry="UPDATE movie SET name=%s Where id=%s"
            cursor.execute(qry,[Name,id])
            conn.commit()
            
        if Director!= aqry:
            qry="UPDATE movie SET director=%s Where id=%s"
            cursor.execute(qry,[Director,id])
            conn.commit()
            
        if Year!= yqry:
            qry="UPDATE movie SET year=%s Where id=%s"
            cursor.execute(qry,[Year,id])
            conn.commit()
        if Description!= dqry:
            qry="UPDATE movie SET description=%s Where id=%s"
            cursor.execute(qry,[Description,id])
            conn.commit()
        if Genre!= gqry:
            qry="UPDATE movie SET genre=%s Where id=%s"
            cursor.execute(qry,[Genre,id])
            conn.commit()
        if Quantity!= qqry:
            qry="UPDATE movie SET quantity=%s Where id=%s"
            cursor.execute(qry,[Quantity,id])
            conn.commit()
        
        qry='SELECT * FROM movie WHERE id=%s'
        cursor.execute(qry,[id])
        data=cursor.fetchall()
        msg = 'The changes have been made'
        return render_template('editmovie.html',value=data,msg=msg)
    msg='No changes are detected.'    
    return render_template('editmovie.html',value=data,msg=msg)



@app.route('/editmusic/<id>',methods=["GET","POST"])
def editmusic(id):
    qry = 'SELECT * FROM music WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()
    if request.method =='POST':        
        Name=request.form['name']
        MusicianBand=request.form['musicianband']
        Album=request.form['album']
        Year=request.form['year']
        Description=request.form['description']
        Genre=request.form['genre']
        Quantity=request.form['quantity']
        qry = 'SELECT name FROM music WHERE id=%s'
        aqry= 'SELECT musicianband FROM music WHERE id=%s'
        pqry = 'SELECT album FROM music WHERE id=%s'
        yqry = 'SELECT year FROM music WHERE id=%s'
        dqry = 'SELECT description FROM music WHERE id=%s'
        gqry = 'SELECT genre FROM music WHERE id=%s'
        qqry = 'SELECT quantity FROM music WHERE id=%s'
        if Name!= qry:
            qry="UPDATE music SET name=%s Where id=%s"
            cursor.execute(qry,[Name,id])
            conn.commit()
            
        if MusicianBand!= aqry:
            qry="UPDATE music SET musicianband=%s Where id=%s"
            cursor.execute(qry,[MusicianBand,id])
            conn.commit()
            
        if Album!= pqry:
            qry="UPDATE music SET album=%s Where id=%s"
            cursor.execute(qry,[Album,id])
            conn.commit()
        if Year!= yqry:
            qry="UPDATE music SET year=%s Where id=%s"
            cursor.execute(qry,[Year,id])
            conn.commit()
        if Description!= dqry:
            qry="UPDATE music SET description=%s Where id=%s"
            cursor.execute(qry,[Description,id])
            conn.commit()
        if Genre!= gqry:
            qry="UPDATE music SET genre=%s Where id=%s"
            cursor.execute(qry,[Genre,id])
            conn.commit()
        if Quantity!= qqry:
            qry="UPDATE music SET quantity=%s Where id=%s"
            cursor.execute(qry,[Quantity,id])
            conn.commit()
        
        qry='SELECT * FROM music WHERE id=%s'
        cursor.execute(qry,[id])
        data=cursor.fetchall()
        msg = 'The changes have been made'
        return render_template('editmusic.html',value=data,msg=msg)
    msg='No changes are detected.'    
    return render_template('editmusic.html',value=data,msg=msg)

@app.route('/deletemovies/<id>', methods=['GET', 'POST'])
def deletemovies(id):
    l=[]
    qry = 'SELECT * FROM movie WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()   
   
    if request.method =='POST':
        qry='select id from movie where id> %s'
        cursor.execute(qry,[id])
        conn.commit()
        if cursor.rowcount==0:
            qry = 'DELETE FROM movie WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()            
        else:                        	
            number=cursor.fetchall()
            for x in number:
                l.append(x[0])
            a=l[0]
            l.insert(0,a-1)            
            qry = 'DELETE FROM movie WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()        
            for i in range(len(l)):            
                    qry="UPDATE movie SET id=%s WHERE id=%s"
                    cursor.execute(qry,[l[i],l[i]+1])
                    conn.commit()
           
        qry = 'SELECT * FROM movie'
        cursor.execute(qry)
        data=cursor.fetchall()
        return redirect(url_for('movies', value=data))
    return render_template('deletemovies.html',value=data)

@app.route('/deletemusic/<id>', methods=['GET', 'POST'])
def deletemusic(id):
    l=[]
    qry = 'SELECT * FROM music WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()   
   
    if request.method =='POST':
        qry='select id from music where id> %s'
        cursor.execute(qry,[id])
        conn.commit()
        if cursor.rowcount==0:
            qry = 'DELETE FROM music WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()            
        else:                        	
            number=cursor.fetchall()
            for x in number:
                l.append(x[0])
            a=l[0]
            l.insert(0,a-1)            
            qry = 'DELETE FROM music WHERE id=%s'
            cursor.execute(qry,[id])
            conn.commit()        
            for i in range(len(l)):            
                    qry="UPDATE music SET id=%s WHERE id=%s"
                    cursor.execute(qry,[l[i],l[i]+1])
                    conn.commit()
           
        qry = 'SELECT * FROM music'
        cursor.execute(qry)
        data=cursor.fetchall()
        return redirect(url_for('music', value=data))
    return render_template('deletemusic.html', value=data)


@app.route('/displaybook/<id>')
def displaybook(id):
        q1='Select * From book Where id = %s'
        cursor.execute(q1,[id])
        data = cursor.fetchall()
        q2='Select Image from book where id = %s'
        cursor2.execute(q2,[id])
        data2=cursor2.fetchall()
        for x in data2:
            L=x[0]
            photo=b64encode(L).decode("utf-8")
        return render_template('displaybook.html',photo=photo,data=data)

@app.route('/displaymusic/<id>')
def displaymusic(id):
    qry = 'SELECT * FROM music WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()
    conn.commit()
    return render_template('displaymusic.html', value=data)

@app.route('/displaymovies/<id>')
def displaymovies(id):
    qry = 'SELECT * FROM movie WHERE id=%s'
    cursor.execute(qry,[id])
    data = cursor.fetchall()
    conn.commit()
    return render_template('displaymovies.html', value=data)

@app.route('/profile/')
def profile():
    if 'loggedin' in session:      
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE uid = %s', [session['id']])
        account = cursor.fetchone()
       
        return render_template('profile.html',account=account)
    elif 'adminloggedin' in session:
        flash('No access for admins')
    else:
        flash('Not logged in.')
    return redirect(url_for('home'))

    
@app.route('/admin/', methods=['GET','POST'])
def admin():
    if 'adminloggedin' in session:
            return render_template('elay.html')
    else:
        flash('You do not have authorization. Please log in as an admin')
        return redirect(url_for('home'))
    
@app.route('/users/', methods=['GET'])
def users():
    query = "SELECT * from users"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return render_template('users.html',value=data)

@app.route('/book/', methods=['GET',"POST"])
def book():
    conn = MySQLdb.connect("localhost","root","anki@123janvi","pythonregister" )
    cursor = conn.cursor()
    query = "SELECT * from book"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return render_template('book.html',value=data)
@app.route('/addbook/', methods=['GET',"POST"])
def addbook():
    msg=''
    if request.method == "POST" and 'name' in request.form and 'genre' in request.form and 'author' in request.form and 'publisher' in request.form and 'year' in request.form and 'description' in request.form and 'quantity' in request.form:
       name = request.form['name']      
       author = request.form['author']
       publisher = request.form['publisher']
       year = request.form['year']
       genre=request.form['genre']
       quantity=request.form['quantity']
       description = request.form['description']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM book WHERE name = %s and author = %s', [name,author])
       check=cursor.fetchone()
       if check:
           msg='This book has already been  added....'
           
       else:           
           cursor.execute('SELECT MAX(id) From book')
           r=cursor.fetchone()
           maxid=list(r.values())
           cursor.execute('INSERT INTO book VALUES(%s,%s, %s,%s,%s,%s,%s,%s)', [maxid[0]+1,name, author,publisher, year,description,genre,quantity])
           mysql.connection.commit()
           return redirect(url_for('book'))
    
    return render_template('addbook.html',msg=msg)
    
@app.route('/music/', methods=['GET',"POST"])
def music():
    conn = MySQLdb.connect("localhost","root","anki@123janvi","pythonregister" )
    cursor = conn.cursor()
    query = "SELECT * from music"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return render_template('music.html',value=data)

@app.route('/addmusic/', methods=['GET',"POST"])
def addmusic(): 
    msg=''
    if request.method == "POST" and 'name' in request.form and 'genre' in request.form and 'album' in request.form and 'musicianband' in request.form and 'year' in request.form and 'description' in request.form and 'quantity' in request.form:
       name = request.form['name']      
       musicianband = request.form['musicianband']
       album = request.form['album']
       year = request.form['year']
       genre=request.form['genre']
       quantity=request.form['quantity']
       description = request.form['description']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM music WHERE name = %s and musicianband = %s and album = %s', [name,musicianband,album])
       check=cursor.fetchone()
       if check:
           msg='This piece has already been  added....'
       else:           
           cursor.execute('SELECT MAX(id) From music')
           r=cursor.fetchone()
           maxid=list(r.values())
           cursor.execute('INSERT INTO music VALUES(%s,%s, %s,%s,%s,%s,%s,%s)', [maxid[0]+1,name, musicianband,album, year,description,genre,quantity])
           mysql.connection.commit()
           return redirect(url_for('music'))
    
    return render_template('addmusic.html',msg=msg)
   

@app.route('/movies/', methods=['GET',"POST"])
def movies():

    conn = MySQLdb.connect("localhost","root","anki@123janvi","pythonregister" )
    cursor = conn.cursor()
    query = "SELECT * from movie"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return render_template('movies.html',value=data)

@app.route('/addmovies/', methods=['GET',"POST"])
def addmovies():
    msg=''
    if request.method == "POST" and 'name' in request.form and 'genre' in request.form and 'director' in request.form and 'year' in request.form and 'description' in request.form and 'quantity' in request.form:
       name = request.form['name']      
       director = request.form['director']     
       year = request.form['year']
       genre=request.form['genre']
       quantity=request.form['quantity']
       description = request.form['description']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM movie WHERE name = %s and director = %s', [name,director])
       check=cursor.fetchone()
       if check:
           msg='This movie has already been  added....' 
       else:           
           cursor.execute('SELECT MAX(id) From movie')
           r=cursor.fetchone()
           maxid=list(r.values())
           cursor.execute('INSERT INTO movie VALUES(%s,%s, %s,%s,%s,%s,%s,%s)', [maxid[0]+1,name, director,year,description,genre,quantity])
           mysql.connection.commit()
           return redirect(url_for('book'))
    
    return render_template('addmovies.html',msg=msg)
    


@app.route('/logout/', methods = ['GET','POST'])
def logout():       
    if 'adminloggedin'in session:
        session.pop('adminloggedin')
        session.pop('id')
        session.pop('username')   
        
    if 'loggedin'in session:
        session.pop('loggedin')
        session.pop('id')
        session.pop('username') 
        
    return redirect(url_for('home'))

@app.route('/register/', methods=["GET","POST"])
def register():
    msg = ''
    if 'loggedin' in session:
       return redirect(url_for('home'))
    elif request.method == 'POST' and 'username' in request.form and 'number' in request.form  and 'password' in request.form and 'confirm' in request.form and 'email' in request.form:
       username = request.form['username']
       password = request.form['password']
       confirm = request.form['confirm']
       email = request.form['email']
       number = request.form['number']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM users WHERE username = %s', [username])
       register = cursor.fetchone()
       cursor.execute('SELECT * FROM users WHERE number = %s', [number])
       num = cursor.fetchall()
       if register:
            msg = 'Account already exists!'
       elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
       elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
       elif not username or not password or not email:
            msg = 'Please fill out the form!'
       elif num:
            msg = 'This number is already in use. Please check again.'
       elif confirm!=password:
            msg = 'The passwords do not match ' 
       else:        
            cursor.execute('SELECT MAX(uid) From users')
            r=cursor.fetchone()
            maxid=list(r.values())
            cursor.execute('INSERT INTO users VALUES (%s,%s, %s, %s,%s)', [maxid[0]+1,username, password, email,number])
            mysql.connection.commit()
            cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s',[username,password])
            login=cursor.fetchone()
            if login:
                session['loggedin'] = True
                session['id'] = login['uid']
                session['username'] = login['username']
            flash('You have successfully registered! Thank you for registering.You have logged in')
            
            return redirect(url_for('home'))
    elif request.method == 'POST':
            msg = 'Please fill out the form!'    
    return render_template('REGISTER2.html', msg=msg)
		 
if __name__ == '__main__':
    app.run()