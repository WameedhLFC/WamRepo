def Load_Database():

    import json
    import random
    from datetime import datetime
    from pymongo import MongoClient
    client = MongoClient()								# connect to the server.
    db = client["p0db"]								# returns an object pointing to the DB named "test".
    Coll_Ins_Many = db["Client_Info"]                         # WH create an object of the collection 

    a = ['96893250']
    d = ['Houston','Boston','Charlotte','New York','Chicago','Philadelphia','Los Angeles','San Antonio','Austin','Detroit','San Diego','Dallas','Phoenix','San Jose','Seattle','San Francisco','Denver','Nashville','Fortworth','El Paso']
    while (len(a)<1000):
        b = f'{random.randrange(1, 10**8):08}'
        if b not in a:
            a.append(b)
        
    u = []

    import json
    with open("Client_Info.json") as file:
        data = json.load(file)

    for i in range(len(data['Client_Info'])):
        n = a.pop()
        u.append(n)
        data['Client_Info'][i-1]['AccountID'] = n
        data['Client_Info'][i-1]['City'] = random.choice(d)
    result = Coll_Ins_Many.insert_many(data["Client_Info"]).inserted_ids

    collection = db["Transactions"]

    with open("Transactions.json") as file:
        data = json.load(file)

    q = ["transfer","withdraw","deposit"]

    year = ["2021","2020","2019"]
    month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    day = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15"\
        ,"16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
    t = []
    while (len(t)<1000):
        r = random.choice(year)+","+random.choice(month)+","+random.choice(day)
        t.append(r)

    p = ['96893250']
    while (len(p)<1000):
        b = f'{random.randrange(1, 10**8):08}'
        if b not in p:
            p.append(b)

    for i in range(len(data)):
        data[i-1]['TransacID'] = p.pop()
        data[i-1]['InitiatorID'] = random.choice(u)
        s = random.choice(q)
        data[i-1]['Type'] = s
        if s == "transfer":
            data[i-1]['ReceiverID'] = random.choice(u)
        else:
            data[i-1]['ReceiverID'] = ""
        data[i-1]['Date'] = random.choice(t)

    result = collection.insert_many(data).inserted_ids
