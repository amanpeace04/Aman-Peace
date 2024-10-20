from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import pymysql

pymysql.install_as_MySQLdb()  # iss line se mera mysql chal jayega.

app = Flask(__name__)

# ye line MySQL database ko Flask ke saath connect karne ke liye hai.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567@localhost/college_db'
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'  # ye table name hai.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Qualification(db.Model):
    __tablename__ = 'students_qualification'  # Ye Table name hai.

    id = db.Column(db.Integer, primary_key=True)  
    h_qual = db.Column(db.String(255), nullable=False)
    y_passing = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def home():
    return render_template('index.html')

    # isse hamari student ya jo bhi table hum bna rhe hai wo iss line se ban jayegi manually table create karne ki jarurat nhi hai SQL me.
@app.before_request
def create_tables():
    db.create_all()

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        prn_no = request.form['prn_no']
        bar_code = request.form['bar_code']
        return "Login successful!"
    return render_template('student_login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        course = request.form['course']

        print(f"Name: {name}, Email: {email}, Phone: {phone}, DOB: {dob}, Course: {course}") 

        # ye lines se mySQL me student wali table me data save karegi.
        new_student = Student(name=name, email=email, phone=phone, dob=dob, course=course)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('qualification_details'))  
    return render_template('registration.html')

@app.route('/qualification_details', methods=['GET', 'POST'])
def qualification_details():
    if request.method == 'POST':
        h_qual = request.form['highest_qualification']
        y_passing = request.form['year_of_passing']
        grade = request.form['grade']

        print(f"h_qual: {h_qual}, y_passing: {y_passing}, grade: {grade}")  

        # ye lines se mySQL me qualification wali table me data save karegi.
        new_qualification = Qualification(h_qual=h_qual, y_passing=y_passing, grade=grade)
        db.session.add(new_qualification)
        db.session.commit()

        return redirect(url_for('upload_page'))  
    return render_template('qualification_details.html')



@app.route('/upload', methods=['POST', 'GET'])
def upload_page():
    return render_template('upload.html')

@app.route('/prn_no', methods=['GET', 'POST'])
def prn_page():
    reg_no = generate_registration_number()
    bar_code = generate_registration_number()  
    return render_template('prn_no.html', reg_no=reg_no, bar_code=bar_code)

def generate_registration_number():
    return random.randint(100000000, 999999999)

if __name__ == '__main__':
    app.run(debug=True)
