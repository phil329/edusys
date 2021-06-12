var getSpecialities = function (){
	$.post('/data/CollegeSpeciality',function(data){
		data=JSON.parse(data);
		$('#addSpeciality').html('');
		$('#addSpeciality').append('<option style="display:none" selected>空</option>');
		$.each(data,function(index,item){
			var typeStr = '<optgroup label="' + item["ColName"] + '">';
			for (let speName of item["SpeName"]){
				typeStr += '<option value="' + speName[1] + '">' + speName[0] + '</option>';
			}
			typeStr += '</optgroup>'
			$('#addSpeciality').append(typeStr);
		});
		$('#addSpeciality').selectpicker('refresh');
		$('#addSpeciality').selectpicker('show');
	})
  }
var getColleges = function (){
	$.post('/data/CollegeSpeciality',function(data){
		data=JSON.parse(data);
		$('#addCollege').html('');
		$('#addCollege').append('<option style="display:none" selected>空</option>');
		$.each(data,function(index,item){
			var typeStr = '<option>' + item["ColName"] + '</option>';
			$('#addCollege').append(typeStr);
		});
		$('#addCollege').selectpicker('refresh');
		$('#addCollege').selectpicker('show');
	})
}
var getClassrooms = function(){
    $.post('/data/ClassroomInfo',function(data){
        data=JSON.parse(data);
		$('#classroomNo').html('');
		$('#classroomNo').append('<option style="display:none" selected>空</option>');
		$.each(data,function(index,item){
			var typeStr = '<option value="' + item["No"] + '">' + item["position"] + '</option>';
			$('#classroomNo').append(typeStr);
		});
		$('#classroomNo').selectpicker('refresh');
		$('#classroomNo').selectpicker('show');
    })
}
var getCourseTeacherClassroom = function(){
    $.post('/data/CourseInfo',function(data){
        data=JSON.parse(data);
		$('#addCourseNo').html('');
		$('#addCourseNo').append('<option style="display:none" selected>空</option>');
		$.each(data['rows'],function(index,item){
			var typeStr = '<option value="' + item["courseID"] + '">' + item["courseName"] + '</option>';
			$('#addCourseNo').append(typeStr);
		});
		$('#addCourseNo').selectpicker('refresh');
		$('#addCourseNo').selectpicker('show');
    })
    $.post('/data/TeacherInfo',function(data){
        data=JSON.parse(data);
		$('#addTeacherNo').html('');
		$('#addTeacherNo').append('<option style="display:none" selected>空</option>');
		$.each(data['rows'],function(index,item){
			var typeStr = '<option value="' + item["No"] + '">' + item["name"] + '</option>';
			$('#addTeacherNo').append(typeStr);
		});
		$('#addTeacherNo').selectpicker('refresh');
		$('#addTeacherNo').selectpicker('show');
    })

    $.post('/data/ClassroomInfo',function(data){
        data=JSON.parse(data);
		$('#addClassroomNo').html('');
		$('#addClassroomNo').append('<option style="display:none" selected>空</option>');
		$.each(data,function(index,item){
			var typeStr = '<option value="' + item["No"] + '">' + item["position"] + '</option>';
			$('#addClassroomNo').append(typeStr);
		});
		$('#addClassroomNo').selectpicker('refresh');
		$('#addClassroomNo').selectpicker('show');
    })


}
var check_addStudent = function () {
        if (document.getElementById("addName").value && document.getElementById("addBirthday").value && (document.getElementById("addSpeciality").value!="空") && document.getElementById("addGender").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }
var check_addAdmin = function () {
   if (document.getElementById("addName").value && document.getElementById("addBirthday").value && document.getElementById("addGender").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
}
var check_addTeacher = function () {
        if (document.getElementById("addName").value && document.getElementById("addBirthday").value && (document.getElementById("addCollege").value!="空") && document.getElementById("addGender").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
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
var check_addExam = function () {
        if ((document.getElementById("addCourseNo").value!="空") && document.getElementById("addDay").value && document.getElementById("addBeginTime").value && document.getElementById("addEndTime").value && (document.getElementById("addTeacherNo").value!="空") && (document.getElementById("addClassroomNo").value!="空")) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }
var addTeacher_submit = function (){
	if(!check_addTeacher())
		return;

    var data = {};
    data['addName']=document.getElementById("addName").value
    data['addGender'] = document.getElementById("addGender").value
    data['addBirthday'] = document.getElementById("addBirthday").value
    data['addCollege'] = document.getElementById("addCollege").value
  	$.ajax({
  		url: '/edit/addTeacher',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="wrong oldPassword"){
  					alert("旧密码错误");
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
var addAdmin_submit =  function (){
	if(!check_addAdmin())
		return;
    var data = {};
    data['addName']=document.getElementById("addName").value
    data['addGender'] = document.getElementById("addGender").value
    data['addBirthday'] = document.getElementById("addBirthday").value
  	$.ajax({
  		url: '/edit/addAdmin',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="wrong oldPassword"){
  					alert("旧密码错误");
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
var addStudent_submit =  function (){
	if(!check_addStudent())
		return;
    var data = {};
    data['addName']=document.getElementById("addName").value
    data['addGender'] = document.getElementById("addGender").value
    data['addBirthday'] = document.getElementById("addBirthday").value
    data['addSpeciality'] = document.getElementById("addSpeciality").value
  	$.ajax({
  		url: '/edit/addStudent',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="wrong oldPassword"){
  					alert("旧密码错误");
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
  				$('#table').bootstrapTable('refresh');
  		}
  	})
  }

var addExam_submit = function(){
    if(!check_addExam())
		return;
    var data = {}
  	data["addCourseNo"] = document.getElementById("addCourseNo").value
  	data["addDay"] = document.getElementById("addDay").value
  	data["addBeginTime"] = document.getElementById("addBeginTime").value
  	data["addEndTime"] = document.getElementById("addEndTime").value
  	data["addTeacherNo"] = document.getElementById("addTeacherNo").value
  	data["addClassroomNo"] = document.getElementById("addClassroomNo").value

  	$.ajax({
  		url: '/edit/addExam',
  		type: 'post',
  		dataType:'json',
  		data:JSON.stringify(data),
  		success: function(res){
  			if(res['status'] == false){
  				if(res['reason']=="repeated Course"){
  					alert("该课程已安排考试");
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
