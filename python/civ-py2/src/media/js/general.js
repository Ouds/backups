/* 
Civilization by Ouds
Copyright (c) 2010 Thinker.cc. Please don't steal.
*/

function start(){
    setInterval(server_time, 1000);
    food();
    wood();
    ore();
    gold();
    people();
}

function curent_time(){
    clock = now.getHours() + ":";
    mm = now.getMinutes();
    if(mm <= 9) clock += "0";
    clock += mm + ":";
    ss = now.getSeconds();
    if(ss <= 9) clock += "0";
    return clock + ss;
}

function server_time(){
    document.getElementById("server_current_time").innerHTML = curent_time();
    now.setSeconds(now.getSeconds()+1)
}

// 城市资源

function food(){
    food_object = document.getElementById("food");
    food_value = parseInt(food_object.innerHTML);
    food_storage_value = parseInt(document.getElementById("food_storage").innerHTML);
    food_speed_value = parseInt(document.getElementById("food_speed").innerHTML);
    if(food_value < food_storage_value && food_speed_value > 0){
        setTimeout(food, 3600/food_speed_value*1000);
        food_object.innerHTML = food_value + 1;
    }
}

function wood(){
    wood_object = document.getElementById("wood");
    wood_value = parseInt(wood_object.innerHTML);
    wood_storage_value = parseInt(document.getElementById("wood_storage").innerHTML);
    wood_speed_value = parseInt(document.getElementById("wood_speed").innerHTML);
    if(wood_value < wood_storage_value && wood_speed_value > 0){
        setTimeout(wood, 3600/wood_speed_value*1000);
        wood_object.innerHTML = wood_value + 1;
    }
}

function ore(){
    ore_object = document.getElementById("ore");
    ore_value = parseInt(ore_object.innerHTML);
    ore_storage_value = parseInt(document.getElementById("ore_storage").innerHTML);
    ore_speed_value = parseInt(document.getElementById("ore_speed").innerHTML);
    if(ore_value < ore_storage_value && ore_speed_value > 0){
        setTimeout(ore, 3600/ore_speed_value*1000);
        ore_object.innerHTML = ore_value + 1;
    }
}

function gold(){
    gold_object = document.getElementById("gold");
    gold_value = parseInt(gold_object.innerHTML);
    gold_storage_value = parseInt(document.getElementById("gold_storage").innerHTML);
    gold_speed_value = parseInt(document.getElementById("gold_speed").innerHTML);
    if(gold_value < gold_storage_value){
        setTimeout(gold, 3600/gold_speed_value*1000);
        gold_object.innerHTML = gold_value + 1;
    }
}

function people(){
    people_object = document.getElementById("people");
    people_value = parseInt(people_object.innerHTML);
    people_storage_value = parseInt(document.getElementById("people_storage").innerHTML);
    people_speed_value = parseInt(document.getElementById("people_speed").innerHTML);
    if(people_value < people_storage_value){
        setTimeout(people, 3600/people_speed_value*1000);
        people_object.innerHTML = people_value + 1;
    }
}

// 时间格式和事件

function time_format(s){
    if(s >= 0){
        hours = Math.floor(s/(60*60));
        minutes = Math.floor(s/60)%60;
        seconds = s%60;
        t = hours + ":";
        if(minutes <= 9) t += "0";
        t += minutes + ":";
        if(seconds <= 9) t += "0";
        t += seconds;
    }
    else t = "0:00:0x";
    return t;
}

function event_timer(time_remain, id){
    tr = parseInt(time_remain) + 2;
    event_id = document.getElementById(id);
    if (tr == 0){
        window.location.reload();
    }
    else{
        event_id.innerHTML = time_format(tr);
        time_remain -= 1;
        setTimeout("event_timer(" + time_remain + ",'" + id + "')", 1000);
    }
}

// 字符串去除空格属性

String.prototype.trim = function(){ return this.replace(/(^\s*)|(\s*$)/g, ""); }
String.prototype.ltrim = function(){ return this.replace(/(^\s*)/g, ""); }
String.prototype.rtrim = function(){ return this.replace(/(\s*$)/g, ""); } 

// 检验和提示

function is_valid(vo){
	var valid_result = false;
	for(var o = 0; o < vo.length; o++){
		var valid_object = document.getElementById(vo[o]);
		switch(valid_object.getAttribute('valid')){
			case 'blank':
				valid_result = not_blank(valid_object);
				break;
			case 'number':
				valid_result = is_number(valid_object);
				break;
		}
		if(!valid_result)
			break;
	}
	return valid_result;
}

var valid_error_color = "#FF9900";
var valid_right_color = "#FFFFFF";

function not_blank(valid_object){
	valid_object.value = valid_object.value.trim();
	if(valid_object.value == ''){
		valid_object.style.backgroundColor = valid_error_color;
		alert('不能为空');
		return false;
	}
	else{
		valid_object.style.backgroundColor = valid_right_color;
		return true;
	}
}

function is_number(valid_object){
	valid_object.value = valid_object.value.trim();
	num_reg = "^[0-9]+$";
    reg_exp = new RegExp(num_reg);
	if(!reg_exp.test(valid_object.value)){
		valid_object.style.backgroundColor = valid_error_color;
		alert('请输入数字');
		return false;
	}
	else{
		valid_object.style.backgroundColor = valid_right_color;
		return true;
	}
}
