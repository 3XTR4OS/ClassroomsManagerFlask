	document.addEventListener('DOMContentLoaded', () => {
	  document.querySelectorAll('button').forEach(button => {
	    button.onclick = () => {
	      const request = new XMLHttpRequest();
	      request.open('POST', `/${button.id}`);
	      request.onload = () => {
				const response = request.responseText;
				document.getElementById('data_field').innerHTML = response;
	      };
	      request.send();
	    };
	 });
	});