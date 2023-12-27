from flask import Flask, redirect,render_template,request,session,url_for,flash
import mysql.connector
connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='taskmanagementsystem'
        )
mycursor=connection.cursor()

#Create a flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

#Define a route and corresponding view Home page
@app.route('/')
def log():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('home.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']
    authenticate_query = "SELECT * FROM users WHERE user_name = %s AND password = %s"
    mycursor.execute(authenticate_query, (username, password))
    authenticated_user = mycursor.fetchone()
    if authenticated_user:
        return render_template("home.html", user=username)
    else:
        return render_template('login.html', msg="Invalid username or password.")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirm_password')
        email=request.form.get('email')
        if password != confirmpassword:
            flash('Passwords do not match. Please try again.', 'error')
        else:
            check_query = "SELECT * FROM users WHERE user_name = %s"
            mycursor.execute(check_query, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                flash('Username already taken. Please choose another.', 'error')
            else:
                insert_query = "INSERT INTO users (user_name,email,password,confirm_password) VALUES (%s, %s,%s,%s)"
                data = (username,email,password,confirmpassword)
                mycursor.execute(insert_query, data)
                connection.commit()
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('log'))
    return render_template('register.html')

@app.route('/add')
def create():
    return render_template("add.html")

@app.route('/add_task', methods=['POST'])
def addtask():
    userid = request.form.get('user_id')
    tasktitle = request.form.get('title')
    description = request.form.get('description')
    duedate = request.form.get('due_date')
    status = request.form.get('status')
    query = "INSERT INTO tasks (user_id, title, description, due_date, status) VALUES (%s, %s, %s, %s, %s)"
    data = (userid, tasktitle, description, duedate, status)
    mycursor.execute(query, data)
    connection.commit()
    return render_template('home.html')

@app.route('/view')
def view():
    query = "SELECT user_id,task_id, title, description, due_date, status FROM tasks"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template("view.html",sqldata=data)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/update_task', methods=['POST'])
def updatetask():
    if request.method == 'POST':
        userid = request.form.get('user_id')
        status = request.form.get('status')
        query = "UPDATE tasks SET status = %s WHERE user_id = %s"
        sqldata = (status, userid)
        mycursor.execute(query, sqldata)
        connection.commit()
        return render_template('home.html')
    
@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/search_task',methods=['POST'])
def searchtask():
    userid=request.form.get('user_id')
    query = "SELECT user_id, task_id, title, description, due_date, status FROM tasks WHERE user_id = '{}'".format(userid)
    mycursor.execute(query)
    data=mycursor.fetchall()
    if not data:
      return render_template("search.html",msg="Task Not Found!")  
    else:
        return render_template("view.html",sqldata=data)
    
@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/delete_task', methods=['POST'])
def deletetask():
    if request.method == 'POST':
        userid = request.form.get('user_id')  
        query = "DELETE FROM tasks WHERE user_id = %s"
        sqldata = (userid,)
        mycursor.execute(query, sqldata)
        connection.commit()
        return render_template('home.html')
    
@app.route('/logout')
def logout():
    # Clear the user session
    session.clear()

    return render_template('login.html')
#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug=True)
