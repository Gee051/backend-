import random
from datetime import datetime


data = {}
def register():
    # with open("Bankfiles.txt", "r") as file:
    #     data = eval(file.read())
        
    print("$$$$$-- Register --$$$$$$")
    while True:
        first_name = input('First Name:\n>')
        if  first_name.isalpha() != True:
            print("first_name should be a valid name")
            register()
            return None
           
        else:
            last_name = input('Last Name:\n>')
            if  last_name.isalpha() != True:
                print("first_name should be a valid name")
                register()
                return None
            else:
                login_pin = input('Login Pin:\n>')
                transaction_pin = int(input('transaction Pin:\n>'))
                acc_num = account_num()
                print("====== Creating Account ====")
                print('Successful')
            

   
        data[acc_num] = {
            'first_name' : first_name,
            'last_name': last_name,
            'login_pin' : login_pin,
            'transaction_pin' : transaction_pin,
            'bal' :0,
        }

            
        print(f"""\nWelcome, {first_name}!You have successfully created your account. Your account number is {acc_num}. """)
        print('\n', data)
    
        break
    login()


def login():
    acc_num = input('Account Number:\n>')
    # pin = input('Login Pin:\n>')
    user_data = data.get(acc_num)
    if user_data:
        if data.get(acc_num) :
            first_login = True
            print("$$$$$-- Login Successful--$$$$$")
            # first_login = True 
                    
            while True:
                    if first_login:
                        # user_data = data
                        print(f"Welcome, {user_data['first_name']}")
                        first_login = False
                        print("what would you like to do.\n (1) deposit .\n (2) withdraw .\n (3) checkbalance. \n (4) transfer. \n(5) exit")
                        input_ = int(input(":>>"))
                        if input_ == 1:
                            deposit()
                            
                        elif input_ == 2:
                            withdraw()
                            
                        elif input_ == 3:
                            checkbalance()
                            
                        elif input_ == 4:
                            transfer()
                            
                        elif input_ == 5:
                            exit()
                        
                            
                        else: 
                            print("invalid option")
                            login()
                        break            
                            
                    else:
                        print(f"Welcome back, {user_data['first_name']}")
                        
        else:
            print("Invalid account number")
        #login()
          
def account_num():
    begin = "0"
    for _ in range(9):
        begin+=str(random.choice(range(10)))
        
    return begin
        

           
def deposit():
    acc_num = input('Account Number:\n>')
    user_data = data.get(acc_num)
    amount = float(input("Enter Amount you will like to deposit:\n>"))
    transaction_pin = input("transaction Pin:\n>")
    if user_data['transaction_pin'] == transaction_pin:
    
            # amt = deposit(amount, user_data['bal'])
            # user_data['bal'] += amount
        print(f"{amount} deposited")
        user_data['bal']+= amount
        exit()
        
    else:
        print("Invalid transaction pin")
        exit()



def withdraw():
    acc_num = input('Account Number:\n>')
    user_data = data.get(acc_num)
    amount = float(input("Enter Amount you will like to withdraw:\n>"))
    transaction_pin = input("transaction Pin:\n>")
    if user_data['transaction_pin'] == transaction_pin:
        if amount > user_data['bal']:
            print(f"{amount} withdrawn")
            user_data['bal']-= amount
        else:
            print("Insufficient funds")
            exit()
        
    else:
        print("Invalid transaction pin")
        exit()



        
def checkbalance():
    acc_num = input('Account Number:\n>')
    user_data = data.get(acc_num)
    # current_date = datetime.now().date()
    # date = current_date.strftime("%a, %d of %B, %Y")
    # print(f"Your current balance at {date} is {user_data['bal']}")
    
    now = datetime.now()                      
    print(now.strftime(f"Your current balance at %d%m%y  {now.hour}:{now.minute} hours is {user_data['bal']}.")) 
    exit()
    return now.isoformat() 
    
    
    
        
   

def transfer():
    acc_num = input('Account Number:\n>')
    user_data = data.get(acc_num)
    other_acc = input("Enter account number of the receiver \n:>> ")
    transaction_amount = int(input("Enter Amount you want to transfer\n:>> "))
    transaction_pin = input("Enter transaction pin:\n>")

    beneficiary = data.get(other_acc) 
                                
    if beneficiary:
        if transaction_amount > user_data['bal']:
            print("Insufficient Funds")
        else:   
            if transaction_pin == user_data['transaction_pin']:
                user_data['bal'] -= transaction_amount 
                beneficiary['bal'] += transaction_amount 
                print("\n$$$$$-- transfer Successful-- $$$$$")
            else:
                print("Incorrect pin.")
                exit()
                
        exit()
                            
                           
def exit():
    acc_num = input('Account Number:\n>') 
    user_data = data.get(acc_num) 
    exit_input=int(input("Would you like to perform another transactionaction \n (1) Yes  (2) No "))
    if exit_input == 1:
        login()
        
    elif exit_input == 2:
        print(f"{user_data['first_name']} Bye")
        
        # with open("Bankfiles.txt", "w") as file:
        #         file.write(str(data))
    
        
    else:
        print("Invalid input")
        exit()
        




print("====== Welcome to the GeeBanks ======")
def Accquestion():
    Accquestion= int(input("do you have an account with us: 1 (yes) 2 (no) \n"))

    if Accquestion == 1:
        login()
        
    elif Accquestion == 2:
        register()
        
    else: 
        print("invalid input")

Accquestion()

    

    


