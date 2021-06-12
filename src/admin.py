# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    admin
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/3/29 15:38
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------
from flask import Flask,session,render_template,Blueprint

admin_bp = Blueprint('admin',__name__,url_prefix='/admin')

@admin_bp.route('/admin_index',methods=['GET','POST'])
def admin_index():
    posts = {"AdminNo":session['No'],"AdminName":session['name']}
    return render_template('/admin/admin_index.html',posts=posts)

@admin_bp.route('/admin_stuff_addStudent',methods=['GET','POST'])
def admin_stuff_addStudent():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_stuff_addStudent.html', posts=posts)

@admin_bp.route('/admin_stuff_addTeacher',methods=['GET','POST'])
def admin_stuff_addTeacher():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_stuff_addTeacher.html', posts=posts)

@admin_bp.route('/admin_stuff_addAdmin',methods=['GET','POST'])
def admin_stuff_addAdmin():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_stuff_addAdmin.html', posts=posts)

@admin_bp.route('/admin_course_viewCourse',methods=['GET','POST'])
def admin_course_viewCourse():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_course_viewCourse.html', posts=posts)

@admin_bp.route('/admin_course_viewSpecialityCurriculum',methods=['GET','POST'])
def admin_course_viewSpecialityCurriculum():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_course_viewSpecialityCurriculum.html', posts=posts)

@admin_bp.route('/admin_course_teachApplication',methods=['GET','POST'])
def admin_course_teachApplication():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_course_teachApplication.html', posts=posts)

@admin_bp.route('/admin_course_startApplication',methods=['GET','POST'])
def admin_course_startApplication():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_course_startApplication.html', posts=posts)

@admin_bp.route('/admin_exam_editExam',methods=['GET','POST'])
def admin_exam_editExam():
    posts = {"AdminNo": session['No'], "AdminName": session['name']}
    return render_template('/admin/admin_exam_editExam.html', posts=posts)

