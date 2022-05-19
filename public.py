from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/loginbutton')
def loginbutton():
	return render_template('loginbutton.html')
	


@public.route('/login',methods=['get','post'])
def login():

	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']


			if res[0]['usertype']=='teacher':
				flash("Login successfully")
				return redirect(url_for('teacher.teacher_home'))

			elif res[0]['usertype']=='admin':
				flash("Login successfully")
				return redirect(url_for('admin.admin_home'))

			elif res[0]['usertype']=='student':
				q="select * from student where login_id='%s'"%(session['lid'])
				res=select(q)
				session['st_id']=res[0]['student_id']
				flash("Login successfully")
				return redirect(url_for('student.student_home'))

				
		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('login.html')

@public.route('/admin_login',methods=['get','post'])
def admin_login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']

			if res[0]['usertype']=='admin':
				flash("Login successfully")
				return redirect(url_for('admin.admin_home'))

		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('admin_login.html')

@public.route('/staff_login',methods=['get','post'])
def staff_login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']

			if res[0]['usertype']=='teacher':
				flash("Login successfully")
				return redirect(url_for('teacher.teacher_home'))

		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('staff_login.html')


@public.route('/student_login',methods=['get','post'])
def student_login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']

			if res[0]['usertype']=='student':
				flash("Login successfully")
				return redirect(url_for('student.student_home'))

		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('student_login.html')









