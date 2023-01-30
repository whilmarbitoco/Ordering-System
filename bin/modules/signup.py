import json


def signup(username, password):
    with open("bin/tlog.json", "r") as f:
        data = json.load(f)
    data["credentials"].append({
        "username": username,
        "password": password
    })
    with open("bin/tlog.json", "w") as f:
        json.dump(data, f)
    

