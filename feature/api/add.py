from models.student import Student, db
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required


add_user = Blueprint('add_user', __name__)


@add_user.route('/add/student')
def add_student_box():
    return render_template('add_stu.html')

@add_user.route('/add/student', methods = ["POST", "GET"])
@login_required
def add_student():
    if request.method == "POST":
        name = request.form.get('name')
        math = request.form.get('math')
        english = request.form.get('english')
        chemistry = request.form.get('chemistry')
        physics = request.form.get('physics')
        
        
        # if not math.isnumeric:
        #     flash('Check your math !')
        #     math = request.form.get('math')
        #     return redirect(url_for('add_user.add_student_box'))
        # if not str(english).isnumeric:
        #     flash('Check your english !')
        #     return redirect(url_for('add_user.add_student_box'))
        # if not str(chemistry).isnumeric:
        #     flash('Check your chemistry !')
        #     return redirect(url_for('add_user.add_student_box'))
        # if not str(physics).isnumeric:
        #     flash('Check your physics')
        #     return redirect(url_for('add_user.add_student_box'))
            
        
        total_mark = (float(english)+float(chemistry)+float(physics)+float(math))/4
        new_student = Student(name=name, math=math, english=english,
                            chemistry=chemistry, physics=physics,
                            total_mark=total_mark)
        db.session.add(new_student)    
        db.session.commit()
        return redirect(url_for('check_user.check_student'))
    else: return "Wrong"


