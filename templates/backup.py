from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/table1')
def table1():
    with open('static/Table1.csv', 'r') as inFile:
        read = csv.reader(inFile)
        data = [row for row in read]
        fields = data[0]
        del data[0]
    return render_template('table1.html', data = data, fields = fields)

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
