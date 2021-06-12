# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    data_get
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/4/24 16:33
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------
from flask import Flask,session,Blueprint,request,flash
import mysql.connector
import json
from utils import *
from config import *
import traceback

data_bp = Blueprint('data',__name__,url_prefix='/data')

#get
@data_bp.route('/TeacherInfo',methods=['GET','POST'])
def getData_TeacherInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select TeacherNo,TeacherName,TeacherGender,TeacherBirthday,CollegeName from TeacherInfo,CollegeInfo where TeacherInfo.TeaCollegeNo=CollegeInfo.CollegeNo"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"No": res[0], "name": res[1], "gender": res[2], "birthday": res[3].isoformat(),
                            "collegeName": res[4]}
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取学生信息
@data_bp.route('/StudentInfo',methods=['GET','POST'])
def getData_StudentInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    if (session["identity"]=="admin"):
        sql = "select StudentNo,StudentName,StudentGender,StudentBirthday,CollegeName,SpecialityName from StudentInfo,CollegeInfo,SpecialityInfo where StudentInfo.CollegeNo=CollegeInfo.CollegeNo and StudentInfo.SpecialityNo=SpecialityInfo.SpecialityNo"
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            if cur_res != []:
                data = {}
                data['total'] = len(cur_res)
                data['rows'] = []
                for res in cur_res:
                    cur_data = {"No": res[0], "name": res[1], "gender": res[2], "birthday": res[3].isoformat(),
                                "collegeName": res[4], "specialityName": res[5]}
                    data['rows'].append(cur_data)
                data = json.dumps(data)
                return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    else:
        if(request.form["courseNo"]==""):
            return {}
        else:
            sql = "select StudentNo,StudentName,StudentGender,StudentBirthday,CollegeName,SpecialityName from CollegeInfo,SpecialityInfo,StudentInfo where StudentInfo.StudentNo in (select StudentNo from StudentCurriculum SC where SC.CourseNo=%s) and StudentInfo.CollegeNo=CollegeInfo.CollegeNo and StudentInfo.SpecialityNo=SpecialityInfo.SpecialityNo" % (request.form["courseNo"])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                if cur_res != []:
                    data = {}
                    data['total'] = len(cur_res)
                    data['rows'] = []
                    for res in cur_res:
                        cur_data = {"No": res[0], "name": res[1], "gender": res[2], "birthday": res[3].isoformat(),
                                    "collegeName": res[4], "specialityName": res[5]}
                        data['rows'].append(cur_data)
                    data = json.dumps(data)
                    return data
            except Exception as e:
                print(traceback.print_exc())
                flash(traceback.print_exc())
                return None

#获取管理员信息
@data_bp.route('/AdminInfo',methods=['GET','POST'])
def getData_AdminInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select AdminNo,AdminName,AdminGender,AdminBirthday from AdminInfo"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"No": res[0], "name": res[1], "gender": res[2], "birthday": res[3].isoformat()}
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取学院与专业
@data_bp.route('/CollegeSpeciality',methods=['GET','POST'])
def getData_CollegeSpeciality():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select CollegeName,SpecialityName,SpecialityNo from SpecialityInfo,CollegeInfo where SpecialityInfo.CollegeNo=CollegeInfo.CollegeNo;"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = []
            sameCol = {}
            for res in cur_res:
                if "ColName" in sameCol:
                    if sameCol["ColName"] == res[0]:
                        sameCol["SpeName"].append([res[1],res[2]])
                    else:
                        data.append(dict(sameCol))
                        sameCol["ColName"] = res[0]
                        sameCol["SpeName"] = [[res[1],res[2]]]
                else:
                    sameCol["ColName"] = res[0]
                    sameCol["SpeName"] = [[res[1],res[2]]]
            data.append(dict(sameCol))
            data = json.dumps(data)
            return data
        else:
            print("cur_res == []")
            return None
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取课程信息
@data_bp.route('/CourseInfo',methods=['GET','POST'])
def getData_CourseInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select CourseNo,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.TeacherNo=TeacherInfo.TeacherNo and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "teacherName": res[2],"classroom": res[6]}
                cur_data["time"] = cur_courseTime([res[3],res[4],res[5]])
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取任课课程信息
@data_bp.route('/TeachCourseInfo',methods=['GET','POST'])
def getData_TeachCourseInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select CourseNo,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.TeacherNo=%s and CourseInfo.TeacherNo=TeacherInfo.TeacherNo and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"%(session["No"])
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "teacherName": res[2],"classroom": res[6]}
                cur_data["time"] = cur_courseTime([res[3],res[4],res[5]])
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None


