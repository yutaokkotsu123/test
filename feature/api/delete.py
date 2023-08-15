from flask import Blueprint, redirect, render_template, url_for, request
from models.student import Student, db
from flask_login import login_required

delete_user = Blueprint("delete_user", __name__)


@delete_user.route('/delete/student')
@login_required
def delete_student():
    return render_template('delete_stu.html')

@delete_user.route('/delete/student', methods = ["GET", "DELETE", "POST"])
@login_required
def delete_student_box():
    if request.method == "POST":    
        student_id = request.form.get('id')
        if student_id is not None:
            student = Student.query.get(student_id)
            db.session.delete(student)
            db.session.commit()
            return redirect(url_for('check_user.check_student'))
        else: return "Check your id"

