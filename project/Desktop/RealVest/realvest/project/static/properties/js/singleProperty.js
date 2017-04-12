// var createMap = function() {
//         // Create a map object and specify the DOM element for display.
//         var googleMapsDiv = document.getElementsByClassName('googleMaps')

//         var map = new google.maps.Map(googleMapsDiv, {
//           center: {lat: latitude, lng: longitude},
//           scrollwheel: false,
//           zoom: 8
//         });
// };

// CreateMap()

var googleMapsDiv = document.getElementsByClassName('googleMaps')[0]
console.log(googleMapsDiv)

var latitude = parseFloat(googleMapsDiv.dataset['lat'])
var longitude = parseFloat(googleMapsDiv.dataset['long'])
console.log(latitude)
console.log(longitude)



// function initMap() {
// 	var map = new google.maps.Map(googleMapsDiv, {
// 		center: coordinates,
// 		zoom: 4
// 		})
// 	var marker = new google.maps.Marker({
// 		position: coordinates,
// 		map: map,
// 		});
// }

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