#获取专业课表
@data_bp.route('/SpecialityCurriculum',methods=['GET','POST'])
def getData_SpecialityCurriculum():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select SpecialityName,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from SpecialityCurriculum,CourseInfo,TeacherInfo,ClassroomInfo,SpecialityInfo where SpecialityCurriculum.SpecialityNo=SpecialityInfo.SpecialityNo and SpecialityCurriculum.CourseNo=CourseInfo.CourseNo and CourseInfo.TeacherNo=TeacherInfo.TeacherNo and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        data = {}
        data['total'] = len(cur_res)
        data['rows'] = []
        for res in cur_res:
            cur_data = {"specialityName": res[0], "courseName": res[1], "teacherName": res[2],"classroom": res[6]}
            cur_data["time"] = cur_courseTime([res[3],res[4],res[5]])
            data['rows'].append(cur_data)
        data = json.dumps(data)
        return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取专业课表，显示课程表
@data_bp.route('/SpecialityCurriculum_display',methods=['GET','POST'])
def getData_SpecialityCurriculum_display():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    sql = "select CourseNo,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.CourseNo in (select CourseNo from SpecialityCurriculum where SpecialityCurriculum.SpecialityNo = %s) and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo and CourseInfo.TeacherNo=TeacherInfo.TeacherNo;"%(session["speciality"])
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        data = {}
        data['total'] = len(cur_res)
        data['rows'] = [{'ClassNo':"第一节课"},{'ClassNo':"第二节课"},{'ClassNo':"第三节课"},{'ClassNo':"第四节课"},{'ClassNo':"第五节课"},{'ClassNo':"第六节课"},{'ClassNo':"第七节课"},{'ClassNo':"第八节课"},{'ClassNo':"第九节课"},{'ClassNo':"第十节课"}]
        week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for res in cur_res:
            cur_data = res[1]+'-'+res[2]+'\n('+res[6]+')'
            courseBeginNo = int(res[4])
            courseDay = week[int(res[3])-1]
            for i in range(res[5]):
                data['rows'][courseBeginNo+i-1][courseDay]=cur_data
        data = json.dumps(data)
        return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取个人课表
@data_bp.route('/StudentCurriculum',methods=['GET','POST'])
def getData_StudentCurriculum():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select CourseNo,CourseName,TeacherInfo.TeacherNo,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.CourseNo in (select CourseNo from StudentCurriculum where StudentCurriculum.StudentNo=%s) and CourseInfo.TeacherNo=TeacherInfo.TeacherNo and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"%(session["No"])
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1],"teacherID":res[2], "teacherName": res[3], "classroom": res[7]}
                cur_data["time"] = cur_courseTime([res[4], res[5], res[6]])
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取个人课表，显示课程表
@data_bp.route('/StudentCurriculum_display',methods=['GET','POST'])
def getData_StudentCurriculum_display():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    sql = "select CourseNo,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.CourseNo in (select CourseNo from StudentCurriculum where StudentCurriculum.StudentNo = %s) and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo and CourseInfo.TeacherNo=TeacherInfo.TeacherNo;"%(session["No"])
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        data = {}
        data['total'] = len(cur_res)
        data['rows'] = [{'ClassNo':"第一节课"},{'ClassNo':"第二节课"},{'ClassNo':"第三节课"},{'ClassNo':"第四节课"},{'ClassNo':"第五节课"},{'ClassNo':"第六节课"},{'ClassNo':"第七节课"},{'ClassNo':"第八节课"},{'ClassNo':"第九节课"},{'ClassNo':"第十节课"}]
        week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for res in cur_res:
            cur_data = res[1]+'-'+res[2]+'\n('+res[6]+')'
            courseBeginNo = int(res[4])
            courseDay = week[int(res[3])-1]
            for i in range(res[5]):
                data['rows'][courseBeginNo+i-1][courseDay]=cur_data
        data = json.dumps(data)
        return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取教师课表，显示课程表
@data_bp.route('/TeacherCurriculum_display',methods=['GET','POST'])
def getData_TeacherCurriculum_display():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    sql = "select CourseNo,CourseName,TeacherName,CourseDay,CourseBeginNo,CourseNums,ClassroomPosition from CourseInfo,TeacherInfo,ClassroomInfo where CourseInfo.TeacherNo=%s and CourseInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"%(session["No"])
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        data = {}
        data['total'] = len(cur_res)
        data['rows'] = [{'ClassNo':"第一节课"},{'ClassNo':"第二节课"},{'ClassNo':"第三节课"},{'ClassNo':"第四节课"},{'ClassNo':"第五节课"},{'ClassNo':"第六节课"},{'ClassNo':"第七节课"},{'ClassNo':"第八节课"},{'ClassNo':"第九节课"},{'ClassNo':"第十节课"}]
        week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for res in cur_res:
            cur_data = res[1]+'-'+res[2]+'\n('+res[6]+')'
            courseBeginNo = int(res[4])
            courseDay = week[int(res[3])-1]
            for i in range(res[5]):
                data['rows'][courseBeginNo+i-1][courseDay]=cur_data
        data = json.dumps(data)
        return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取任课申请
