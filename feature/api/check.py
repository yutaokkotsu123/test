from flask import Blueprint, render_template
from models.student import Student
from models.user_login import Register
from flask_login import login_required

check_user = Blueprint('check_user', __name__,
                template_folder='templates',
                static_folder='static')

column_lst = ['STT', 'Name', 'Math', 'English', 'Physics', 'Chemistry', 'Total Mark']


@check_user.route('/', methods = ["GET"])
@login_required
def check_student():
    student = Student.query.all()
    return render_template('table_sql.html', users = student, column = column_lst)



