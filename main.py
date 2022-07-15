import datetime
import os
import urllib.request
from flask import flash
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras


app = Flask(__name__)

app.secret_key = "ami-trambadiya"

DB_HOST = "localhost"
DB_NAME = "studentDB"
DB_USER = "postgres"
DB_PASS = "test123"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)

UPLOAD_FOLDER = 'static/upload/'
UPLOAD_FILE = 'static/files/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_FILE'] = UPLOAD_FILE


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ----------------------------------------Login-----------------------------------------


@app.route('/')
def index():
    if 'loggedin' in session:
        return redirect(url_for('showdata'))
    else:
        if 'userloggedin' in session:
            return redirect(url_for('userprofile'))
        else:
            return render_template("login.html")


@app.route("/adminlogin", methods=["GET", "POST"])
def adminlogin():
    cur = conn.cursor()
    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        cur.execute(
            f"SELECT * FROM admin_login WHERE email = '{email}' AND passwd = '{password}'")
        account = cur.fetchone()

        cur.execute(f"SELECT * FROM user_login WHERE email = '{email}'")
        accountuser = cur.fetchone()

        if account:
            session['loggedin'] = True
            session['email'] = account[1]
            session['password'] = account[2]
            session['username'] = account[3]
            flash(u'You loggedin Successfully')
            return redirect(url_for('showdata'))

        elif accountuser:
            passwordrs = accountuser[3]
            check = check_password_hash(passwordrs, password)
            if check:
                session['userloggedin'] = True
                session['id'] = accountuser[0]
                session['username'] = accountuser[2]
                session['email'] = accountuser[1]
                session['password'] = accountuser[3]
                flash(u'You loggedin Successfully')
                return redirect(url_for('userprofile'))
            else:
                msgg = "Incorrect username/password"
                return render_template('login.html', msgg=msgg)

        else:
            error = "Incorrect username/password"
            return render_template('login.html', error=error)

    cur.close()
    return render_template('login.html')

# -------------------------------------Admin Dashboard--------------------------------------


@app.route('/adminmaster', methods=["GET", "POST"])
def showdata():
    if session['loggedin']:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM user_profile,user_login"
                    f" where user_login.id = user_profile.user_id order by user_login.id desc")
        account = cur.fetchall()
        print(account)
        return render_template("admin_master.html", data=account)
    else:
        return render_template("login.html")

# Edit User


@app.route('/euser/<int:user_id>')
def euser(user_id):
    if session['loggedin']:
        cur = conn.cursor()
        cur.execute(
            f"SELECT * FROM user_profile, user_login WHERE user_login.id = '{user_id}' and user_profile.user_id = '{user_id}'")
        account = cur.fetchone()
        print(account)
        return render_template("edit_user.html", account=account)
    else:
        return redirect(url_for('login'))


@app.route("/updateuser", methods=["GET", "POST"])
def updateuser():
    if session['loggedin']:
        if request.method == "POST":
            user_id = request.form.get("userid")
            fname = request.form.get("fname")
            lname = request.form.get("lname")
            dob = request.form.get("dob")
            mobile = request.form.get("mobile")
            gender = request.form.get("gender")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            zipcode = request.form.get("zipcode")
            username = request.form.get('username')
            email = request.form.get('email')
            date_modified = datetime.date.today()
            cur = conn.cursor()
            cur.execute(
                f"UPDATE user_profile set first_name='{fname}', last_name='{lname}', date_of_birth='{dob}', mobile_number='{mobile}', gender='{gender}', address='{address}', city='{city}', state='{state}', zipcode='{zipcode}', profile_updated_dt='{date_modified}' WHERE user_id='{user_id}'")
            cur.execute(
                f"UPDATE user_login set username='{username}', email='{email}' WHERE id='{user_id}'")
            conn.   commit()
            cur.close()
            flash(u'User details updated successfully')
        return redirect(url_for('showdata'))
    else:
        return redirect(url_for('login'))

# Delete User


@app.route('/delete/<int:user_id>')
def delete(user_id):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM user_profile WHERE user_id ='{user_id}'")
    cur.execute(f"DELETE FROM user_login WHERE id ='{user_id}'")
    conn.commit()
    cur.close()
    return redirect(url_for('showdata'))

# Add User


@app.route("/createuser", methods=["GET", "POST"])
def createuser():
    return render_template("add_user.html")


@app.route("/adduser", methods=["GET", "POST"])
def adduser():
    if session['loggedin']:
        cur = conn.cursor()
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_pw = request.form.get('confirm_pw')
        cur.execute(f"select * from user_login where email='{email}'")
        user_exist = cur.fetchone()
        cur.close()
        if user_exist:
            msg = "Account with this email aready exist, please try another email..!!"
            return render_template("add_user.html", error=msg)
        if request.method == "POST":
            if password == confirm_pw:
                nuser()
            else:
                msg = "Password and Confirm password doesn't match..."
                return render_template("add_user.html", error=msg)
    else:
        return redirect(url_for('login'))
    return redirect(url_for('showdata'))


