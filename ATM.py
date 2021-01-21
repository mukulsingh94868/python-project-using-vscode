import time
print("please insert YOUR CARD")
time.sleep(5)
password = 1234
pin = int(input("enter your atm pin:"))
balance = 5000
two_thousand = 2000
if pin  == password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """
            )
        try:
            option = int(input("Please enter your choice:"))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"your current balance is {balance}")
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")
        if option == 2:
            withdraw_amount = int(input("please enter withdraw_amount:"))
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")

            print(f"your current balamce is {balance}:")
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")
            ok1 = int(withdraw_amount/500)
            print(ok1,"notes of 500 provides you")
            print("thank you visit again")

            
                          



        if option == 3:
            deposit_amount = int(input("please enter deposit_amount:"))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")
            print(f"your updated balance is {balance}")
            print("=======================================================")
            print("=======================================================")
            print("=======================================================")
        if option == 4:
            break                






else:
    print("wrong pin Please try again")                
