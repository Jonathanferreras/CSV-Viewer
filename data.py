import csv
def extractCsv(csv_name):
    reader = csv.DictReader(open('static/'+ csv_name, 'rb'))					#open csv file
    data = []																	#intialize empty array named 'data'
    for line in reader:                        									#creates array of dictionaries
    	data.append(line)														#append each dictionary from csv into 'data'
    fields = data[0].keys() 													#creates array of keys from 'data'

    return data, fields
