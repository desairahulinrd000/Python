from time import sleep
from datetime import datetime as dt
import random as rd


bank_users=5800019008
ittr=0
ifsc="ABCD1231234"
users=[]
micr=5800011234
bank_card_number=5800019008181612



class NewAccount():
    
        
    def __init__(self,f_name,m_name,l_name,dob,mobile,upin,user_id,card_nor):
        self.f_name=f_name
        self.m_name=m_name
        self.l_name=l_name
        self.dob=dob
        self.mobile=mobile
        self.pin=upin
        self.acc_nor=user_id
        self.balance=0.0
        self.card_number=card_nor
        self.card_exp_yr=dt.now().year+6
        self.card_exp_mnt=dt.now().month
        self.card_exp_cvv=rd.randrange(100,999)
        self.card_pin=rd.randrange(1000,9999)
        
        
    def details(self):
        print(f'Name:{self.f_name} {self.m_name} {self.l_name}')
        print(f'Date of Birth:{self.dob}')
        print(f'Mobile Number:{self.mobile}')
        print(f'Account Number:{self.acc_nor}')
        print(f'IFSC Code:{ifsc}')
        print(f'MICR Code:{micr}')
        print(f'Balance:{self.balance}')
        print(f'Debit Card Number:{self.card_number}')
        print(f'Expiry:{self.card_exp_mnt}/{self.card_exp_yr}')
        print(f'CVV:{self.card_exp_cvv}')
        print(f'Debit Card PIN:{self.card_pin}')
        
    def deposit(self,dep_amt):
        self.balance+=dep_amt
        print("Deposited Amount Successfully")
        print(f'Balance={self.balance}')
        
        
    def wd_amt(self,dep_amt):
        self.balance-=dep_amt

        
def loading(text):
    print(text,end="")
    a=rd.randrange(2,6)
    for i in range(a):
        print(".",end="")
        sleep(0.8)
    print()
    
    
    
while True:
    loading("Entering Bank Account's Portal")
    choice1=int(input("1)New user\n2)Exixting User\n3)Quit\nYour Choice:-"))
    if choice1==1:
        choice2=int(input("1)Create New Account\n2)Quit\nYour Choice:-"))
        if choice2==1:
            fname=input("Enter your First Name:-")
            mname=input("Enter your Middle Name:-")
            lname=input("Enter your Last Name:-")
            dob=input("Enter Your Date Of Birth in DD/MM/YYYY format:-")
            mobile=int(input("Enter Your Mobile Number"))
            upin=int(input("Enter Your 4-digit User Pin:-"))
            user_acc=str(micr) + str(bank_users)
            users.append(NewAccount(fname,mname,lname,dob,mobile,upin,bank_users,bank_card_number))
            loading("Creating new Account")
            print("Account Created Successfully")
            users[ittr].details()
            bank_users+=1
            bank_card_number+=1
            ittr+=1
        elif choice2==2:
            pass
    elif choice1==2:
        acc=int(input("Enter Your Account Number:"))
        loading("Fetching Account's")
        found=False
        for i in range(ittr):
            if acc == users[i].acc_nor:
                found=True
                pin=int(input("Enter Your Four digit PIN:"))
                loading("Validating PIN.")
                if users[i].pin==pin:
                    a="""
1)View Account Details and Balance
2)Deposite Amount
3)Withdraw Amount
4)Quit
Enter Your Choice:-"""
                    choice3=int(input(a))
                    if choice3==1:
                        loading("Fetching Account Detail's")
                        users[i].details()
                    elif choice3==2:
                        dep_amt=int(input("Enter the Amount to be deposited:"))
                        users[i].deposit(dep_amt)

                    elif choice3==3:
                        with_amt=int(input("Enter the amount to be Withdrawn:"))
                        if with_amt>users[i].balance:
                            print("Insufficient Funds")

                        else:
                            users[i].wd_amt(with_amt)
                            
                            loading("Connecting to Server.")
                            print("Please Collect your Cash")

                    elif choice3==4:
                        pass   
                    
                else:
                    print("Invalid PIN")
                    
            elif not found:
                print("No Account Details Found")
        print("Logging Off")


    
