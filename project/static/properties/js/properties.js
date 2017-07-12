console.log("JS connected")


// BEGINNING AJAX REQUEST TO LOAD PROPERTIES

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


// Turning LocalStorage attribute into a constant variable. This is the PropertiesArray
const propertyObjList = JSON.parse(localStorage.getItem('propertyObject'))['result'];


// Filter Function
var hardFilter = function(filterState, propertyObjList){
	var searchResultArray = [];
	console.log(filterState);
	for(index in propertyObjList){
		var property = propertyObjList[index];
		if (property.current_price >= filterState['priceMin'] 
			&& property.current_price <= filterState['priceMax']
			&& property.bedrooms >= filterState['numberBedrooms'] 
			){
			console.log('counted')
			searchResultArray.push(property);

		}

	}
	searchResultArray = findCityMatches(filterState['cityInput'], searchResultArray);
	searchResultArray = findStateMatches(filterState['stateInput'], searchResultArray);
	return searchResultArray
};

var captureFilterState = function(){
	const filterState = {
		'priceMin' : parseInt(document.getElementById('minInput').value),
		'priceMax' : parseInt(document.getElementById('maxInput').value),
		'cityInput' : document.getElementById('cityInput').value,
		'stateInput' : document.getElementById('stateInput').value,
		'numberBedrooms' : parseInt(document.getElementById('bedroomsInput').value)
	};
	return filterState
}

// Add event listener for filter toggle button.
var filterToggleButton = document.getElementById('filterToggleButton');
filterToggleButton.addEventListener('click', function(){
	var filterArea = document.getElementById('filterArea');
		if (filterArea.style.display == 'block'){
			filterArea.style.display = 'none';

		}
		else{
			filterArea.style.display = 'block';
		}

});

// Add event listener for hardFilter button.
var searchButton = document.getElementById('searchButton');
searchButton.addEventListener('click',function(){
	var propertyUl = document.getElementById('propertyList');
	var filterState = captureFilterState();
	var propertyResults = hardFilter(filterState, propertyObjList);
	console.log(propertyResults);
	while(propertyUl.firstChild ){
  		propertyUl.removeChild( propertyUl.firstChild );
	}
	for (index in propertyResults){
		var property = propertyResults[index];
		
		var newLi = create_li(property);
		propertyUl.appendChild(newLi);
	}

});




// QUICK FILTER FUNCTIONS
var findCityMatches = function(wordToMatch, properties){
	return properties.filter(property=> {
		const regex = new RegExp(wordToMatch, 'gi');
		return property.city.match(regex)
	})
};

var findStateMatches = function(wordToMatch, properties){
	return properties.filter(property=> {
		const regex = new RegExp(wordToMatch, 'gi');
		return property.state.match(regex)
	})
};

// FILTER EVENT LISTENERS
var cityInput = document.getElementById('cityInput');
var stateInput = document.getElementById('stateInput');

// cityInput.addEventListener('keyup', function(){
// 	var cityMatches = findCityMatches(this.value, propertyObjList);
// 	var propertyUl = document.getElementById('propertyList');
// 	while(propertyUl.firstChild ){
//   		propertyUl.removeChild( propertyUl.firstChild );
// 	}
// 	for (index in cityMatches){
// 		var newLi = create_li(cityMatches[index]);
//         propertyUl.appendChild(newLi);
// 	}
// });

// stateInput.addEventListener('keyup', function(){
// 	var stateMatches = findStateMatches(this.value, propertyObjList);
// 	var propertyUl = document.getElementById('propertyList');
// 	while(propertyUl.firstChild ){
//   		propertyUl.removeChild( propertyUl.firstChild );
// 	}
// 	for (index in stateMatches){
// 		var newLi = create_li(stateMatches[index]);
//         propertyUl.appendChild(newLi);
// 	}
// });










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


