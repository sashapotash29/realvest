console.log("JS connected")


// BEGINNING AJAX REQUEST TO LOAD PROPERTIES

var url = "http://127.0.0.1:8000/property/deliprops"

function loadXMLDoc(url) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(url) {
    	console.log(xmlhttp);
        if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
           if (xmlhttp.status == 200) {
               console.log(xmlhttp.responseText);
           }
           else if (xmlhttp.status == 400) {
              alert('There was an error 400');
           }
           else {
               alert('something else other than 200 was returned');
           }
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


loadXMLDoc(url)


var create_li = function(property){
	var new_li = document.createElement('li');
	new_li.setAttribute('class', )

};

