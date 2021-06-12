# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    teacher
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/4/19 19:12
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------
from flask import Flask,session,render_template,Blueprint

teacher_bp = Blueprint('teacher',__name__,url_prefix='/teacher')


@teacher_bp.route('/teacher_index',methods=['GET','POST'])
def teacher_index():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_index.html', posts=posts)

@teacher_bp.route('/teacher_course_teachApplication',methods=['GET','POST'])
def teacher_course_teachApplication():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_course_teachApplication.html', posts=posts)

@teacher_bp.route('/teacher_course_startApplication',methods=['GET','POST'])
def teacher_course_startApplication():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_course_startApplication.html', posts=posts)

@teacher_bp.route('/teacher_course_teacherCurriculum',methods=['GET','POST'])
def teacher_course_teacherCurriculum():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_course_teacherCurriculum.html', posts=posts)

@teacher_bp.route('/teacher_course_classStudent',methods=['GET','POST'])
def teacher_course_classStudent():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_course_classStudent.html', posts=posts)

@teacher_bp.route('/teacher_exam_monitorInfo',methods=['GET','POST'])
def teacher_exam_monitorInfo():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_exam_monitorInfo.html', posts=posts)

@teacher_bp.route('/teacher_exam_classExam',methods=['GET','POST'])
def teacher_exam_classExam():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_exam_classExam.html', posts=posts)

@teacher_bp.route('/teacher_score_addScore',methods=['GET','POST'])
def teacher_score_addScore():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_score_addScore.html', posts=posts)

@teacher_bp.route('/teacher_assistant_choose',methods=['GET','POST'])
def teacher_assistant_choose():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_assistant_choose.html', posts=posts)

@teacher_bp.route('/teacher_evaluate_addEvaluation',methods=['GET','POST'])
def teacher_evaluate_addEvaluation():
    posts = {"TeacherNo": session['No'], "TeacherName": session['name']}
    return render_template('/teacher/teacher_evaluate_addEvaluation.html', posts=posts)


