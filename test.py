import csv
reader = csv.DictReader(open('static/Table1.csv', 'rb'))
dict_list = []
for line in reader:
    dict_list.append(line)
fields = dict_list[0].keys()
data = []
for data_set in dict_list:
    temp = []
    for field in fields:
        temp.append(data_set[field])
    data.append(temp)
# reader = csv.DictReader(open('static/Table1.csv', 'rb'))
# dict_list = []
# for line in reader:
#     dict_list.append(line)
# print(dict_list)
# keys = dict_list[0].keys()
#
# secret = 'Boston'
# for data in dict_list:
#     for key in keys:
#         if data[key] == secret:
#             for key in keys:
#                 print(data[key])


# category = (drugs -> [benzo / pills, drug2, drug3], guns -> [machine gun, gun2, gun3], ...)
#
# data = {name -> [john, bob, mary, ...], product -> [benzo / pills, machine gun, poop]}
#
#
# user_input = input() #drugs
# sub_cat = category[user_input] #[benzo / pills, drug2, drug3]
# user_in2 = input() # benzo / pills
# sub_chosen = sub_cat[0]
#
# for key, value in data:
#     if data[product] has user_in2 ?:
#         print(name)
#         print(product)
#         print(location)
#         print(zipcode)
