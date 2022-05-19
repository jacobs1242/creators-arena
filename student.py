from public import *
import uuid

student=Blueprint('student',__name__)

@student.route('/student_home')
def student_home():
	return render_template('student_home.html')
	



@student.route('/student_send_complaint',methods=['get','post'])
def student_send_complaint():
	data={}
	sid=session['st_id']

	if 'submit' in request.form:
		
		complaint=request.form['Complaint']
		q="INSERT INTO `complaints`VALUES(null,'%s','%s','pending',NOW())"%(sid,complaint)
		insert(q)

		flash("success...")

		return redirect(url_for('student.student_send_complaint'))

	q="SELECT * FROM `complaints` WHERE `student_id`='%s'"%(sid)
	res=select(q)
	data['complaints']=res
	return render_template('student_send_complaint.html',data=data)



@student.route('/student_view_notification',methods=['get','post'])
def student_view_notification():
	data={}

	q="select * from notifications"
	res=select(q)
	if res:
		data['not']=res
		print(res)
	return render_template("student_view_notification.html",data=data)


@student.route('/student_view_profile',methods=['get','post'])
def student_view_profile():
	data={}
	sid=session['st_id']
	q="select * from student where student_id='%s'"%(sid)
	res=select(q)
	if res:
		data['stud']=res
		print(res)
	return render_template("student_view_profile.html",data=data)



@student.route('/student_edit_profile',methods=['get','post'])
def student_edit_profile():
	data={}
	sid=session['st_id']
	q="select * from student where student_id='%s'"%(sid)
	res=select(q)
	if res:
		data['dir']=res
		print(res)

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		cs=request.form['cs']
		dept=request.form['dept']
		phone=request.form['ph']
		email=request.form['em']
		q="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s',course='%s',department='%s' where student_id='%s'"%(fn,ln,pl,phone,email,cs,dept,sid)
		update(q)
		flash("updated")
		print(q)
		return redirect(url_for('student.student_view_profile'))
	return render_template("student_edit_profile.html",data=data)




@student.route('/student_view_category',methods=['get','post'])
def student_view_category():
	data={}
	sid=session['st_id']
	q="select * from category"
	res=select(q)
	if res:
		data['cat']=res
		print(res)
	return render_template("student_view_category.html",data=data)



@student.route('/student_manage_talent',methods=['get','post'])
def student_manage_talent():
	data={}
	id=request.args['id']
	sid=session['st_id']

	if 'manage' in request.form:
		title=request.form['title']
		des=request.form['des']
		img=request.files['img']
		path='static/'+str(uuid.uuid4())+img.filename
		img.save(path)
		q="insert into talents values(NULL,'%s','%s','%s','%s','%s','pending')"%(sid,id,title,des,path)
		insert(q)
		flash("Added Successfully...!")
		return redirect(url_for('student.student_manage_talent',id=id))

	q="select * from talents"
	res=select(q)
	if res:
		data['talent']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete from talents where talent_id='%s'"%(id)
		delete(q)
		flash("deleted.....!")
		return redirect(url_for('student.student_manage_talent',id=id))
	return render_template("student_manage_talent.html",data=data)



@student.route('/student_view_other_talents',methods=['get','post'])
def student_view_other_talents():
	data={}
	sid=session['st_id']

	q="select * from talents inner join student using(student_id) where student_id!='%s'"%(sid)
	res=select(q)
	if res:
		data['stud']=res
		print(res)
	return render_template("student_view_other_talents.html",data=data)




@student.route('/student_view_comments',methods=['get','post'])
def student_view_comments():
	data={}
	

	id=request.args['id']
	q="select * from comments where talent_id='%s'"%(id)
	res=select(q)
	if res:
		data['com']=res
		print(res)

	return render_template("student_view_comments.html",data=data)


@student.route('/student_manage_comments',methods=['get','post'])
def student_manage_comments():
	data={}
	id=request.args['id']
	sid=session['st_id']

	if 'manage' in request.form:
		com=request.form['com']
		q="insert into comments values(NULL,'%s','%s','%s',curdate())"%(id,sid,com)
		insert(q)
		flash("Add Successfully...!")
		return redirect(url_for('student.student_manage_comments',id=id))

	q="select * from comments"
	res=select(q)
	if res:
		data['com']=res
		print(res)
	return render_template("student_manage_comments.html",data=data)