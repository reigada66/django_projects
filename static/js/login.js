let state1 = false;

$(document).ready(function() {
	let password1 = document.getElementById("password");
	let iconp1 = document.getElementById("iconp1");


	iconp1.addEventListener("click", function(){
		if (state1) {
			password1.setAttribute("type", "password");
			iconp1.setAttribute("class", "far fa-eye-slash");
		} else {
			password1.setAttribute("type", "text");
			iconp1.setAttribute("class", "far fa-eye");
//            alvo.classList.removeClass( "fa fa-eye" ).addClass( "fas fa-eye-slash" );
		}
		state1 = !state1;
	});


});
