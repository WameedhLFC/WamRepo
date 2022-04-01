from BankDB import *
from BankFunctions import *

def Menu():  
    print("\n################### Welcome to My Bank ###################")
    print("Enter one of the following options: \n (1) Load Database \n (2) View Account \
        \n (3) Deposit \n (4) Withdraw \n (5) Transfer \n (6) Close Account \n (7) Create Account \
        \n (8) Show Customer Accounts  \n (9) Show Transactions \n (10) Show Account Transactions \n (0) Exit")
    print("###########################################################")

Menu()

while (True):

    x = input("Enter option number: ")

    if x == "1":
        Load_Database()
        print("Database loaded successfully")
        while True:
            y = input("Continue? (Y/N): ")
            if y not in ["Y","N"]:
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "2":
        View_Account()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break         

    elif x == "3":
        Deposit()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break         

    elif x == "4":
        Withdraw()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break 

    elif x == "5":
        Transfer()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break         

    elif x == "6":
        Close_Account()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break         

    elif x == "7":
        Create_Account() 
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break        

    elif x == "8":
        Show_Customer_Accounts()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "9":
        Show_Transactions()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "10":
        Show_Account_Transactions()
        while True:
            y = input("Continue? (Y/N): ")
            # yn = ["Y","N"]
            if y not in ["Y","N"]:
                print("Invalid entry!!")
                continue
            else:
                break 
        if y == "Y":
            Menu()
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "0":
        print("\nThanks for using My Bank\n")
        break

    else:
        print("Invalid Entry!")
        continue
