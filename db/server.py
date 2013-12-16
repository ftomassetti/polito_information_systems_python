from flask import Flask,request,render_template
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

import MySQLdb as mdb

MYSQL_HOST = "localhost"
MYSQL_DATABASE_USER = "root"
MYSQL_DATABASE_PASSWORD = "root"
MYSQL_DATABASE_DB = "infosys"

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
@app.route('/index.html')
def index():
    # http://localhost:5000?user=Tim
    username= request.args.get('user')

    if not username:
        username='Anonymous'
    user = { 'nickname': username }

    return render_template("index.html", user = user)

@app.route("/insertdata.html", methods=["GET","POST"])
def insertData():
    form = RegistrationForm()
    if form.validate_on_submit():
        status = storeData(form)
        return render_template("data.html", status=status)
    return render_template("insertdata.html",form=form)


def storeData(form):
    name = form.name.data
    surname = form.surname.data
    username= form.username.data
    gender = form.gender.data
    address = form.address.data
    city = form.city.data
    country = form.country.data

    db = mdb.connect(MYSQL_HOST, MYSQL_DATABASE_USER, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_DB);
    cursor = db.cursor()

    createTableSQL = "CREATE TABLE IF NOT EXISTS users (id MEDIUMINT NOT NULL AUTO_INCREMENT,\
         name VARCHAR(30), surname VARCHAR(30), username VARCHAR(30),\
         gender VARCHAR(1), address VARCHAR(50), city VARCHAR(30), country VARCHAR(30),PRIMARY KEY(id));"

    cursor.execute(createTableSQL)

    checkUserSQL = "SELECT username from users"

    cursor.execute(checkUserSQL)
    result = cursor.fetchall()
    found = False
    for row in result:
        print(row[0])
        if row[0]==username:
            found = True
    if not found:
        insertSQL = "INSERT INTO users (name,surname,username,gender,address,city,country) VALUES \
        ('"+str(name)+"','"+str(surname)+"','"+str(username)+"','"+str(gender)+"','"+str(address)+"','"+str(city)+"','"+str(country)+"');"

        try:
            cursor.execute(insertSQL)
            db.commit()
            status = "USER INFORMATION ARE STORED CORRECTLY"
        except:
            db.rollback()
            status = "THERE WAS AN ERROR. DATA NOT STORED"
    else:
            status = "The username you entered already exists. "

    cursor.close()
    return status

@app.route("/getuserinfo.html")
def userInfo():
    db = mdb.connect(MYSQL_HOST, MYSQL_DATABASE_USER, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_DB);
    cursor = db.cursor()
    checkUserSQL = "SELECT * from users"
    cursor.execute(checkUserSQL)
    result = cursor.fetchall()

    dbrows = []
    for row in result:

        dbrows.append({
                      'name':       row[1],
                      'surname':    row[2],
                      'username':   row[3],
                      'gender':     row[4],
                      'address':    row[5],
                      'city':       row[6],
                      'country':    row[7]
                      })

    return render_template("showdata.html",dbrows=dbrows)

class RegistrationForm(Form):
    name = TextField( 'name', validators = [Required()])
    surname = TextField( 'surname', validators = [Required()])
    username = TextField( 'username', validators = [Required()])
    gender = TextField( 'gender', validators = [Required()])
    address = TextField( 'address', validators = [Required()])
    city = TextField( 'city', validators = [Required()])
    country = TextField( 'country', validators = [Required()])

if __name__ == "__main__":
    app.debug=True
    app.run()#host='0.0.0.0')
