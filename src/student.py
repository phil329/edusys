# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    student
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/4/19 10:03
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------
from flask import Flask,session,render_template,Blueprint

student_bp = Blueprint('student',__name__,url_prefix='/student')


@student_bp.route('/student_index',methods=['GET','POST'])
def student_index():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_index.html', posts=posts)

@student_bp.route('/student_course_specialityCurriculum',methods=['GET','POST'])
def student_course_specialityCurriculum():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_course_specialityCurriculum.html', posts=posts)

@student_bp.route('/student_course_studentCurriculum',methods=['GET','POST'])
def student_course_studentCurriculum():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_course_studentCurriculum.html', posts=posts)

@student_bp.route('/student_course_selectCourse',methods=['GET','POST'])
def student_course_selectCourse():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_course_selectCourse.html', posts=posts)

@student_bp.route('/student_exam_viewExam',methods=['GET','POST'])
def student_exam_viewExam():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_exam_viewExam.html', posts=posts)

@student_bp.route('/student_score_viewScore',methods=['GET','POST'])
def student_score_viewScore():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_score_viewScore.html', posts=posts)

@student_bp.route('/student_evaluate_addEvaluation',methods=['GET','POST'])
def student_evaluate_addEvaluation():
    posts = {"StudentNo": session['No'], "StudentName": session['name']}
    return render_template('/student/student_evaluate_addEvaluation.html', posts=posts)


