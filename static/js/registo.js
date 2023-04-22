let state1 = false;
let state2 = false;
let isPasswordMatch = false;

$(document).ready(function() {
	let password1 = document.getElementById("password");
	let password2 = document.getElementById("password2");
	let iconp1 = document.getElementById("iconp1");
	let iconp2 = document.getElementById("iconp2");
	const feedback = document.getElementById("confirmPassword-feedback");


	let passwordStrength = document.getElementById("password-strength");
	let lowUpperCase = document.querySelector(".low-upper-case i");
	let number = document.querySelector(".one-number i");
	let specialChar = document.querySelector(".one-special-char i");
	let eightChar = document.querySelector(".eight-character i");
	const correio = document.querySelector('input[type="email"]');

	correio.addEventListener("blur", (event) => {
		var filtro = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		if (!filtro.test(correio.value)){
		  correio.focus();
		}
	});

	password1.addEventListener("keyup", function(){
		let pass = document.getElementById("password").value;
		checkStrength(pass);
	});

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

	iconp2.addEventListener("click", function(){
		if (state2) {

			password2.setAttribute("type", "password");
			iconp2.setAttribute("class", "far fa-eye-slash");
		} else {
			password2.setAttribute("type", "text");
			iconp2.setAttribute("class", "far fa-eye");
//            alvo.classList.removeClass( "fa fa-eye" ).addClass( "fas fa-eye-slash" );
		}
		state2 = !state2;
	});


	password2.addEventListener("input", () => {

		if (password.value.indexOf(password2.value) != 0) {
			feedback.innerHTML = "Passwords não coincidem!";
			isPasswordMatch = false;
		} else {
			feedback.innerHTML = "Até agora tudo bem!";
			isPasswordMatch = true;
		}
	});


	function checkStrength(password) {
		let strength = 0;

		//If password contains both lower and uppercase characters
		if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) {
			strength += 1;
			lowUpperCase.classList.remove('fa-circle');
			lowUpperCase.classList.add('fa-check');
		} else {
			lowUpperCase.classList.add('fa-circle');
			lowUpperCase.classList.remove('fa-check');
		}
		//If it has numbers and characters
		if (password.match(/([0-9])/)) {
			strength += 1;
			number.classList.remove('fa-circle');
			number.classList.add('fa-check');
		} else {
			number.classList.add('fa-circle');
			number.classList.remove('fa-check');
		}
		//If it has one special character
		if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) {
			strength += 1;
			specialChar.classList.remove('fa-circle');
			specialChar.classList.add('fa-check');
		} else {
			specialChar.classList.add('fa-circle');
			specialChar.classList.remove('fa-check');
		}
		//If password is greater than 7
		if (password.length > 7) {
			strength += 1;
			eightChar.classList.remove('fa-circle');
			eightChar.classList.add('fa-check');
		} else {
			eightChar.classList.add('fa-circle');
			eightChar.classList.remove('fa-check');
		}

		// If value is less than 2
		if (strength < 2) {
			passwordStrength.classList.remove('progress-bar-warning');
			passwordStrength.classList.remove('progress-bar-success');
			passwordStrength.classList.add('progress-bar-danger');
			passwordStrength.style = 'width: 10%';
		} else if (strength == 3) {
			passwordStrength.classList.remove('progress-bar-success');
			passwordStrength.classList.remove('progress-bar-danger');
			passwordStrength.classList.add('progress-bar-warning');
			passwordStrength.style = 'width: 60%';
		} else if (strength == 4) {
			passwordStrength.classList.remove('progress-bar-warning');
			passwordStrength.classList.remove('progress-bar-danger');
			passwordStrength.classList.add('progress-bar-success');
			passwordStrength.style = 'width: 100%';
		}
	}

});
