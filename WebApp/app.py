from flask import *
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'SECRET'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'aisner'
app.config['MYSQL_DATABASE_PASSWORD'] = 'WattTeam6'
app.config['MYSQL_DATABASE_DB'] = 'DriverIncentiveDB'
app.config['MYSQL_DATABASE_HOST'] = 'mysql1.cs.clemson.edu'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        # Read posted values from UI (underscore before variable name usually denotes a private variable)
        #_name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # Validate received values
        if _email and _password:
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', ( _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@app.route('/showSignIn')
def showSignIn():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('signin.html')

@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        # connect to mySql
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][2]),_password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')

    except Exception as e:
        return render_template('error.html', error = str(e))
    finally:
        cursor.close()
        con.close()

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/profSettings')
def profSettings():
    if session.get('user'):
        return render_template('profileSettings.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/regConfirm')
def regConfirm():
    return render_template('registrationConfirmation.html')

@app.route('/catProd')
def catProd():
    if session.get('user'):
        return render_template('catalogProductPage.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/catOrdRevSub')
def catOrdRevSub():
    if session.get('user'):
        return render_template('catalogOrderReviewSubmit.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/catOrdConf')
def catOrdConf():
    if session.get('user'):
        return render_template('catalogOrderConfirmation.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/catListView')
def catListView():
    if session.get('user'):
        return render_template('catalogItemListView.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/catHome')
def catHome():
    if session.get('user'):
        return render_template('catalogHome.html')
    else:
        return render_template('error.html', error = 'Unauthorized Access')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUsWithContact.html')
    

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)

