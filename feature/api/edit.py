from models.student import Student, db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required




edit_user = Blueprint("edit_user", __name__)

@edit_user.route('/edit/student')
@login_required
def edit_student():
    return render_template('edit_stu.html')

@edit_user.route('/edit/student', methods = ["PUT", "GET", "POST"])
@login_required
def edit_student_box():
     if request.method == "POST":
        user_id = request.form.get('id')
        exists = db.session.query(Student.id).filter_by(id=user_id).first() 
        if exists is not None :
            user = Student.query.get(user_id)
            name = request.form.get('name')
            math = request.form.get('math')
            english = request.form.get('english')
            physics = request.form.get('physics')
            chemistry = request.form.get('chemistry')
            
            # If input == "" then dont update 
            if name is "":
                name = user.name
            if math is "":
                math = user.math
            if english is "":
                english = user.english
            if chemistry is "":
                chemistry = user.chemistry
            if physics is "":
                physics = user.physics
                
            # Set self in4 = input in4
            user.name = name
            user.math = float(math)
            user.english = float(english)
            user.physics = float(physics)
            user.chemistry = float(chemistry)
            total_mark = (user.english+user.chemistry+user.physics+user.math)/4
            user.total_mark = total_mark
            db.session.commit()
            return redirect(url_for('check_user.check_student'))
        else:
            flash('Please check your id you enter !')
            return redirect(url_for('edit_user.edit_student_box'))
