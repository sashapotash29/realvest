var googleMapsDiv = document.getElementsByClassName('googleMaps')[0]
console.log(googleMapsDiv)

var latitude = parseFloat(googleMapsDiv.dataset['lat'])
var longitude = parseFloat(googleMapsDiv.dataset['long'])
console.log(latitude)
console.log(longitude)


function initMap() {
        var uluru = {lat: latitude, lng: longitude};
        var map = new google.maps.Map(googleMapsDiv, {
          zoom: 15,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
};

// SLIDESHOW JAVASCRIPT

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var imageList = document.getElementsByClassName("slideShowImage");
    if (n > imageList.length) {slideIndex = 1} 
    if (n < 1) {slideIndex = imageList.length} ;
    for (i = 0; i < imageList.length; i++) {
        imageList[i].style.display = "none"; 
    }
    imageList[slideIndex-1].style.display = "block"; 
};










// Investment stuff
const save_button = document.getElementById('saveButton')
const invest_button = document.getElementById('investButton')


if (save_button){
  save_button.addEventListener('click', function(){
  	console.log("we are here")
  	save_button.style.display = "none"
  	var xmlHttp = new XMLHttpRequest();
      xmlHttp.onreadystatechange = function() { 
          if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
              callback(xmlHttp.responseText);
      }
      id = document.getElementById('propertyInfoUl').dataset['id']
      xmlHttp.open("get", "/save_property/"+id, true);
      xmlHttp.send();
  });
};

var investButtonInForm = document.getElementById('formToInvest')

if(invest_button){

invest_button.addEventListener('click', function(){
	console.log("we are here")
	investButtonInForm.style.display="block"
	 // var xmlHttp = new XMLHttpRequest();
  //   xmlHttp.onreadystatechange = function() { 
  //       if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
  //           callback(xmlHttp.responseText);
  //   }
  //   xmlHttp.open("GET", "/save_property/, true); // true for asynchronous 
  //   xmlHttp.send(null);

    invest_button.style.display = "none"
	
  });
};






var priceCleaner = function(priceString){
  var cleanPrice = "";
  var threeCheck = 0;
  for (var i = priceString.length-1; i >= 0; i--){
    if (threeCheck % 3 == 0 && threeCheck != 0) {
      cleanPrice = "," + cleanPrice;
      cleanPrice = priceString[i] + cleanPrice;
      threeCheck +=1;
    } 
    else{
      cleanPrice = priceString[i] + cleanPrice;
      threeCheck += 1;

    }

  }
  return cleanPrice
};
