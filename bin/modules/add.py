import json


with open('bin/tadd.json', 'r') as f:
  data = json.load(f)
  
menu = data["log"]

def additem(ids, name, price):
    with open("bin/log.json", "r") as f:
        data = json.load(f)
    data["log"].append({
        "id": ids,
        "name": name,
        "price": price,
    })
    with open("bin/log.json", "w") as f:
        json.dump(data, f)



