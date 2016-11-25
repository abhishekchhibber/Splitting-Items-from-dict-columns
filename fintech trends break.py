import csv
with open('Fintech.csv') as csvfile: #change here
	reader = csv.DictReader(csvfile)
	acts = [ ]
	for row in reader:
		acts.append(row)
print ("Original List length: "+ str(len(acts)))



newTrendList = [ ]


def trendcleaner(dataRow):

	dataRowTrend = dataRow['Trend']
	splitDataRowTrend = dataRowTrend.split(',')
	trendLength = len(splitDataRowTrend)

	for tL in range(0,trendLength):
		tempDict = { }
		tempTrend = splitDataRowTrend[tL]
		newDate = dataRow['Date']
		newSegement = dataRow['Segment']
		newTitle = dataRow['Title']
		newCountry = dataRow['Country']
		newTrend = tempTrend

		tempDict['Date'] = newDate
		tempDict['Segment'] = newSegement
		tempDict['Title'] = newTitle
		tempDict['Country'] = newCountry
		tempDict['Trend'] = newTrend
		# print(tempDict)
		newTrendList.append(tempDict)


	return (dataRow)


for act in acts:
	actTrend = act['Trend']
	if ',' in actTrend:
		trendcleaner(act)
	else:
		newTrendList.append(act)


print("List after Trends adjustment: "+str(len(newTrendList)))



newCountryList = [ ]

def countrycleaner(dataRow):

	dataRowCountry = dataRow['Country']
	splitDataRowCountry = dataRowCountry.split(',')
	countryLength = len(splitDataRowCountry)

	for cL in range(0,countryLength):
		tempDictTwo = { }
		tempCountry = splitDataRowCountry[cL]
		newDate = dataRow['Date']
		newSegement = dataRow['Segment']
		newTitle = dataRow['Title']
		newCountry = tempCountry
		newTrend = dataRow['Trend']

		tempDictTwo['Date'] = newDate
		tempDictTwo['Segment'] = newSegement
		tempDictTwo['Title'] = newTitle
		tempDictTwo['Country'] = newCountry
		tempDictTwo['Trend'] = newTrend
		# print(tempDict)
		newCountryList.append(tempDictTwo)


	return (dataRow)




for newTrendListItem in newTrendList:
	actCountry = newTrendListItem['Country']
	if ',' in actCountry:
		countrycleaner(newTrendListItem)
	else:
		newCountryList.append(newTrendListItem)


print("List after Country adjustment: "+str(len(newCountryList)))





newSegmentList = [ ]

def segmentcleaner(dataRow):

	dataRowSegment = dataRow['Segment']
	splitDataRowSegment = dataRowSegment.split(',')
	segmentLength = len(splitDataRowSegment)

	for cL in range(0,segmentLength):
		tempDictThree = { }
		tempSegment = splitDataRowSegment[cL]
		newDate = dataRow['Date']
		newCountry = dataRow['Country']
		newTitle = dataRow['Title']
		newSegment = tempSegment
		newTrend = dataRow['Trend']

		tempDictThree['Date'] = newDate
		tempDictThree['Segment'] = newSegment
		tempDictThree['Title'] = newTitle
		tempDictThree['Country'] = newCountry
		tempDictThree['Trend'] = newTrend
		# print(tempDict)
		newSegmentList.append(tempDictThree)


	return (dataRow)




for newCountryListItem in newCountryList:
	actSegment = newCountryListItem['Segment']
	if ',' in actSegment:
		segmentcleaner(newCountryListItem)
	else:
		newSegmentList.append(newCountryListItem)


print("List after Segment adjustment: "+str(len(newSegmentList)))





with open('fintech_final.csv', 'w', encoding='utf-8', newline = '') as csvfile: #change here
    fieldnames = ['Title','Date','Segment','Country','Trend']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in newSegmentList:
    	writer.writerow(val)

