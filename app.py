from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/student_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Student Model
class Student(db.Model):
    __tablename__ = 'students'  # Add this line to specify the table name

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)

# Routes
@app.route('/')
def index():
    students = Student.query.all()  # Get all students from the database
    return render_template('index.html', students=students)

@app.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    
    if request.method == 'POST':
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.dob = request.form['dob']
        student.amount_due = request.form['amount_due']
        
        db.session.commit()  # Commit the changes to the database
        return redirect('/')  # Redirect back to the students list
    
    return render_template('update.html', student=student)  # Render update form with current student data

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)  # Delete the student record
    db.session.commit()  # Commit the deletion
    return redirect('/')  # Redirect back to the students list

if __name__ == "__main__":
    app.run(debug=True)
