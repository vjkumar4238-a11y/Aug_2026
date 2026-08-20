# from datetime import datetime
# class account:
#     def __init__(self,username,password,balance=0):
#         self.username=username
#         self.password=password
#         self.balance=balance
#         self.transactions=[]

#     def deposit(self,amount):
#         self.balance+=amount
#         self.transactions.append((datetime.now(),f"deposited {amount}"))
#         print(f"\namount deposited: {amount}\ntotal balance {self.balance}")
              
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             self.transactions.append((datetime.now(),f"withdraw {amount}"))
#             print(f"\namount debited:{amount}\nremaining balance{self.balance}")
#         else:
#             print("insufficient balance")
#     def get_balance(self):
#         return self.balance
    
#     def mini_statement(self):
#         print("\nministatement:")
#         print(f"username:{self.username}")
#         print(f"current balance: {self.balance}")
#         for t in self.transactions:
#             print(f"{t[0]} - {t[1]}")

# class banking_system:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self,username,password):
#         if username in self.accounts:
#             print("user already exists")
#         else:
#             self.accounts[username]=account(username,password)
#             print("\naccount created successfuly")
#             print("-------welcome to Canarabank-------")
#     def log_in(self,username,password):
#         if username in self.accounts:
#             account =self.accounts[username]
#             if account.password==password:
#                 print("login success")
#                 return account
#             else:
#                 print("invalid password")
#         else:
#             print("user not found")
#         return None

# bank =banking_system()

# while True:
#     print("\n")
#     print("1. create account")
#     print("2. login")
#     print("3. exit")
#     choice=input("enter your choice (1-3): ")
#     if choice=="1":
#         username= input("enter username: ")
#         password = input("enter password: ")
#         bank.create_account(username,password)
#     elif choice=='2':
#         username= input("enter username: ")
#         password = input("enter password: ")
#         accounts= bank.log_in(username,password)
#         if accounts is not None:
#             print(f"welcome,{username}")
#             while True:
#                 print(f"welcome,{username}")
#                 print("1. deposit")
#                 print("2. withdrawl")
#                 print("3.balance")
#                 print("4. mini statement")
#                 print("5. logout\n")
#                 option = input("enter your choice: ")
#                 if option =='1':
#                     try:

#                         amount = int(input("Enter amount to deposit: "))
#                         accounts.deposit(amount)
#                     except:
#                         print(f"please enter numarics")
#                 elif option=='2':
#                     try:
#                         amount = int(input("Enter withdrawl amount: "))
#                         accounts.withdraw(amount)
#                     except:
#                         print(f"please enter numarics")
#                 elif option=='3':
#                     print(f"current balance: {accounts.get_balance()}")
#                 elif option=='4':
#                     accounts.mini_statement()
#                 elif option=="5":
#                     print("\n-------thank you-----------")
#                     exit()
#                 else:
#                     print("invalid choice")
#     elif choice=='3':
#         print("thanks for choocing the our bank")
#         break
#     else:
#         print("invalid choice")


    


        
















    

