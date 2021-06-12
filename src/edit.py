# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    edit
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/4/26 16:24
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------
from flask import Flask,session,render_template,Blueprint,request
import mysql.connector
import json,datetime
from config import *
import traceback

edit_bp = Blueprint('edit',__name__,url_prefix='/edit')

#edit
@edit_bp.route('/addStudent',methods=['POST'])
def edit_addStudent():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    CollegeNo=0
    data = json.loads(request.get_data(as_text=True))

    #先查找学院号
    sql = "select CollegeNo from SpecialityInfo where SpecialityNo='%s'"% (data["addSpeciality"])
    try:
        cur.execute(sql)
        cur_res=cur.fetchall()
        if cur_res!=[]:
            CollegeNo = cur_res[0][0]
    except Exception as e:
        print(traceback.print_exc())

    sql = "INSERT INTO `StudentInfo`(StudentName,StudentGender,StudentBirthday,CollegeNo,SpecialityNo) VALUES ('%s', '%s', '%s', '%s', '%s');" %(data["addName"],data["addGender"],data["addBirthday"],CollegeNo,data["addSpeciality"])
    try:
        cur.execute(sql)
        sql = "select StudentNo from StudentInfo where  StudentName='%s' and StudentGender='%s' and StudentBirthday='%s' and CollegeNo=%s and SpecialityNo=%s;"%(data["addName"],data["addGender"],data["addBirthday"],CollegeNo,data["addSpeciality"])
        cur.execute(sql)
        cur_res=cur.fetchall()
        ID = cur_res[0][0]
        sql = "UPDATE StudentInfo set StudentPassword='%s' where StudentName='%s' and StudentGender='%s' and StudentBirthday='%s' and CollegeNo=%s and SpecialityNo=%s;"%(ID,data["addName"],data["addGender"],data["addBirthday"],CollegeNo,data["addSpeciality"])
        cur.execute(sql)
        mydb.commit()
        return '{"status":"200"}'
    except Exception as e:
        print(traceback.print_exc())
        return '{"status":"500"}'

@edit_bp.route('/addTeacher',methods=['POST'])
def edit_addTeacher():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    CollegeNo=0
    data = json.loads(request.get_data(as_text=True))

    #先查找学院号
    sql = "select CollegeNo from CollegeInfo where CollegeName='%s'"% (data["addCollege"])
    try:
        cur.execute(sql)
        cur_res=cur.fetchall()
        if cur_res!=[]:
            CollegeNo = cur_res[0][0]
    except Exception as e:
        print(traceback.print_exc())

    sql = "INSERT INTO `TeacherInfo`(TeacherName,TeacherGender,TeacherBirthday,TeaCollegeNo) VALUES ('%s', '%s', '%s', '%s');" %(data["addName"],data["addGender"],data["addBirthday"],CollegeNo)
    try:
        cur.execute(sql)
        sql = "select TeacherNo from TeacherInfo where  TeacherName='%s' and TeacherGender='%s' and TeacherBirthday='%s' and TeaCollegeNo=%s;" % (
        data["addName"], data["addGender"], data["addBirthday"], CollegeNo)
        cur.execute(sql)
        cur_res = cur.fetchall()
        ID = cur_res[0][0]
        sql = "UPDATE TeacherInfo set TeacherPassword='%s' where TeacherName='%s' and TeacherGender='%s' and TeacherBirthday='%s' and TeaCollegeNo=%s;" % (
        ID, data["addName"], data["addGender"], data["addBirthday"], CollegeNo)
        cur.execute(sql)
        mydb.commit()
        return '{"status":"200"}'
    except Exception as e:
        print(traceback.print_exc())
        return '{"status":"500"}'

