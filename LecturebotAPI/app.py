import os
import random

from flask import Flask, render_template, request, redirect

from LecturebotDAL.repository.dataservice import get_data,delete_data_build_num, update_data_b, insert_data,get_data_by_build_num, get_data_by_id, delete_data, save, update_data, req1, req2, req3,get_data_by_init, get_data_by_pass, delete_data_init, delete_data_pass
from LecturebotDAL.models.model import Student, CourseWork, Subject,  Teacher, House
from LecturebotAPI.forms.Student_form import Studform
from LecturebotAPI.forms.Student_coursework_form import CourseworkForm
from LecturebotAPI.forms.Teacher_form import TeacherForm
from LecturebotAPI.forms.Subject_form import Subj_form
from LecturebotAPI.forms.House_form import HouseForm
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Student', methods=['GET', 'POST'])
def forstudnt():
    result = get_data(Student)
    form = Studform()
    if request.method == 'POST':
        print(form.gradebook_number.data)
        students = get_data_by_id(Student, form.gradebook_number.data)
        if students is not None:
            if form.gradebook_number.data == students.gradebook_number:
                students = Student(int(form.gradebook_number.data),form.full_name.data, form.stgroup.data, form.year_of_receipt.data)
                update_data(students, Student)
            else:
                students = Student(form.gradebook_number.data, form.full_name.data, form.stgroup.data,form.year_of_receipt.data)
                insert_data(students)
        else:
            students = Student(form.gradebook_number.data, form.full_name.data, form.stgroup.data,form.year_of_receipt.data)
            insert_data(students)
        save()
        return redirect('/Student')
    return render_template('Student.html', students=result, form=form)


@app.route('/Student/delete/<gradebook_number>')
def user_delete(gradebook_number):
    delete_data(Student, gradebook_number)
    save()
    return redirect('/Student')


@app.route('/Student/edit/<gradebook_number>', methods=['GET'])
def student_edit(gradebook_number):
    if request.method == 'GET':
        students = get_data_by_id(Student, gradebook_number)
        result = get_data(Student)
        form = Studform()
        form.gradebook_number.data = students.gradebook_number
        form.full_name.data = students.full_name
        return render_template('Student.html', students=result, form=form)


@app.route('/Course_work', methods=['GET', 'POST'])
def forcoursework():
    result = get_data(CourseWork)
    form = CourseworkForm()
    if request.method == 'POST':
        print(form.initalization_num.data)
        works = get_data_by_init(CourseWork, form.initalization_num.data)
        if works is not None:
            if form.initalization_num.data == works.initalization_num:
                works = CourseWork(int(form.initalization_num.data),form.gradebook_number.data, form.cwname.data, form.research_direction.data, form.mark.data)
                update_data_cw(works, CourseWork)
            else:
                works = CourseWork(form.initalization_num.data,form.gradebook_number.data, form.cwname.data, form.research_direction.data, form.mark.data)
                insert_data(works)
        else:
            works = CourseWork(form.initalization_num.data,form.gradebook_number.data, form.cwname.data, form.research_direction.data, form.mark.data)
            insert_data(works)
        save()
        return redirect('/Course_work')
    return render_template('Course_work.html', works=result, form=form)


@app.route('/Course_work/delete/<initalization_num>')
def work_delete(initalization_num):
    delete_data_init(CourseWork, initalization_num)
    save()
    return redirect('/Course_work')


@app.route('/Course_work/edit/<initalization_num>', methods=['GET'])
def work_edit(initalization_num):
    if request.method == 'GET':
        works = get_data_by_init(CourseWork, initalization_num)
        result = get_data(CourseWork)
        form = CourseworkForm()
        form.initalization_num.data = works.initalization_num
        form.cwname.data = works.cwname
        return render_template('Course_work.html', works=result, form=form)


@app.route('/Teacher', methods=['GET', 'POST'])
def forteacher():
    result = get_data(Teacher)
    form = TeacherForm()
    if request.method == 'POST':
        print(form.pass_number.data)
        teachers = get_data_by_pass(Teacher, form.pass_number.data)
        if teachers is not None:
            if form.pass_number.data == teachers.pass_number:
                teachers = Teacher(int(form.pass_number.data), form.full_name.data, form.department.data)
                update_data_t(teachers, Teacher)
            else:
                teachers = Teacher(form.pass_number.data, form.full_name.data, form.department.data)
                insert_data(teachers)
        else:
            teachers = Teacher(form.pass_number.data, form.full_name.data, form.department.data)
            insert_data(teachers)
        save()
        return redirect('/Teacher')
    return render_template('Teacher.html', teachers=result, form=form)


