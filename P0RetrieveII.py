from P0Connect import *             # Check if the leak is coming through this import
from InsertOne import *
from UpdateOne import *
import random
import pprint
from bson import ObjectId
from pymongo import MongoClient


def Show_Customer_Accounts():                                 # Option 8
    # global collection
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    counter=0
    for doc in collection.find({}):        # Loop through all documents in Collection Client_Info
        counter+=1
        print(f'Account Number: {doc["AccountID"]}  First Name: {doc["FirstName"]}  Last Name: {doc["LastName"]}  Email: {doc["email"]} City:{doc["City"]}  Balance: {doc["Balance"]}')
    print(f'\nMy Bank has a total of {counter} customer accounts\n')


def Show_Account_Transactions():
    tcollection = db["Transactions"]                  # WH returns an object to the collection named "Transactions"
    collection = db["Client_Info"] 
    for doc in collection.find({}):        # find docs where "size = 2", iterate thru the search results.
        for tdoc in tcollection.find({}):
            if tdoc["AccID"] == doc["AccountID"]:
                print (f'{doc["FirstName"]} made a transaction ')
                continue

        #print(f'First Name: {tdoc["FirstName"]}  Last Name: {tdoc["LastName"]}    Email: {tdoc["email"]}   City:{tdoc["City"]}')

def Create_Account(AccountID,FirstName,LastName,email,City):
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    c = []                                 # list c stores all AccountID's to make sure newly created accounts have unique Account ID's
    for doc in collection.find({}):        # find docs where "size = 2", iterate thru the search results.
        c.append(doc["AccountID"])
    while (True):
        AccountID = f'{random.randrange(1, 10**8):08}'
        if AccountID in c:
            continue
        else:
            #print (AccountID)
            break
    FirstName = input("Enter your first name: ")
    LastName = input("Enter your last name: ")
    email = input("Enter your email: ")
    City = input("Enter your city: ")
    
    Balance = float(0)
    Instert(AccountID,FirstName,LastName,email,City,Balance)
    print (f'\nAccount created successfully. Your account number is: {AccountID}\n')

    # for doc in collection.find({}):        # find docs where "size = 2", iterate thru the search results.
    #     if doc["AccountID"] not in a:
    #         a.append(doc["AccountID"])
    #         continue
    # print(a)
    # AccountID = input("Enter your account ID: ")
    # while True:       # find docs where "size = 2", iterate thru the search results.

    #     if doc["AccountID"] in a:
    #         AccountID = input("Invalid account ID. Enter a different account ID: ")
    #         continue
    #     else:
    #         a.append(doc["AccountID"])
    #         break     
    # FirstName = input("Enter your first name: ")
    # LastName = input("Enter your last name: ")
    # email = input("Enter your email address: ")
    # City = input("Enter your city: ")

    # collection.insert({"AccountID":AccountID, "FirstName":FirstName, "LastName":LastName, "email":email, "City":City})
    # print("\n Account created successfully\n")

def View_Account():                                     # Option 2
    AccountID = input("Enter account number: ")
    # global collection
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in collection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        print(f'AccountID: {doc["AccountID"]}  First Name: {doc["FirstName"]}  Last Name: {doc["LastName"]}  Email: {doc["email"]}  City:{doc["City"]}  Balance: {doc["Balance"]}')

def Close_Account():                                     # Option 6
    AccountID = input("Enter account number: ")
    # global collection
    collection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in collection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        print(f'AccountID: {doc["AccountID"]}  closed successfully.')
        collection.delete_one({"AccountID":AccountID})

def Deposit():
    AccountID = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    # global collection
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in dcollection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = amount + doc["Balance"]
        Update(AccountID,Balance)
        print(f'Amount deposited successfully. Your balance is: {Balance}')

def Withdraw():
    AccountID = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    # global collection
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in dcollection.find({"AccountID":AccountID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = doc["Balance"] - amount
        dcollection.update_one({"AccountID":AccountID}, {"$set": {"Balance":Balance}})
        print(f'Amount withdraw successfully. Your balance is: {Balance}')

def Transfer():
    SenderID = input("Enter your account number: ")
    ReceiverID = input("Enter recepient's account number: ")
    amount = float(input("Enter amount to transfer: "))
    # global collection
    dcollection = db["Client_Info"]                  # WH returns an object to the collection named "Client_Info"
    for doc in dcollection.find({"AccountID":SenderID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = doc["Balance"] - amount
        dcollection.update_one({"AccountID":SenderID}, {"$set": {"Balance":Balance}})

    print(f'Amount Transferred successfully. Your balance is: {Balance}')

    for doc in dcollection.find({"AccountID":ReceiverID}):        # find docs where "size = 2", iterate thru the search results.
        Balance = doc["Balance"] + amount
        dcollection.update_one({"AccountID":ReceiverID}, {"$set": {"Balance":Balance}})
