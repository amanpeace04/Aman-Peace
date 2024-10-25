from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Ye connection hai.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567@localhost/institute_db'
db = SQLAlchemy(app)

# Isse Student table define hoti hai.
class Student(db.Model):
    __tablename__ = 'students'  # Table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    highest_qualification = db.Column(db.String(255), nullable=False)
    year_of_passing = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    passport_photo = db.Column(db.String(255), nullable=False)  
    signature = db.Column(db.String(255), nullable=False)  
    marksheet = db.Column(db.String(255), nullable=False)  
    prn_no = db.Column(db.String(255), nullable=True)  
    barcode = db.Column(db.String(255), nullable=True)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    return render_template('index.html')

# Isse Automatically table create ho jayegi database (MySQL) me.
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
        highest_qualification = request.form['highest_qualification']
        year_of_passing = request.form['year_of_passing']
        grade = request.form['grade']

        # Isse User ke docs upload honge.
        passport_photo = request.files['passport_photo'].filename
        signature = request.files['signature'].filename
        marksheet = request.files['marksheet'].filename

        # Upload file ko save karne ke liye. Isse static folder ke uploads folder me user ke docs save honge.
        request.files['passport_photo'].save(f'static/uploads/{passport_photo}')
        request.files['signature'].save(f'static/uploads/{signature}')
        request.files['marksheet'].save(f'static/uploads/{marksheet}')

        # Database (MySQL) me data save karne ke liye.
        new_student = Student(
            name=name, email=email, phone=phone, dob=dob, course=course,
            highest_qualification=highest_qualification, year_of_passing=year_of_passing, grade=grade,
            passport_photo=passport_photo, signature=signature, marksheet=marksheet
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('prn_page', student_id=new_student.id))  
    return render_template('registration.html')

# For generating Prn Number & Bar Code
@app.route('/prn_no/<int:student_id>', methods=['GET', 'POST'])
def prn_page(student_id):
    reg_no = generate_registration_number()
    bar_code = generate_registration_number()  
    # Isse apna prn number and bar code bhi MySQl me Chala jayega.
    student = Student.query.get(student_id)
    if student:
        student.prn_no = reg_no
        student.barcode = bar_code
        db.session.commit()

    return render_template('prn_no.html', reg_no=reg_no, bar_code=bar_code)

def generate_registration_number():
    return random.randint(100000000, 999999999)

if __name__ == '__main__':
    app.run(debug=True)