@edit_bp.route('/addAdmin',methods=['POST'])
def edit_addAdmin():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))

    sql = "INSERT INTO `AdminInfo`(AdminName,AdminGender,AdminBirthday) VALUES ('%s', '%s', '%s');" %(data["addName"],data["addGender"],data["addBirthday"])
    try:
        cur.execute(sql)
        sql = "select AdminNo from AdminInfo where  AdminName='%s' and AdminGender='%s' and AdminBirthday='%s';" % (
            data["addName"], data["addGender"], data["addBirthday"])
        cur.execute(sql)
        cur_res = cur.fetchall()
        ID = cur_res[0][0]
        sql = "UPDATE AdminInfo set AdminPassword='%s' where  AdminName='%s' and AdminGender='%s' and AdminBirthday='%s';" % (
            ID,data["addName"], data["addGender"], data["addBirthday"])
        cur.execute(sql)
        mydb.commit()
        return '{"status":"200"}'
    except Exception as e:
        print(traceback.print_exc())
        return '{"status":"500"}'

@edit_bp.route('/editPassword',methods=['POST'])
def edit_editPassword():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))

    if(session["password"]!=data["oldPassword"]):
        return {'status' : False, 'reason':'wrong oldPassword'}

    if(len(data["newPassword"])<6):
        return {'status': False, 'reason': 'short newPassword'}
    sql = ""

    if(session["identity"]=="student"):
        sql = " update %s set %s = '%s' where %s = '%s';" %("StudentInfo","StudentPassword",data["newPassword"],"StudentNo",session["No"])
    elif(session["identity"]=="teacher"):
        sql = " update %s set %s = '%s' where %s = '%s';" %("TeacherInfo","TeacherPassword",data["newPassword"],"TeacherNo",session["No"])
    else:
        sql = " update %s set %s = '%s' where %s = '%s';" %("AdminInfo","AdminPassword",data["newPassword"],"AdminNo",session["No"])
    try:
        cur.execute(sql)
        mydb.commit()
        session["password"] = data["newPassword"]
        return {'status': True}
    except Exception as e:
        print(traceback.print_exc())
        return {'status': False,'reason':'mysql wrong'}

