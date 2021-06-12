# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
    Software:   PyCharm
    File Name:    utils
    Description:   
  
    Author:  Phil
    Email:  furuoo@163.com
    Date:   2021/4/24 16:38
    Version:  3.8.1
"""
# --------------------------------------------------------------
#    Description：
#    
#    
# --------------------------------------------------------------

#计算课程时间
def cur_courseTime(data):
    res = ""
    day = ["","周一","周二","周三","周四","周五","周六","周七"]
    beginNo = data[1]
    endNo = data[1]+data[2]-1
    res = day[int(data[0])]+"第"+str(beginNo)+"-"+str(endNo)+"节课"
    return res

#计算考试时间
def cur_examTime(data):
    res = data[0].isoformat()+"：\n"+str(data[1])+"-"+str(data[2])
    return res