@data_bp.route('/TeachApplication',methods=['GET','POST'])
def getData_TeachApplication():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    if(session["identity"]=="admin"):
        sql = "select TeachCourseApplication.TeacherNo,TeacherName,TeachCourseApplication.CourseNo,CourseName,Reason from CourseInfo,TeacherInfo,TeachCourseApplication where TeachCourseApplication.TeacherNo=TeacherInfo.TeacherNo and TeachCourseApplication.CourseNo=CourseInfo.CourseNo and TeachCourseApplication.Status='waiting';"
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"teacherID": res[0], "teacherName": res[1], "courseID": res[2],"courseName": res[3],"reason":res[4]}
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    else:
        sql = "select TeachCourseApplication.CourseNo,CourseName,Reason,Status from CourseInfo,TeachCourseApplication where TeachCourseApplication.TeacherNo = %s and TeachCourseApplication.CourseNo=CourseInfo.CourseNo;"%(session["No"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []

            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1],"reason": res[2]}
                if(res[3]=="waiting"):
                    cur_data["status"]="等待审核"
                elif(res[3]=="dismissed"):
                    cur_data["status"]="驳回"
                elif(res[3]=="passed"):
                    cur_data["status"] = "通过"
                else:
                    cur_data["status"] = "未知"
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None

