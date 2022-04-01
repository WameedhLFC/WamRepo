from BankDB import *           
import random
import re
import pprint
from bson import ObjectId
from pymongo import MongoClient
client = MongoClient()
db = client["p0db"]

def View_Account():                                     # Option 2
    AccountID = input("Enter account number: ")
    while AccountID not in Account_ID_Validation():
        AccountID = input("Invalid!! Enter 8-digit account number: ")
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in collection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        print(f'AccountID: {doc["AccountID"]}  First Name: {doc["FirstName"]}  Last Name: {doc["LastName"]}  Email: {doc["email"]}  City:{doc["City"]}  Balance: {doc["Balance"]}')

def Deposit():                                              # Option 3
    AccountID = input("Enter account number: ")
    while AccountID not in Account_ID_Validation():
        AccountID = input("Invalid!! Enter 8-digit account number: ")
    amount = Amount_Float_Positive()
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    collection = db["Transactions"]
    for doc in dcollection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = float(amount) + doc["Balance"]
        dcollection.update_one({"AccountID":AccountID}, {"$set": {"Balance":Balance}})
        print(f'Amount deposited successfully. Your balance is: {Balance}')
    collection.insert_one({"TransacID":Create_Transaction_ID(),"InitiatorID":AccountID,"Type":"deposit","ReceiverID":"","Date":Create_Date(),"Amount":float(amount)})

def Withdraw():                                                # Option 4
    AccountID = input("Enter account number: ")
    while AccountID not in Account_ID_Validation():
        AccountID = input("Invalid!! Enter 8-digit account number: ")
    
    # global collection
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    collection = db["Transactions"]
    for doc in dcollection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        while(True):
            amount = Amount_Float_Positive()
            if float(amount) > doc["Balance"]:
                print(f'Insufficient balance of {doc["Balance"]}')
                continue
            else:
                break
        Balance = doc["Balance"] - float(amount)
        dcollection.update_one({"AccountID":AccountID}, {"$set": {"Balance":Balance}})
        print(f'Amount withdrawn successfully. Your balance is: {Balance}')
    collection.insert_one({"TransacID":Create_Transaction_ID(),"InitiatorID":AccountID,"Type":"withdraw","ReceiverID":"","Date":Create_Date(),"Amount":float(amount)})