#处理任课申请
@edit_bp.route('/HandleTeachApplication',methods=['GET','POST'])
def edit_HandleTeachApplication():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))

    if(data["choice"]=="disagree"):
        sql = "update TeachCourseApplication set Status='dismissed' where TeacherNo=%s and CourseNo=%s;" % (data["teacherID"],data["courseID"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(data["choice"]=="agree"):
        sql = "update TeachCourseApplication set Status='passed' where TeacherNo=%s and CourseNo=%s;" % (data["teacherID"], data["courseID"])
        cur.execute(sql)
        sql = "update CourseInfo set TeacherNo=%s where CourseNo=%s;" %(data["teacherID"],data["courseID"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(data["choice"]=="cancel"):
        sql = "delete from TeachCourseApplication where TeacherNo=%s and CourseNo=%s;" % (session["No"],data["courseID"])
        cur.execute(sql)
        sql = "alter table TeachCourseApplication auto_increment=1"
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(data["choice"]=="submit"):
        sql = "insert into TeachCourseApplication values(%s,%s,'%s','waiting');" % (session["No"], data["courseID"],data["reason"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    else:
        return {'status':False}

#处理开课申请
@edit_bp.route('/HandleStartApplication',methods=['GET','POST'])
def edit_HandleStartApplication():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))

    if(data["choice"]=="disagree"):
        sql = "update StartCourseApplication set Status='dismissed' where TeacherNo=%s and CourseName='%s';" % (data["teacherID"],data["courseName"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(data['choice']=="agree"):
        sql = "update StartCourseApplication set Status='passed' where TeacherNo=%s and CourseName='%s';" % (data["teacherID"], data["courseName"])
        cur.execute(sql)
        sql = "insert into CourseInfo (CourseName,TeacherNo,CourseDay,CourseBeginNo,CourseNums,ClassroomNo) values ('%s',%s,'%s',%s,%s,%s);" %(data["courseName"],data["teacherID"],data["courseDay"],data["courseBeginNo"],data["courseNums"],data["classroomNo"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(data['choice']=="cancel"):
        sql = "delete from StartCourseApplication where TeacherNo=%s and CourseName='%s';" % (session["No"], data["courseName"])
        cur.execute(sql)
        sql = "alter table StartCourseApplication auto_increment=1"
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif (data["choice"] == "submit"):
        sql = "insert into StartCourseApplication values(%s,'%s','%s','waiting');" % (
        session["No"], data["courseName"], data["reason"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    else:
        return {'status': False}

#增加考试
@edit_bp.route('/addExam',methods=['GET','POST'])
def edit_addExam():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))

    sql = "select * from ExamInfo where CourseNo=%s;" % (data["addCourseNo"])
    cur.execute(sql)
    cur_res = cur.fetchall()
    if cur_res != []:
        return {'status': False,'reason':'repeated Course'}

#成功
    sql = "insert into ExamInfo values(%s,'%s','%s','%s',%s,%s)" %(data["addCourseNo"],data["addDay"],data["addBeginTime"],data["addEndTime"],data["addClassroomNo"],data["addTeacherNo"])
    cur.execute(sql)
    mydb.commit()
    return {'status': True}

#删除个人课程表项
@edit_bp.route('/delStudentCurriculum',methods=['GET','POST'])
def edit_delStudentCurriculum():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    data = json.loads(request.get_data(as_text=True))
    sql = "delete from StudentCurriculum where StudentNo=%s and CourseNo=%s;" % (session['No'],data["courseID"])
    cur.execute(sql)
    sql = "alter table StudentCurriculum auto_increment=1"
    cur.execute(sql)
    mydb.commit();
    return {'status': True}

#添加个人课程表项
@edit_bp.route('/addStudentCurriculum',methods=['GET','POST'])
def edit_addStudentCurriculum():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    data = json.loads(request.get_data(as_text=True))

    #检测时间冲突
    #遍历个人课程，分别比对已有课程与新增课程是否冲突
    sql = "select CourseDay,CourseBeginNo,CourseNums from CourseInfo where CourseInfo.CourseNo in (select CourseNo from StudentCurriculum where StudentCurriculum.StudentNo=%s) ;" % (session["No"])
    cur.execute(sql)
    cur_res = cur.fetchall()
    sql = "select CourseDay,CourseBeginNo,CourseNums from CourseInfo where CourseInfo.CourseNo=%s;" %(data["addCourseNo"])
    cur.execute(sql)
    add_res = cur.fetchall()
    add_res = add_res[0]
    if cur_res != []:
        for res in cur_res:
            if(res[0]==add_res[0]):
                if(int(res[1])>int(add_res[1])):
                    if(int(res[1])<=(int(add_res[1])+int(add_res[2])-1)):
                        return {'status': False, 'reason': 'repeated time'}
                elif(int(add_res[1])<=(int(res[1])+int(res[2])-1)):
                    return {'status': False, 'reason': 'repeated time'}

    sql = "insert into StudentCurriculum values(%s,%s);" % (session['No'],data["addCourseNo"])
    cur.execute(sql)
    mydb.commit();
    return {'status': True}

#添加教学评价
@edit_bp.route('/addEvaluation',methods=['GET','POST'])
def edit_addEvaluation():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    data = json.loads(request.get_data(as_text=True))

    if(session["identity"]=="student"):
        sql = "insert into EvaluationInfo(CourseNo,TeacherNo,StuContent,StudentNo) values(%s,%s,'%s',%s);" % (data["addCourseNo"],data["addTeacherNo"],data["addEva"],session["No"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}
    elif(session["identity"]=="teacher"):
        sql = "insert into EvaluationInfo(CourseNo,TeacherNo,TeaContent) values(%s,%s,'%s');" % (
        data["addCourseNo"], session["No"], data["addEva"])
        cur.execute(sql)
        mydb.commit()
        return {'status': True}

    return {'status':False}

#添加成绩
@edit_bp.route('/addScore',methods=['GET','POST'])
def edit_addScore():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    data = json.loads(request.get_data(as_text=True))

    sql = "select * from ScoreInfo where StudentNo=%s and CourseNo=%s"%(data["studentID"],data["courseID"])
    cur.execute(sql)
    cur_res = cur.fetchall()
    if(cur_res==[]):
        sql = "insert into ScoreInfo values(%s,%s,'%s');" % (data["courseID"],data["studentID"],data["score"])
        cur.execute(sql)
        mydb.commit();
        return {'status': True}
    else :
        sql = "update ScoreInfo set Score='%s' where StudentNo=%s and CourseNo=%s"%(data['score'],data["studentID"],data["courseID"])
        cur.execute(sql)
        mydb.commit();
        return {'status': True}
