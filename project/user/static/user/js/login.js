var listNavItems = document.getElementsByClassName('aTagNav')

console.log("hello");
console.log(listNavItems);

for(var i=0; i<=listNavItems.length-1; i++){

	listNavItems[i].style.display = "none";



};

var searchForm = document.getElementsByClassName('searchBarFormArea')[0].style.display="none"

// THE TOGGLE BUTTONS
var investorToggle = document.getElementById('investorToggle');
var realtorToggle = document.getElementById('realtorToggle');

// THE FORM SECTIONS
var investorSection = document.getElementById('investorSection');
var realtorSection = document.getElementById('realtorSection');



investorToggle.addEventListener('click', function(e){
	investorSection.className = investorSection.className.replace("active", "");
	investorSection.className += "active"
	realtorSection.className = realtorSection.className.replace("active", "");
});

realtorToggle.addEventListener('click', function(e){
	realtorSection.className = realtorSection.className.replace("active", "");
	realtorSection.className += "active"
	investorSection.className = investorSection.className.replace("active", "");

});


// SIGN UP AND LOGIN TOGGLE WITHIN SECTION

var innerToggleButtonInvestor = document.getElementById('toggleSignUpOrLoginInvestor');
var innerToggleButtonRealtor = document.getElementById('toggleSignUpOrLoginRealtor');


// FORM SECTIONS
var investorLoginForm = document.getElementById('investorLoginForm');
var investorSignUpForm = document.getElementById('investorSignUpForm');
var realtorLoginForm = document.getElementById('realtorLoginForm');
var realtorSignUpForm = document.getElementById('realtorSignUpForm');

innerToggleButtonInvestor.addEventListener('click', function(){
	if (this.value == "Sign Up"){
		investorSignUpForm.style.display = "block"
		investorLoginForm.style.display = "none"
		this.value = "Login";

	}
	else{
		investorLoginForm.style.display = "block"
		investorSignUpForm.style.display = "none"
		this.value = "Sign Up";
	}


});

innerToggleButtonRealtor.addEventListener('click', function(){
	if (this.value == "Sign Up"){
		realtorSignUpForm.style.display = "block"
		realtorLoginForm.style.display = "none"
		this.value = "Login";

	}
	else{
		realtorLoginForm.style.display = "block"
		realtorSignUpForm.style.display = "none"
		this.value = "Sign Up";
	}


});



