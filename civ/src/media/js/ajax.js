/* 
Civilization by Ouds
Copyright (c) 2010 Thinker.cc. Please don't steal.
*/

var xhr = false;
try{
	xhr = new XMLHttpRequest();
}
catch(ms){
	try{
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	}
	catch(oie){
		try{
			xhr = new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch(failed){
			xhr = false;
		}
	}
}
if(!xhr)
	alert("Error initializing XMLHttpRequest");

function call(method, url, data, element_id){

	xhr.open(method, url);
	xhr.onreadystatechange = function(){
		
		if(element_id != null)
			document.getElementById(element_id).innerHTML = method;
		
		if(xhr.readyState == 4 && xhr.status == 200){

			var rt = xhr.responseText;
			
			if(rt == 'reload')
				location.reload();
			else if(rt.substr(0, 2) == 'to')
				location.href = rt.substr(3);
			else
				document.getElementById(element_id).innerHTML = rt;
		}
	};
	xhr.setRequestHeader('X_REQUESTED_WITH', 'XMLHttpRequest');
	xhr.send(data);
}



