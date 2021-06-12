var getCourses = function(){
    $.post('/data/CourseInfo',function(data){
		data=JSON.parse(data);
		$('#addCourseNo').html('');
		$('#addCourseNo').append('<option style="display:none" selected>空</option>');
		$.each(data["rows"],function(index,item){
			var typeStr = '<option value="' + item["courseID"] + '">' + item["courseName"] + '</option>';
			$('#addCourseNo').append(typeStr);
		});
		$('#addCourseNo').selectpicker('refresh');
		$('#addCourseNo').selectpicker('show');
	})
}

var getCourseTeachers = function(){
    $.post('/data/StudentCurriculum',function(data){
		data=JSON.parse(data);
		$('#addCourseNo').html('');
		$('#addCourseNo').append('<option style="display:none" selected>空</option>');
		$.each(data["rows"],function(index,item){
			var typeStr = '<option value="{\'courseID\':' + item["courseID"] +',\'teacherID\':' + item["teacherID"] + '}">' + item["courseName"] + '-' + item["teacherName"] + '</option>';
			$('#addCourseNo').append(typeStr);
		});
		$('#addCourseNo').selectpicker('refresh');
		$('#addCourseNo').selectpicker('show');
	})
}

var check_editPassword = function () {
        if (document.getElementById("oldPassword").value && document.getElementById("newPassword").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }

var check_addStudentCurriculum = function () {
        if ((document.getElementById("addCourseNo").value!="空")) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }

var check_addEvaluation = function () {
        if ((document.getElementById("addCourseNo").value!="空") && document.getElementById("addEva").value ) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }

var editPassword_submit = function (){
  	if(!check_editPassword())
		return;
  	var data = {}
  	data["oldPassword"] = document.getElementById("oldPassword").value
  	data["newPassword"] = document.getElementById("newPassword").value
  	$.ajax({
  		url: '/edit/editPassword',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="wrong oldPassword"){
  					alert("旧密码错误");
  				}
  				else if(res['reason']=="short newPassword"){
  					alert("新密码至少6位")
  				}
  				else {
  					alert("数据库错误，稍后重试");
  				}
  			}
  			else
  				alert("成功");
  		}
  	})
}
var addStudentCurriculum_submit =  function (){
  	if(!check_addStudentCurriculum())
		return;
    var data = {};
    data['addCourseNo']=document.getElementById("addCourseNo").value
  	$.ajax({
  		url: '/edit/addStudentCurriculum',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="repeated time"){
  					alert("时间冲突");
  				}
  				else {
  					alert("数据库错误，稍后重试");
  				}
  			}
  			else
  				alert("成功");
  				$('#table').bootstrapTable('refresh');
  		}
  	})

  }

var addEvaluation_submit = function () {
    if(!check_addEvaluation())
		return;
    var data = {};
    json_str = document.getElementById("addCourseNo").value
    json_str = json_str.replace(/\'/g, "\"")
    json_json = JSON.parse(json_str)

    data['addCourseNo'] = json_json["courseID"]
    data['addTeacherNo'] = json_json["teacherID"]
    data['addEva']=document.getElementById("addEva").value
  	$.ajax({
  		url: '/edit/addEvaluation',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){

  			if(res['status'] == false){
  				if(res['reason']=="repeated time"){
  					alert("时间冲突");
  				}
  				else {
  					alert("数据库错误，稍后重试");
  				}
  			}
  			else
  				alert("成功");
  				$('#table').bootstrapTable('refresh');
  		}
  	})
}