def nuser():
    cur = conn.cursor()
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hash_pw = generate_password_hash(password)
    cur.execute(
        f"""INSERT INTO user_login (username,email,passwd) VALUES('{username}','{email}','{hash_pw}')""")
    conn.commit()
    cur.execute("SELECT max(id) FROM user_login")
    new_id = cur.fetchone()
    cur.execute(f"""INSERT INTO user_profile (user_id)VALUES('{new_id[0]}')""")
    conn.commit()
    cur.close()
    flash(u'User created successfully')
    return redirect(url_for('showdata'))


# Change Password
@app.route('/changepw/<int:user_id>')
def changepw(user_id):
    if session['loggedin']:
        cur = conn.cursor()
        cur.execute(
            f"SELECT * FROM user_profile,user_login where user_login.id = '{user_id}'and user_profile.user_id = '{user_id}'")
        account = cur.fetchone()
        print(account)

        return render_template("change_pw.html", account=account)
    else:
        return redirect(url_for(showdata))


@app.route('/resetpw/<int:user_id>', methods=["GET", "POST"])
def resetpw(user_id):
    if session['loggedin']:
        password = request.form.get('newpassword')
        confirmpw = request.form.get('confirmpw')
        if request.method == "POST":
            if password == confirmpw:
                conpw()

            else:
                error = "Password and Confirm password doesn't match..."
                cur = conn.cursor()
                cur.execute(
                    f"SELECT * FROM user_profile,user_login where user_login.id = '{user_id}'and user_profile.user_id = '{user_id}'")
                account = cur.fetchone()
                return render_template("change_pw.html", account=account, error=error)
    else:
        return redirect(url_for('login'))
    return redirect(url_for('showdata'))


def conpw():
    cur = conn.cursor()
    user_id = request.form.get("user_id")
    password = request.form.get("newpassword")
    has_pw = generate_password_hash(password)
    cur.execute(
        f"UPDATE user_login set passwd='{has_pw}' WHERE id='{user_id}'")
    conn.commit()
    cur.close()
    flash(u'Password updated successfully')
    return redirect(url_for('showdata'))


# ---------------------------User Profile-------------------------------

@app.route('/userprofile')
def userprofile():
    if session['userloggedin']:
        cur = conn.cursor()
        user_id = session['id']
        cur.execute(
            f"SELECT * FROM user_profile,user_login where user_login.id ='{user_id}' and user_profile.user_id='{user_id}'")
        accountuser = cur.fetchone()
        return render_template("user_profile.html", accountuser=accountuser)
    else:
        return render_template("login.html")


@app.route('/user_id', methods=["GET", "POST"])
def updateprofile():
    user_id = session['id']
    if session['userloggedin']:
        cur = conn.cursor()
        cur.execute(
            f"SELECT * FROM user_profile,user_login where user_login.id = '{user_id}' and user_profile.user_id = '{user_id}'")
        accountuser = cur.fetchone()
        cur.close()
        return render_template("update_user.html", accountuser=accountuser)
    else:
        return redirect(url_for('login'))

# Update User


@app.route("/userdata", methods=["GET", "POST"])
def userdata():
    if session['userloggedin']:
        if request.method == "POST":
            user_id = request.form.get("userid")
            fname = request.form.get("fname")
            lname = request.form.get("lname")
            dob = request.form.get("dob")
            mobile = request.form.get("mobile")
            gender = request.form.get("gender")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            zipcode = request.form.get("zipcode")
            username = request.form.get('username')
            email = request.form.get('email')
            file = request.files['file']
            pdffile = request.files['pdffile']
            date_modified = datetime.date.today()
            cur = conn.cursor()
            if request.method == "POST":
                pdfnm = secure_filename(pdffile.filename)
                filename = secure_filename(file.filename)
                pdffile.save(os.path.join(
                    app.config['UPLOAD_FOLDER_FILE'], pdfnm))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute(f"UPDATE user_profile set first_name='{fname}', last_name='{lname}', date_of_birth='{dob}', mobile_number='{mobile}', gender='{gender}', address='{address}', city='{city}', state='{state}', zipcode='{zipcode}', profile_updated_dt='{date_modified}', img='{filename}', birth_certificate='{pdfnm}'  WHERE user_id='{user_id}'")
            cur.execute(
                f"UPDATE user_login set username='{username}', email='{email}'WHERE id='{user_id}'")
            conn.commit()
            cur.close()
            flash(u'Your profile updated successfully')
        return redirect(url_for('userprofile'))
    else:
        return redirect(url_for('login'))


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='upload/' + filename))


#
# @app.route('/photo', methods=["GET", "POST"])
# def photo():
#     user_id = session['id']
#     if session['userloggedin']:
#         cur = conn.cursor()
#         cur.execute(f"SELECT * FROM user_profile,user_login where user_login.id = '{user_id}' and user_profile.user_id = '{user_id}'")
#         accountuser = cur.fetchone()
#     return render_template("user_photo.html", accountuser = accountuser)


@app.route('/logoutadmin')
def logoutadmin():
    session['loggedin'] = False
    session.clear()
    return render_template("login.html")


@app.route('/logoutuser')
def logoutuser():
    session['userloggedin'] = False
    session.clear()
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
