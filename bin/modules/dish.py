import json

with open('bin/foods.json', 'r') as f:
  data = json.load(f)
  
menu = data["dish"]

def getprice(cname):
  for item in menu:
    name = item['name']
    price = item['price']
    if name == cname:
      return price

def getid(cname):
  for item in menu:
    name = item['name']
    ids = item['id']
    price = item['price']
    if ids == cname:
      return int(price)

def getnamebyid(cid):
  for item in menu:
    ids = item['id']
    name = item['name']
    price = item['price']
    if ids == cid:
      return [name, price]

def getall():
  for item in menu:
    ids = item['id']
    name = item['name']
    price = item['price']
    print(f"[{ids}] {name} | price: {price}")


