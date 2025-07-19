import os
import json

file="D:/PROJECT/CARVIO_v1/data/users.json"

def load_users():
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump({}, f)
    with open(file,"r") as f:
        return json.load(f)  

def save_users(users):
    with open(file, "w") as f:
        json.dump(users,f,indent=4)