from flask import Flask, render_template, request
from data import extractCsv
import csv
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def home():
	return render_template('index.html')

@app.route('/table1')
def table1():
	categories = {'categoryA': ['aa', 'ab', 'ac'],
				  'categoryB': ['bb', 'ba', 'bc'],
				  'categoryC': ['cc', 'ca', 'cb']}
	category_titles = categories.keys()
	data, fields = extractCsv('Table1.csv')
	return render_template('tables.html',
							data = data,
							fields = fields,
							category_titles = category_titles,
							categories = categories)

@app.route('/table2')
def table2():
	categories = {'categoryA': ['aa', 'ab', 'ac'],
				  'categoryB': ['bb', 'ba', 'bc'],
				  'categoryC': ['cc', 'ca', 'cb']}
	category_titles = categories.keys()
	data, fields = extractCsv('Table2.csv')

	return render_template('tables.html',
							data = data,
							fields = fields,
							category_titles = category_titles,
							categories = categories)

@app.route('/table3')
def table3():
	categories = {'categoryA': ['aa', 'ab', 'ac'],
				  'categoryB': ['bb', 'ba', 'bc'],
				  'categoryC': ['cc', 'ca', 'cb']}
	category_titles = categories.keys()
	data, fields = extractCsv('Table3.csv')

	return render_template('tables.html',
							data = data,
							fields = fields,
							category_titles = category_titles,
							categories = categories)
if __name__ == "__main__":
    TEMPLATES_AUTO_RELOAD = True
    app.run(debug=True)
