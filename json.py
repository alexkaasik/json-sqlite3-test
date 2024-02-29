import json

json_data='{ "name":"Alex", "age":30, "city":"Tallinn"}'

data_= json.loads(json_data)

for id_,data in enumerate(data_):
    print(id_," ", data)

for key,value in data_.items():
    print(key,value)
