import json


with open('bin/log.json', 'r') as f:
  data = json.load(f)
  
menu = data["log"]

def log(name, price, quantity, total, username):
    with open("bin/log.json", "r") as f:
        data = json.load(f)
    data["log"].append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total,
        "user": username
    })
    with open("bin/log.json", "w") as f:
        json.dump(data, f)



def getlog(uname):
  for item in menu:
    username = item['user']
    name= item['name']
    price = item['price']
    quantity = item['quantity']
    total = item['total']
    if uname == username:
      print(f"Name     : {username}")
      print(f"Item     : {name}")
      print(f"Price    : {price}")
      print(f"Quantity : {quantity}")
      print(f"Total    : {total}")
      print("\n")


