
from flask import redirect, render_template, request, url_for
from app import flaskApp
from app.model import Group, Student


tom = Student(uwaID = "17345678", name = "tom")	
rick = Student(uwaID = "22355678", name = "rick")	
ricardo = Student(uwaID = "32335678", name = "Ricardo")	
bob = Student(uwaID = "42349678", name = "bob")

group1 = Group(students = [tom, rick, ricardo, bob])

projectGroups = [group1]


@flaskApp.route('/')
@flaskApp.route('/groups')
def groups():
    return render_template('listGroups.html', groups = projectGroups)

@flaskApp.route('/create')
def create():
    return render_template('createGroup.html')

@flaskApp.route('/submit', methods=['post'])
def submit():
    print(request.method)
    print(request.form['numberOfStudents'])
    print("submitting group")
    return redirect(location=url_for('groups'))
