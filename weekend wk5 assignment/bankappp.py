import random
from datetime import datetime

data = {}

def deposit(amount:float, past_bal:float):
    new_bal = amount+past_bal
    return new_bal



def withdraw(amount:float, past_bal:float):
    if amount > past_bal:
        print("Insuffucient funds")
    else:
        new_bal = past_bal-amount
        return new_bal


def account_num():
    begin = "0"
    for _ in range(9):
        begin+=str(random.choice(range(10)))
        
   

    return begin


print("====== Welcome to the GeeBanks ======")

def Accquestion():
    Accquestion= int(input("do you have an account with us: 1 (yes) 2 (no) \n"))

    if Accquestion == 1:
        acc_num = input('Account Number:\n>')
        pin = input('Login Pin:\n>')

        user_data = data.get(acc_num)

        if user_data and user_data.get("pin") == pin:
            print("$$$$$-- Login Successful--$$$$$")
            first_login = True 
            
            while True:
                if first_login:
                    print(f"Welcome, {user_data['name']}")
                    first_login = False
                    print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer. \n(5) exit")
                    input_ = input(":>>")
                    
                    if input_ == "1":
                        amount = float(input("Amount:\n>"))
                        trans_pin = input("Transaction Pin:\n>")
                        if trans_pin == user_data['trans_pin']:
                            amt = deposit(amount, user_data['bal'])
                            user_data['bal'] = amt
                            
                            print("do you want to perfom another transaction? (1) yes (2) no")
                            input_again = input(":>>")
                            if input_again == "1":
                                print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")
                            elif input_again == "2":
                                print("Bye!!!!")
                            else:
                                print("invalid input")
                        else:
                            print("Invalid pin value")
                        
                    elif input_ == "2":
                            amount = float(input("Amount:\n>"))

                            try:
                                new_bal = withdraw(amount, user_data['bal']
                                        )
                                user_data['bal'] = new_bal
                                print("do you want to perfom another transaction? (1) yes (2) no")
                                input_again = input(":>>")
                                if input_again == "1":
                                    print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")

                                elif input_again == "2":
                                    print("Bye!!!!")
                                else:
                                    print("invalid input")
                            except ValueError as msg:
                                print(msg)
                                
                    elif input_ == '3':
                            current_date = datetime.now().date()
                            date = current_date.strftime("%a, %d of %B, %Y")
                            print(f"Your current balance at {date} is {user_data['bal']}")
                            
                            print("do you want to perfom another transaction? (1) yes (2) no")
                            input_again = input(":>>")
                            if input_again == "1":
                                print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")

                            elif input_again == "2":
                                print("Bye!!!!")
                            else:
                                print("invalid input")
                        
                    elif input_ == '4':
                            other_acc = input("Enter Account number\n:>> ")
                            trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                            trans_pin = input("Enter transaction pin:\n>")

                            beneficiary = data.get(other_acc) 
                        
                            if beneficiary:
                                if trans_amount > user_data['bal']:
                                    print("Insufficient Funds")
                                else:   
                                    if trans_pin == user_data['trans_pin']:
                                        user_data['bal'] -= trans_amount 

                                        beneficiary['bal'] += trans_amount 

                                        print("\nTransfer Successful")
                                    else:
                                        print("Incorrect pin.")
                    

                    elif input_ == "5":
                        break        
                else:
                    print(f"Welcome back, {user_data['firstname']}")
        else:
            print("Invalid credentials.")
        
        


        
    elif Accquestion == 2:
            print("$$$$$-- Register --$$$$$$")
            while True:
                first_name = input('First Name:\n>') 
                last_name = input('Last Name:\n>')
                pin = input('Login Pin:\n>')
                trans_pin = input('Transaction Pin:\n>')
                acc_num = account_num()
                print("====== Creating Account ====")
                print('Successful')
            

                
                data[acc_num] = {
                    'first name' : first_name,
                    'last name': last_name,
                    'Login_pin' : pin,
                    'trans_pin' : trans_pin,
                    'bal' :0,
                }

            
                print(f"""\nWelcome, {first_name}!
        You have successfully created your account. Your account number is {acc_num}. """)
                print('\n', data)
                acc_num = input('Account Number:\n>')
                pin = input('Login Pin:\n>')

                user_data = data.get(acc_num)

                if user_data and user_data.get("Login_pin") == pin:
                    print("Login Successful")
                    first_login = True 
                    while True:
                        if first_login:
                            print(f"Welcome, {first_name}")
                            first_login = False
                            print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")
                            input_ = input(":>>")
                            if input_ == "1":
                                amount = float(input("Amount:\n>"))
                                trans_pin = input("Transaction Pin:\n>")
                                if trans_pin == user_data['trans_pin']:
                                    amt = deposit(amount, user_data['bal'])
                                    user_data['bal'] = amt
                                    print("do you want to perfom another transaction? (1) yes (2) no")
                                    input_again = input(":>>")
                                    if input_again == "1":
                                        print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")
                                        
                                    elif input_again == "2":
                                        print(f"{user_data('firstname')} Bye")
                                    else:
                                        print("invalid input")
                                else:
                                    print("Invalid pin value")
                                
                            elif input_ == "2":
                                    amount = float(input("Amount:\n>"))

                                    try:
                                        new_bal = withdraw(amount, user_data['bal']
                                                )
                                        user_data['bal'] = new_bal
                                        print("do you want to perfom another transaction? (1) yes (2) no")
                                        input_again = input(":>>")
                                        if input_again == "1":
                                            print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")
                                        
                                        elif input_again == "2":
                                            print("bye!!")
                                        else:
                                            print("invalid input")
                                    except ValueError as msg:
                                        print(msg)
                                        
                            elif input_ == '3':
                                    current_date = datetime.now().date()
                                    date = current_date.strftime("%a, %d of %B, %Y")
                                    print(f"Your current balance at {date} is {user_data['bal']}")
                                    print("do you want to perfom another transaction? (1) yes (2) no")
                                    input_again = input(":>>")
                                    if input_again == "1":
                                        print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer (5) exit")
                                
                                    elif input_again == "2":
                                        print("Bye")
                                    else:
                                        print("invalid input")
                                
                            elif input_ == '4':
                                    other_acc = input("Enter Account number\n:>> ")
                                    trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                                    trans_pin = input("Enter transaction pin:\n>")

                                    beneficiary = data.get(other_acc) 
                                
                                    if beneficiary:
                                        if trans_amount > user_data['bal']:
                                            print("Insufficient Funds")
                                        else:   
                                            if trans_pin == user_data['trans_pin']:
                                                user_data['bal'] -= trans_amount 

                                                beneficiary['bal'] += trans_amount 

                                                print("\nTransfer Successful")
                                            else:
                                                print("Incorrect pin.")
                            

                            elif input_ == "5":
                                break        
                        else:
                            print(f"Welcome back, {user_data['name']}")
                else:
                    print("Invalid credentials.")
                #Accquestion()
    else:
        print("You have selected invalid output")
        
        
Accquestion()
    
    
with open("C:/Users/hp/Desktop/bankfiles.txt", 'w') as files:
        files.write("=========")
        files.write(data)
        # files.write(f'{acc_number}.\n"first name": {first_name}.\n"last_name": {last_name}.\n"login pin": {login_pin}.\n"transaction pin": {transaction_pin}.\n"balance":{balance}')
        files.write("=========")

    

    


