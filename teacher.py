from public import *
import uuid

teacher=Blueprint('teacher',__name__)

@teacher.route('/teacher_home')
def teacher_home():
	return render_template('teacher_home.html')




@teacher.route('/teacher_manage_students',methods=['get','post'])
def teacher_manage_students():
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
			q="insert into login values(NULL,'%s','%s','student')"%(uname,password)
			lid=insert(q)
			q="insert into student values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,cs,dept,phone,email)
			insert(q)
			flash("Registered Successfully...!")
		return redirect(url_for('teacher.teacher_manage_students'))

	q="select * from student"
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
		q="delete from student where login_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		flash("deleted.....!")
		return redirect(url_for('teacher.teacher_manage_students'))

	if action=='update':
		q="select * from student where login_id='%s'"%(id)
		data['dir']=select(q)

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		cs=request.form['cs']
		dept=request.form['dept']
		phone=request.form['ph']
		email=request.form['em']
		q="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s',course='%s',department='%s' where login_id='%s'"%(fn,ln,pl,phone,email,cs,dept,id)
		update(q)
		flash("updated")
		return redirect(url_for('teacher.teacher_manage_students'))
	return render_template("teacher_manage_students.html",data=data)




@teacher.route('/teacher_manage_category',methods=['get','post'])
def teacher_manage_category():
	data={}
	if 'manage' in request.form:
		cat=request.form['cat']
		q="select * from category where category_id='%s' "%(cat)
		res=select(q)
		if res:
			flash('THIS CATEGORY  ALREADY EXISTS')
		else:
			q="insert into category values(NULL,'%s')"%(cat)
			insert(q)
			flash("Added Successfully")
		return redirect(url_for('teacher.teacher_manage_category'))

	q="select * from category"
	res=select(q)
	if res:
		data['sub']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete from category where category_id='%s'"%(id)
		delete(q)
		flash("Deleted Successfully")
		return redirect(url_for('teacher.teacher_manage_category'))

	if action=='update':
		q="select * from category where category_id='%s'"%(id)
		data['dir']=select(q)

	if 'update' in request.form:
		cat=request.form['cat']
		q="update category set title='%s' where category_id='%s'"%(cat,id)
		update(q)
		flash("Updated Successfully")
		return redirect(url_for('teacher.teacher_manage_category'))
	return render_template("teacher_manage_category.html",data=data)





@teacher.route('/teacher_send_notification',methods=['get','post'])
def teacher_send_notification():
	data={}
	if 'manage' in request.form:
		note=request.form['not']
		q="select * from notifications where notification_id='%s' "%(note)
		res=select(q)
		if res:
			flash('THIS NOTIFICATION  ALREADY EXISTS')
		else:
			q="insert into notifications values(NULL,'%s',curdate())"%(note)
			insert(q)
			flash("Send Successfully")
		return redirect(url_for('teacher.teacher_send_notification'))

	q="select * from notifications"
	res=select(q)
	if res:
		data['not']=res
		print(res)
	return render_template("teacher_send_notification.html",data=data)



@teacher.route('/teacher_view_complaints',methods=['get','post'])
def teacher_view_complaints():
	data={}
	q="SELECT *,CONCAT(`fname`,' ',`lname`) AS `name` FROM `complaints` INNER JOIN `student` using(student_id)"
	res=select(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		print('submit'+str(i))
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(reply)
			print(j)
			print(res[j]['complaint_id'])
			q="update complaints set reply='%s' where complaint_id='%s'" %(reply,res[j]['complaint_id'])
			print(q)
			update(q)
			flash("success")
			return redirect(url_for('teacher.teacher_view_complaints')) 	
		j=j+1
	return render_template('teacher_view_complaints.html',data=data)



@teacher.route('/teacher_view_talent',methods=['get','post'])
def teacher_view_talent():
	data={}
	q="select * from talents inner join student using(student_id)"
	res=select(q)
	if res:
		data['stud']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='verify':
		q="update talents set status='verify' where talent_id='%s'"%(id)
		update(q)
		flash("Approved")
		return redirect(url_for('teacher.teacher_view_talent'))

	if action=='reject':
		q="update talents set status='rejected' where talent_id='%s'"%(id)
		update(q)
		flash("Rejected")
		return redirect(url_for('teacher.teacher_view_talent'))
	return render_template("teacher_view_talent.html",data=data)



@teacher.route('/teacher_view_comments',methods=['get','post'])
def teacher_view_comments():
	data={}
	id=request.args['id']
	q="select * from comments where talent_id='%s'"%(id)
	res=select(q)
	if res:
		data['com']=res
		print(res)

	return render_template("teacher_view_comments.html",data=data)