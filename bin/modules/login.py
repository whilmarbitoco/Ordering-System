import json


with open('bin/tlog.json', 'r') as f:
  data = json.load(f)
  
menu = data["credentials"]


def getcred(uname, upass):
  for item in menu:
    name= item['username']
    password = item['password']
    if uname == name:
      if upass == password:
        return True

    
    


