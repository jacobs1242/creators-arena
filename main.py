from flask import Flask 
from public import public

from teacher import teacher
from student import student
from admin import admin


app=Flask(__name__)
app.secret_key="key"


app.register_blueprint(public)
app.register_blueprint(teacher,url_prefix='/teacher')
app.register_blueprint(student,url_prefix='/student')
app.register_blueprint(admin,url_prefix='/admin')


app.run(debug=True, host = "localhost",port=5231)