def Transfer():                                                # Option 5
    SenderID = input("Enter your account number: ")
    while SenderID not in Account_ID_Validation():
        SenderID = input("Invalid!! Enter 8-digit account number: ")    
    ReceiverID = input("Enter recepient's account number: ")
    while ReceiverID not in Account_ID_Validation():
        ReceiverID = input("Invalid!! Enter 8-digit account number: ")
    # amount = float(input("Enter amount to transfer: "))
    # global collection
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    collection = db["Transactions"]
    for doc in dcollection.find({"AccountID":SenderID}):        # find docs where "size = 2", iterate thru the search results.
        while(True):
            amount = Amount_Float_Positive()
            if float(amount) > doc["Balance"]:
                print(f'Insufficient balance of {doc["Balance"]}')
                continue
            else:
                break
        Balance = doc["Balance"] - float(amount)
        dcollection.update_one({"AccountID":SenderID}, {"$set": {"Balance":Balance}})
    print(f'Amount Transferred successfully. Your balance is: {Balance}')

    collection.insert_one({"TransacID":Create_Transaction_ID(),"InitiatorID":SenderID,"Type":"transfer","ReceiverID":ReceiverID,"Date":Create_Date(),"Amount":float(amount)})

    for doc in dcollection.find({"AccountID":ReceiverID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = doc["Balance"] + float(amount)
        dcollection.update_one({"AccountID":ReceiverID}, {"$set": {"Balance":Balance}})

def Close_Account():                                     # Option 6
    AccountID = input("Enter account number: ")
    while AccountID not in Account_ID_Validation():
        AccountID = input("Invalid!! Enter 8-digit account number: ")
    # global collection
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in collection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        print(f'AccountID: {doc["AccountID"]}  closed successfully.')
        collection.delete_one({"AccountID":AccountID})

def Create_Account():                        # Option 7
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    c = []                                   # list c stores all AccountID's to ensure newly created accounts have unique Account ID's
    for doc in collection.find({}):          # find docs where "size = 2", iterate thru the search results.
        c.append(doc["AccountID"])
    while (True):
        AccountID = f'{random.randrange(1, 10**8):08}'
        if AccountID in c:
            continue
        else:
            #print (AccountID)
            break
    while True:
        FirstName = input("Enter your first name: ")
        if FirstName.isalpha():
            break
        print ("Invalid first name!!")
    while True:
        LastName = input("Enter your last name: ")
        if LastName.isalpha():
            break
        print ("Invalid last name!!")
    while True:
        email = input("Enter your email: ")
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_regex.match(email):
            # print("Email address invalid")
            break
        else:
            print("Invalid Email!!")
            continue
    con = False
    while con!=True:
        l=0
        City = input("Enter your city: ")
        # strs = input('Enter your Name: ')
        for i in City:
            if i.isalpha() or i.isspace():
                l += 1
        if l == len(City):
            con = True    
            break
        else:
            # print('Wrong Input')
            print ("Invalid city name!!")
            continue   
    Balance = float(0)
    collection.insert_one({"AccountID":AccountID,"FirstName":FirstName,"LastName":LastName,"email":email,"City":City,"Balance":Balance})
    print (f'\nAccount created successfully. Your account number is: {AccountID}\n')

def Show_Customer_Accounts():                # Option 8
    # global collection
    collection = db["Client_Info"]           # WH returns an object to the collection named "Client_Info"
    counter=0
    for doc in collection.find({}):          # Loop through all documents in Collection Client_Info
        counter+=1
        print(f'Account Number: {doc["AccountID"]}  First Name: {doc["FirstName"]}  Last Name: {doc["LastName"]} \
Email: {doc["email"]} City:{doc["City"]}  Balance: {doc["Balance"]}')
    print(f'\nMy Bank has a total of {counter} customer accounts\n')

def Show_Transactions():                                 # Option 9
    # global collection
    collection = db["Transactions"]                  # WH returns an object to the collection named "Client_Info"
    counter=0
    for doc in collection.find({}).sort("Date",1):        # Loop through all documents in Collection Client_Info
        counter+=1
        print(f'Transac ID: {doc["TransacID"]}  Initiator ID: {doc["InitiatorID"]}  Type: {doc["Type"]} \
Receiver ID: {doc["ReceiverID"]} Date: {doc["Date"]}  Amount: {doc["Amount"]}')
    print(f'\nMy Bank has a total of {counter} Transactions\n')

def Show_Account_Transactions():                            # Option 10
    AccountID = input('Enter your account ID: ')
    while AccountID not in Account_ID_Validation():
        AccountID = input("Invalid!! Enter 8-digit account number: ")
    collection = db["Transactions"]
    counter = 0
    for doc in collection.find({"$or": [{"InitiatorID":AccountID}, {"ReceiverID":AccountID}] }).sort("Date",1):        # Loop through all documents in Collection Client_Info
        counter += 1
        print(f'Transac ID: {doc["TransacID"]}  Initiator ID: {doc["InitiatorID"]}  Type: {doc["Type"]} \
Receiver ID: {doc["ReceiverID"]} Date: {doc["Date"]}  Amount: {doc["Amount"]}')
    dcollection = db["Client_Info"]
    for doc in dcollection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        print (f'{doc["FirstName"]} {doc["LastName"]} had {counter} transaction on account number: {AccountID} ')

def Create_Date():
    from datetime import datetime
    return str(datetime.now())[:4]+","+str(datetime.now())[5:7]+","+str(datetime.now())[8:10]

def Create_Transaction_ID():
    collection = db["Transactions"]                  # WH returns an object to the collection named "Client_Info"
    c = []                                 # list c stores all AccountID's to ensure newly created accounts have unique Account ID's
    for doc in collection.find({}):        # find docs where "size = 2", iterate thru the search results.
        c.append(doc["TransacID"])
    while (True):
        TransacID = f'{random.randrange(1, 10**8):08}'
        if TransacID in c:
            continue
        else:
            #print (AccountID)
            break
    return TransacID

def Account_ID_Validation():
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    c = []                                 # list c stores all AccountID's to ensure newly created accounts have unique Account ID's
    for doc in collection.find({}):        # find docs where "size = 2", iterate thru the search results.
        c.append(doc["AccountID"])
    return c

def Amount_Float_Positive():
    # global amount
    amount = input("Enter amount: ")
    while (True):
        try:
            # amount = float(input("Enter amount to deposit: "))
            float(amount)
            # print("Number is a float")
        except:
            amount = input("Invalid!! Enter amount: ")
            continue
        else:
            if float(amount) >= 0:
                # print ("Number is positive")
                break
            else:
                amount = input ("Amount must be greater than zero. Enter amount: ")
                continue
    return amount
    