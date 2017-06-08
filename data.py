import csv

categories = {'categoryA': ['aa', 'ab', 'ac'], 'categoryB': ['bb', 'ba', 'bc'], 'categoryC': ['cc', 'ca', 'cb']}
category = categories.keys()
for key in category:
    print(categories[key])
# reader = csv.DictReader(open('static/Table1.csv', 'rb'))
# data = []
# for line in reader:                             #creates array of dictionaries
# 	data.append(line)
# fields = data[0].keys()                    #creates array of keys from data
#
# for group in data:
#     for field in fields:
#         print(group[field])
