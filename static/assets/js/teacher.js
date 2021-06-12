var getCourses = function(){
    $.post('/data/CourseInfo',function(data){
    console.log(data)
		data=JSON.parse(data);
		$('#addCourseNo').html('');
		$('#addCourseNo').append('<option style="display:none" selected>空</option>');
		$.each(data["rows"],function(index,item){
			var typeStr = '<option value="' + item["courseID"] + '">' + item["courseName"] + '</option>';
			$('#addCourseNo').append(typeStr);
			console.log(typeStr)
		});
		$('#addCourseNo').selectpicker('refresh');
		$('#addCourseNo').selectpicker('show');
	})
}
var getTeachCourses = function(){
    $.post('/data/TeachCourseInfo',function(data){
		data=JSON.parse(data);
		$('#addCourseNo').html('');
		$('#addCourseNo').append('<option style="display:none" value="" selected>空</option>');
		$.each(data["rows"],function(index,item){
			var typeStr = '<option value="' + item["courseID"] + '">' + item["courseName"] + '</option>';
			$('#addCourseNo').append(typeStr);
		});
		$('#addCourseNo').selectpicker('refresh');
		$('#addCourseNo').selectpicker('show');
	})
}
var getTeachCourses2 = function(){
    $.post('/data/TeachCourseInfo',function(data){
		data=JSON.parse(data);
		$('#addCourseNo2').html('');
		$('#addCourseNo2').append('<option style="display:none" value="" selected>空</option>');
		$.each(data["rows"],function(index,item){
			var typeStr = '<option value="' + item["courseID"] + '">' + item["courseName"] + '</option>';
			$('#addCourseNo2').append(typeStr);
		});
		$('#addCourseNo2').selectpicker('refresh');
		$('#addCourseNo2').selectpicker('show');
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
var check_addTeachApplication = function () {
        if ((document.getElementById("addCourseNo").value!="空") && document.getElementById("addReason").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }
var check_addStartApplication = function () {
        if (document.getElementById("addCourseName").value && document.getElementById("addReason").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }
var check_addEvaluation = function () {
        if ((document.getElementById("addCourseNo2").value!="空") && document.getElementById("addEva").value) {
            return true;
        }
        else{
        	alert("请填写完整！")
            console.log("没填写完整")
            return false;
        }
  }

var addTeachApplication_submit = function (){
    if(!check_addTeachApplication())
		return;
    var data = {};
    data['choice']="submit"
    data['courseID']=document.getElementById("addCourseNo").value
    data['reason'] = document.getElementById("addReason").value
  	$.ajax({
  		url: '/edit/HandleTeachApplication',
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
var addStartApplication_submit = function (){
    if(!check_addStartApplication())
		return;
    var data = {};
    data['choice']="submit"
    data['courseName']=document.getElementById("addCourseName").value
    data['reason'] = document.getElementById("addReason").value
  	$.ajax({
  		url: '/edit/HandleStartApplication',
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
  		}
  	})
}
var addEvaluation_submit = function () {
    if(!check_addEvaluation())
		return;
    var data = {};

    data['addCourseNo'] = document.getElementById("addCourseNo2").value
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

