from flask import Flask, render_template
from feature.api.check import check_user
from feature.api.add import add_user
from feature.api.delete import delete_user
from feature.api.edit import edit_user  
from feature.login import auth  
from flask_login import LoginManager, current_user, login_required
from extensions import db
from models.user_login import Register
import os

app = Flask(__name__)
app.register_blueprint(check_user)
app.register_blueprint(add_user)
app.register_blueprint(delete_user)
app.register_blueprint(edit_user)
app.register_blueprint(auth)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisscretkry'
db.init_app(app=app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
    
@login_manager.user_loader
def load_user(user_id):     
    return Register.query.get(user_id)

@app.route('/')
def initial():
    return render_template('initial.html')
    
    
    
    
    
    
app.app_context().push()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)