import requests
import xmltodict
from datetime import datetime
import json
import time
# from yattag import indent

# DATA SOURCED VIA MANUAL SEARCH
EastTwentySecond = {'name':'a','number': '121', 'street': '22nd', 'roadtype':'St', 'zip': '10010' }
FiftyOneParkPlace = {'name':'b','number': '45', 'street': 'Park', 'roadtype':'Place', 'zip': '10007' }
SeventyFiveKenmare = {'name':'c','number': '75', 'street': 'Kenmare', 'roadtype':'St', 'zip': '10012' }
ThreeThreeThreeSchermerhorn = {'name':'d','number': '333', 'street': 'Schermerhorn', 'roadtype':'St', 'zip': '11217' }
FiveNineFiveBaltic = {'name':'e','number': '595', 'street': 'Baltic', 'roadtype':'St', 'zip': '11217' }
FiveNineOneThirdAve = {'name':'f','number': '591', 'street': '3rd', 'roadtype':'Ave', 'zip': '10016' }
TwoHundredGreene = {'name':'g','number': '200', 'street': 'Greene', 'roadtype':'St', 'zip': '07302' }
TwoTwoFiveThirtyNine = {'name':'h','number': '225', 'street': '39th', 'roadtype':'St', 'zip': '10016' }
FiveThreeOneMyrtle = {'name':'i','number': '531', 'street': 'Myrtle', 'roadtype':'Ave', 'zip': '11205' }
FiveOneFiveThirtyEighth = {'name':'j','number': '515', 'street': '38th', 'roadtype':'St', 'zip': '10018'}
SixtyWhite = {'name':'k','number': '60', 'street': 'White', 'roadtype':'St', 'zip': '10013' }
FourZeroThreeGreenwich = {'name':'l','number': '403', 'street': 'Greenwich', 'roadtype':'St', 'zip': '10013'}
OneSixOneColumbia = {'name':'m','number': '161', 'street': 'Columbia', 'roadtype':'St', 'zip': '11231' }
FourFiveZeroUnion = {'name':'n','number': '450', 'street': 'Union', 'roadtype':'St', 'zip': '11231' }
ThreeZeroEightThirtyEighth = {'name':'o','number': '308', 'street': '38th', 'roadtype':'St', 'zip': '10016' }

# LIST OF ALL DATA TO ALLOW FOR "FOR" Loop
prop_list = [
	EastTwentySecond
	,FiftyOneParkPlace,SeventyFiveKenmare,
	ThreeThreeThreeSchermerhorn,FiveNineFiveBaltic,
	FiveNineOneThirdAve,
	TwoHundredGreene, 
	TwoTwoFiveThirtyNine, 
	FiveThreeOneMyrtle, FiveOneFiveThirtyEighth, SixtyWhite, 
	FourZeroThreeGreenwich, OneSixOneColumbia,FourFiveZeroUnion,
	ThreeZeroEightThirtyEighth
]

# BEGINNING OF "for" LOOP THAT MAKES REQUEST FOR EACH prop IN prop_list 
# MAKES THE ZPID LIST FOR SECOND ROUND OF REQUESTS FOR INFO
zpid_list = []
for obj in prop_list:
	time.sleep(3)
	print(obj['name'])
	address_url = 'http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz19b6m5nu617_3jtqm&address='+obj['number']+'+'+obj['street']+'+'+obj['roadtype']+'&citystatezip='+obj['zip']
	results = requests.get(address_url).content
	decoded_results = results.decode(encoding='UTF-8')
	try:
		result_collection = xmltodict.parse(decoded_results)
		results_list = result_collection['SearchResults:searchresults']['response']['results']['result']
		for result in results_list:
			zpid_list.append(result['zpid'])
	except:
		print(" ")
		print("Name: ", obj['name'])
		print("Type: ", type(decoded_results))
		print("Length: ", len(decoded_results))
		print("Error occured: ", decoded_results)
		print(" ")

# ITERATE THROUGH ZPID LIST TO GRAB EXTENDED INFO 
print(zpid_list)
for zpid in zpid_list:
	zpid_url = 'http://www.zillow.com/webservice/GetDeepComps.htm?zws-id=X1-ZWz19b6m5nu617_3jtqm&zpid='+zpid+'&count=5'
	results = requests.get(zpid_url).content.decode(encoding='UTF-8')
	print("results:", results)

	
		




