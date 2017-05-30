var listNavItems = document.getElementsByClassName('aTagNav')

console.log("hello");
console.log(listNavItems);

for(var i=0; i<=listNavItems.length-1; i++){

	listNavItems[i].style.display = "none";



};

var searchForm = document.getElementsByClassName('searchBarFormArea')[0].style.display="none"