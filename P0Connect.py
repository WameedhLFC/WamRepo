from pymongo import MongoClient
client = MongoClient()								# connect to the server.
db = client["p0db"]								# returns an object pointing to the DB named "test".

def Load_Database():
    import json
    import random

    Coll_Ins_Many = db["Client_Info"]                         # WH create an object of the collection 
    
    a = ['96893250']
    d = ['Houston','Boston','Charlotte','New York','Chicago','Philadelphia','Los Angeles','San Antonio',\
        'Austin','Detroit','San Diego','Dallas','Phoenix','San Jose','Seattle','San Francisco','Denver',\
            'Nashville','Fortworth','El Paso']
    while (len(a)<1000):
        b = f'{random.randrange(1, 10**8):08}'
        if b not in a:
            a.append(b)

    import json
    with open("Client_Info.json") as file:
        data = json.load(file)

    for i in range(len(data['Client_Info'])):
        data['Client_Info'][i-1]['AccountID'] = a.pop()
        data['Client_Info'][i-1]['City'] = random.choice(d)
    result = Coll_Ins_Many.insert_many(data["Client_Info"]).inserted_ids