@app.route('/Teacher/delete/<pass_number>')
def teach_delete(pass_number):
    delete_data_pass(Teacher, pass_number)
    save()
    return redirect('/Teacher')


@app.route('/Teacher/edit/<pass_number>', methods=['GET'])
def teach_edit(pass_number):
    if request.method == 'GET':
        teachers = get_data_by_pass(Teacher, pass_number)
        result = get_data(Teacher)
        form = TeacherForm()
        form.pass_number.data = teachers.pass_number
        form.full_name.data = teachers.full_name
        return render_template('Teacher.html', teachers=result, form=form)


@app.route('/Subjects', methods=['GET', 'POST'])
def forsubject():
    result = get_data(Subject)
    form = Subj_form()
    if request.method == 'POST':
        print(form.pass_num.data)
        subjects = get_data_by_passn(Subject, form.pass_num.data)
        if subjects is not None:
            if form.pass_num.data == subjects.pass_num:
                subjects = Subject(int(form.pass_num.data),form.sbname.data, form.student_rating.data, form.gradebook_number.data,form.pass_number.data)
                update_data_s(subjects, Subject)
            else:
                subjects = Subject(form.pass_num.data,form.sbname.data, form.student_rating.data, form.gradebook_number.data,form.pass_number.data)
                insert_data(subjects)
        else:
            subjects = Subject(form.pass_num.data,form.sbname.data, form.student_rating.data, form.gradebook_number.data,form.pass_number.data)
            insert_data(subjects)
        save()
        return redirect('/Subjects')
    return render_template('Subjects.html', subjects=result, form=form)


@app.route('/Subjects/delete/<pass_num>')
def subj_delete(pass_num):
    delete_data_passn(Subject, pass_num)
    save()
    return redirect('/Subjects')


@app.route('/Subjects/edit/<pass_num>', methods=['GET'])
def subj_edit(pass_num):
    if request.method == 'GET':
        subjects = get_data_by_passn(Subject, pass_num)
        result = get_data(Subject)
        form = Subj_form()
        form.pass_num.data = subjects.pass_num
        form.sbname.data = subjects.sbname
        return render_template('Subjects.html', subjects=result, form=form)
		
		
		
@app.route('/Dashboard', methods=['GET'])
def dashboard():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    resources = repository.get_all(Resource.Resource)

    repository = ServiceLocator.ServiceLocator(session, ModelBase, DBEngine)
    res_count = repository.get_count_of_resources_of_user().fetchall()

    urls = [str(resource.URL) for resource in resources]
    times = [int(resource.TimesVisited) for resource in resources]

    res = [str(resC[0]) for resC in res_count]
    count = [int(resC[1]) for resC in res_count]

    return render_template('dashboard.html', x1=urls, y1=times, x2=res, y2=count)


@app.route('/House', methods=['GET', 'POST'])
def forhouse():
    result = get_data(House)
    
    if request.method == 'POST':
        print(form.build_num.data)
        houses = get_data_by_build_num(House, form.build_num.data)
        if houses is not None:
            if form.build_num.data == houses.build_num:
                houses = House(int(form.build_num.data),form.adress.data, form.floors.data, form.years.data)
                update_data_b(houses, House)
            else:
                houses = House(form.build_num.data, form.adress.data, form.floors.data,form.years.data)
                insert_data(houses)
        else:
            houses = House(form.build_num.data, form.adress.data, form.floors.data,form.years.data)
            insert_data(houses)
        save()
        return redirect('/House')
    return render_template('House.html', houses=result, form=form)


@app.route('/House/delete/<build_num>')
def house_delete(build_num):
    delete_data_build_num(House, build_num)
    save()
    return redirect('/House')


@app.route('/House/edit/<build_num>', methods=['GET'])
def house_edit(build_num):
    if request.method == 'GET':
        houses = get_data_by_build_num(House, build_num)
        result = get_data(House)
        form = HouseForm()
        form.build_num.data = houses.build_num
        form.adress.data = houses.adress
        return render_template('House.html',  houses=result, form=form)
