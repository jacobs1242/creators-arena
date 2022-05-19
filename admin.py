from public import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')




@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
	data={}
	if 'manage' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		cs=request.form['cs']
		dept=request.form['dept']
		phone=request.form['ph']
		email=request.form['em']
		uname=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash('THIS USERNAME AND PASSWORD IS ALREADY EXIST')
		else:
			q="insert into login values(NULL,'%s','%s','teacher')"%(uname,password)
			lid=insert(q)
			q="insert into admin values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,cs,dept,phone,email)
			insert(q)
			flash("Registered Successfully")
		return redirect(url_for('admin.admin_manage_staff'))

	q="select * from admin"
	res=select(q)
	if res:
		data['stud']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete from admin where login_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		flash("deleted.....!")
		return redirect(url_for('admin.admin_manage_staff'))

	if action=='update':
		q="select * from admin where login_id='%s'"%(id)
		data['dir']=select(q)

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		cs=request.form['cs']
		dept=request.form['dept']
		phone=request.form['ph']
		email=request.form['em']
		q="update admin set fname='%s',lname='%s',place='%s',phone='%s',email='%s',course='%s',department='%s' where login_id='%s'"%(fn,ln,pl,phone,email,cs,dept,id)
		update(q)
		flash("updated")
		return redirect(url_for('admin.admin_manage_staff'))
	return render_template("admin_manage_staff.html",data=data)