#获取开课申请
@data_bp.route('/StartApplication',methods=['GET','POST'])
def getData_StartApplication():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    if(session["identity"]=="admin"):
        sql = "select StartCourseApplication.TeacherNo,TeacherName,CourseName,Reason from TeacherInfo,StartCourseApplication where StartCourseApplication.TeacherNo=TeacherInfo.TeacherNo and StartCourseApplication.Status='waiting';"
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []
            for res in cur_res:
                cur_data = {"teacherID": res[0], "teacherName": res[1], "courseName": res[2],"reason":res[3]}
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    else:
        sql = "select CourseName,Reason,Status from StartCourseApplication where StartCourseApplication.TeacherNo = %s ;" % (session["No"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = {}
            data['total'] = len(cur_res)
            data['rows'] = []

            for res in cur_res:
                cur_data = {"courseName": res[0], "reason": res[1]}
                if (res[2] == "waiting"):
                    cur_data["status"] = "等待审核"
                elif (res[2] == "dismissed"):
                    cur_data["status"] = "驳回"
                elif (res[2] == "passed"):
                    cur_data["status"] = "通过"
                else:
                    cur_data["status"] = "未知"
                data['rows'].append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None

#获取教室信息
@data_bp.route('/ClassroomInfo',methods=['GET','POST'])
def getData_ClassroomInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()
    sql = "select ClassroomNo,ClassroomPosition from ClassroomInfo;"
    try:
        cur.execute(sql)
        cur_res = cur.fetchall()
        if cur_res != []:
            data = []
            for res in cur_res:
                cur_data = {"No": res[0], "position": res[1]}
                data.append(cur_data)
            data = json.dumps(data)
            return data
    except Exception as e:
        print(traceback.print_exc())
        flash(traceback.print_exc())
        return None

#获取考试信息
@data_bp.route('/ExamInfo',methods=['GET','POST'])
def getData_ExamInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    if session["identity"]=="admin":
        sql = "select ExamInfo.CourseNo,CourseName,ExamDay,ExamBeginTime,ExamEndTime,TeacherName,ClassroomPosition from ExamInfo,CourseInfo,TeacherInfo,ClassroomInfo where ExamInfo.CourseNo=CourseInfo.CourseNo and ExamInfo.TeacherNo=TeacherInfo.TeacherNo and ExamInfo.ClassroomNo=ClassroomInfo.ClassroomNo;"
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "teacherName":res[5],"classroomPosition":res[6]}
                cur_data["examTime"] = cur_examTime([res[2],res[3],res[4]])
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    elif session["identity"]=="student":
        sql = "select ExamInfo.CourseNo,CourseName,ExamDay,ExamBeginTime,ExamEndTime,TeacherName,ClassroomPosition from ExamInfo,CourseInfo,TeacherInfo,ClassroomInfo where ExamInfo.CourseNo in (select CourseNo from StudentCurriculum where StudentNo=%s) and ExamInfo.TeacherNo=TeacherInfo.TeacherNo and ExamInfo.ClassroomNo=ClassroomInfo.ClassroomNo and ExamInfo.CourseNo=CourseInfo.CourseNo;"%(session["No"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "teacherName": res[5],
                            "classroomPosition": res[6]}
                cur_data["examTime"] = cur_examTime([res[2], res[3], res[4]])
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    elif session["identity"]=="teacher":
        if(request.form["choice"]=="monitor"):
            sql = "select ExamInfo.CourseNo,CourseName,ExamDay,ExamBeginTime,ExamEndTime,ClassroomPosition from ExamInfo,CourseInfo,ClassroomInfo where ExamInfo.TeacherNo=%s and ExamInfo.ClassroomNo=ClassroomInfo.ClassroomNo and ExamInfo.CourseNo=CourseInfo.CourseNo;"%(session["No"])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                data = []
                for res in cur_res:
                    cur_data = {"courseID": res[0], "courseName": res[1], "teacherName": session['name'],
                                "classroomPosition": res[5]}
                    cur_data["examTime"] = cur_examTime([res[2], res[3], res[4]])
                    data.append(cur_data)
                data = json.dumps(data)
                return data
            except Exception as e:
                print(traceback.print_exc())
                flash(traceback.print_exc())
                return None
        elif(request.form["choice"]=="class"):
            sql = "select ExamInfo.CourseNo,CourseName,ExamDay,ExamBeginTime,ExamEndTime,ClassroomPosition from ExamInfo,CourseInfo,ClassroomInfo where CourseInfo.TeacherNo=%s and ExamInfo.ClassroomNo=ClassroomInfo.ClassroomNo and ExamInfo.CourseNo=CourseInfo.CourseNo;"%(session["No"])
            try:
                cur.execute(sql)
                cur_res = cur.fetchall()
                data = []
                for res in cur_res:
                    cur_data = {"courseID": res[0], "courseName": res[1], "teacherName": session['name'],
                                "classroomPosition": res[5]}
                    cur_data["examTime"] = cur_examTime([res[2], res[3], res[4]])
                    data.append(cur_data)
                data = json.dumps(data)
                return data
            except Exception as e:
                print(traceback.print_exc())
                flash(traceback.print_exc())
                return None
        else:
            return {'status':False,'reason':'wrong choice'}

#获取成绩信息
@data_bp.route('/ScoreInfo',methods=['GET','POST'])
def getData_ScoreInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    if session["identity"]=="student":
        sql = "select ScoreInfo.CourseNo,CourseName,Score from CourseInfo,ScoreInfo where ScoreInfo.StudentNo=%s and ScoreInfo.CourseNo=CourseInfo.CourseNo;" % (session["No"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "score": res[2]}
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    elif session["identity"]=="teacher":
        if(request.form["courseNo"]==""):
            return {}
        sql = "select SC.StudentNo,StudentName,Score from ScoreInfo right join (select StudentInfo.StudentNo,StudentName from StudentCurriculum,StudentInfo where StudentCurriculum.CourseNo=%s and StudentCurriculum.StudentNo=StudentInfo.StudentNo) SC on ScoreInfo.CourseNo=%s and ScoreInfo.StudentNo=SC.StudentNo"%(request.form["courseNo"],request.form["courseNo"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"No": res[0], "name": res[1], "score": res[2]}
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None

#获取教学评价信息
@data_bp.route('/EvaluationInfo',methods=['GET','POST'])
def getData_EvaluationInfo():
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
    cur = mydb.cursor()

    if session["identity"]=="student":
        sql = " select E.CourseNo,CourseName,E.TeacherNo,TeacherName,StuContent from (select CourseNo,TeacherNo,StuContent from EvaluationInfo where StudentNo=%s) E,TeacherInfo,CourseInfo where E.CourseNo=CourseInfo.CourseNo and E.TeacherNo=TeacherInfo.TeacherNo;" %(session["No"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "teacherID": res[2],"teacherName":res[3],"content":res[4]}
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
    elif session["identity"]=="teacher":
        if(request.form["courseNo"]==""):
            return {}
        sql = "select E.CourseNo,CourseName,StuContent from (select CourseNo,StuContent from EvaluationInfo where CourseNo=%s and TeaContent is null) E,CourseInfo where E.CourseNo=CourseInfo.CourseNo;" %(request.form["courseNo"])
        try:
            cur.execute(sql)
            cur_res = cur.fetchall()
            data = []
            for res in cur_res:
                cur_data = {"courseID": res[0], "courseName": res[1], "content": res[2]}
                data.append(cur_data)
            data = json.dumps(data)
            return data
        except Exception as e:
            print(traceback.print_exc())
            flash(traceback.print_exc())
            return None
