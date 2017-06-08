from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/table1')
def table1():
	categories = {'categoryA': ['aa', 'ab', 'ac'],
				  'categoryB': ['bb', 'ba', 'bc'],
				  'categoryC': ['cc', 'ca', 'cb']}
	category_titles = categories.keys()

	reader = csv.DictReader(open('static/Table1.csv', 'rb'))					#open csv file
	data = []																	#intialize empty array named 'data'
	for line in reader:                        									#creates array of dictionaries
		data.append(line)														#append each dictionary from csv into 'data'
	fields = data[0].keys() 													#creates array of keys from 'data'
	return render_template('table1.html', data = data, fields = fields, category_titles = category_titles, categories = categories)

@app.route('/table2')
def table2():
    with open('static/Table2.csv', 'r') as inFile:
        read = csv.reader(inFile)
        data = [row for row in read]
        fields = data[0]
        del data[0]
    return render_template('table2.html', data = data, fields = fields)

@app.route('/table3')
def table3():
    with open('static/Table3.csv', 'r') as inFile:
        read = csv.reader(inFile)
        data = [row for row in read]
        fields = data[0]
        del data[0]
    return render_template('table3.html', data = data, fields = fields)

if __name__ == "__main__":
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
