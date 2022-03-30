from P0Connect import *
from P0RetrieveII import *

while (True):
    print("\n################### Welcome to My Bank ###################")
    print("Enter one of the following options: \n (1) Load Database \n (2) View Account \
        \n (3) Deposit \n (4) Withdraw \n (5) Transfer \n (6) Close Account \n (7) Create Account \
        \n (8) Show Customer Accounts \n (0) Exit")
    print("###########################################################")
    x = input("Enter option number: ")



    if x == "1":
        Load_Database()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "2":
        View_Account()
        # x1 = User("Wameedh",42,"Male")              # WH try x1.show_details("Wameedh",42,"Male")
        # x1.show_details()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "3":
        Deposit()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "4":
        Withdraw()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "5":
        Transfer()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "6":
        Close_Account()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            break

    elif x == "7":
        Create_Account(AccountID="AccountID",FirstName="Name",LastName="Name",email="email",City="City")     
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "8":
        Show_Customer_Accounts()
        y = input("Continue? (Y/N): ")
        if y == "Y":
            continue
        elif y == "N":
            print("\nThanks for using My Bank\n")
            break

    elif x == "0":
        print("\nThanks for using My Bank\n")
        break








    

