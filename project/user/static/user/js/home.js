var url = "http://127.0.0.1:8000/property/deliprops"

function loadXMLDoc(url) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function(url) {
    	// console.log(xmlhttp);
        if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
           if (xmlhttp.status == 200) {
               var propertyObj = JSON.parse(xmlhttp.responseText);
               localStorage.setItem('propertyObject', JSON.stringify(propertyObj));
               var propertyObjArray = propertyObj['result'];
               for (index in propertyObjArray){
               		var new_li = create_li(propertyObjArray[index]);
               		var propertyUl = document.getElementById('propertyList');
               		propertyUl.appendChild(new_li);
               		
               }
               return propertyObjArray
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



loadXMLDoc(url);

// PROPERTY LIST sent at the beginning.
var propertyObjList = JSON.parse(localStorage.getItem('propertyObject'))['result'];


// Create Quick Search
var cityStateInput = document.getElementById('cityStateInput');

cityStateInput.addEventListener('keyup', function(){
 var cityMatches = findStateCityMatches(this.value, propertyObjList);
 var propertyUl = document.getElementById('propertyList');
 while(propertyUl.firstChild ){
     propertyUl.removeChild( propertyUl.firstChild );
 }
 for (index in cityMatches){
   var newLi = create_li(cityMatches[index]);
        propertyUl.appendChild(newLi);
 }
});

var findStateCityMatches = function(wordToMatch, properties){
  return properties.filter(property=> {
    const regex = new RegExp(wordToMatch, 'gi');
    return property.state.match(regex) || property.city.match(regex)
  })
};



























// DOM MANIPULATION FUNCTIONS
var create_li = function(property){
  // Create Basic Structure
  var new_li = document.createElement('li');
  new_li.className = 'col s12 propertiesListItem';
  var cardDiv = document.createElement('div');
  cardDiv.className = 'card blue-grey darken-1';
  var cardContentDiv = document.createElement('div');
  cardContentDiv.className = 'card-content white-text';
  new_li.appendChild(cardDiv);
  cardDiv.appendChild(cardContentDiv);

  var actionDiv = document.createElement('div');
  actionDiv.className = 'card-action';
  var aTag = document.createElement('a');
  aTag.href = '/property/single/' + property.id;
  aTag.innerHTML = 'More Info';
  actionDiv.appendChild(aTag);




  // Create inner <ul> for property specific info
  var propertyInfoUl = document.createElement('ul');

  var dateUploadedLi = document.createElement('li');
  dateUploadedLi.innerHTML = "Date Uploaded: " + property['date_upload'];
  propertyInfoUl.appendChild(dateUploadedLi);

  var propertyTitle = document.createElement('h4');
  propertyTitle.className = 'propertyTitle';
  propertyTitle.innerHTML = property['address'];
  propertyInfoUl.appendChild(propertyTitle)

  var currentPriceLi = document.createElement('li');
  currentPriceLi.className = "propertyLi";
  cleanPrice = priceCleaner(property['current_price'].toString());
  currentPriceLi.innerHTML = "Current Price: $ " + cleanPrice;
  propertyInfoUl.appendChild(currentPriceLi);

  var addressLi = document.createElement('li');
  addressLi.className = "propertyLi";
  addressLi.innerHTML = "Address: " + property['address']+ ", " + property['city'] + ", " + property['state'] + ", " + property['zipcode'];
  propertyInfoUl.appendChild(addressLi);

  var statusLi = document.createElement('li');
  statusLi.className = "propertyLi";
  statusLi.innerHTML = "Status: " + property['status'][0].toUpperCase() + property['status'].substr(1,property['status'].length);
  propertyInfoUl.appendChild(statusLi);

  var addressLi = document.createElement('li');
  addressLi.className = "propertyLi";
  addressLi.innerHTML = "Square Footage: " + property['sq_ft'] + "sqft"
  propertyInfoUl.appendChild(addressLi);

  var bathroomsLi = document.createElement('li');
  bathroomsLi.className = "propertyLi";
  bathroomsLi.innerHTML = "Bathrooms: " + property['bathrooms'];
  propertyInfoUl.appendChild(bathroomsLi);

  var bedroomsLi = document.createElement('li');
  bedroomsLi.className = "propertyLi";
  bedroomsLi.innerHTML = "Bedrooms: " + property['bedrooms'];
  propertyInfoUl.appendChild(bedroomsLi);
  
  cardContentDiv.appendChild(propertyInfoUl);
  cardDiv.appendChild(actionDiv);

  return new_li
};


// EXTRA FUNCTIONS
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