from flask import Blueprint, redirect, render_template, url_for, request, flash
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
        exists = db.session.query(Student.id).filter_by(id=student_id).first()
        if exists:
            student = Student.query.get(student_id)
            db.session.delete(student)
            db.session.commit()
            return redirect(url_for('check_user.check_student'))
        else:
            flash('Your id not exists !')
            return redirect(url_for('delete_user.delete_student_box'))

