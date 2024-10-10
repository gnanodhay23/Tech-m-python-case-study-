objects=[]
class customer:
    def __init__(self,name,dob,mobile_number,email,a_n):
        self.customer_name=name
        self.dob=self.valid_dob(dob)
        self.mobile=self.valid_mobile(mobile_number)
        self.email=email
        self.amount=0
        self.transactions=[]
        self.a_n=a_n
    def valid_dob(self,a):
        m=a
        s=list(m.split("/"))
        if(len(s[0])==2 and len(s[1])==2 and len(s[2])==4):
            return a
        else:
            raise Exception("invalid dob")

    def valid_mobile(self,a):
        return a
    def account(self):
        pass
    def view_details(self):
        l=[]
        l.append(self.customer_name)
        l.append(self.dob)
        l.append(self.mobile)
        l.append(self.email)
        l.append(self.amount)
        #l.append(self.account_number)
        print("ACCOUNT HOLDER DETAILS:")
        print(l)
    def deposit(self,amount):
        self.amount+=amount
        st=str(amount)
        self.transactions.append("credited  "+st)
        print(f"Account {self.a_n} current balance: ",self.amount)
    def withdraw(self,amount):
        self.amount-=amount
        st=str(amount)
        self.transactions.append("debited "+st)
        print(f"Account {self.a_n} current balance: ",self.amount)
    def transaction(self):
        print("hey customer your transactions are: ")
        print(self.transactions)
def createaccount():
    print("Enter yout details: ")
    name=input("Enter your name: ")
    dob=input("Enter your data of birth format(dd/mm/yyyy )pls provide slash: ")
    mobile_number=input("Enetr your mobile number: ")
    email=input("Enter your email: ")
    if(len(objects)==0):
        a_n=1001
    else:
        a_n=1001+len(objects)
    Account_number=customer(name,dob,mobile_number,email,a_n)
    objects.append(Account_number)
    print("Congrats you have created your account with account number Account Number: ",a_n)
def viewaccountdetails():
    n=int(input("please enter your Account_Numer: "))
    for i in objects:
        if(i.a_n==n):
            i.view_details()
            break
def deposit():
    n=int(input("please enter your Account_Numer: "))
    money=int(input("Enter the amount to be deposited: "))
    for i in objects:
        if(i.a_n==n):
            i.deposit(money)
    print("your current balance",i.amount)
def withdraw():
    n=int(input("please enter your Account_Numer: "))
    money=int(input("Enter the amount to be withdraw: "))
    for i in objects:
        if(i.a_n==n):
            i.withdraw(money)
    print("your current balance",i.amount)
def transaction():
    n=int(input("please enter your Account_Numer: "))
    for i in objects:
        if(i.a_n==n):
            i.transaction()
    
def fundtransfer():
    n=int(input("please enter your Account_Numer: "))
    m=int(input("Enter the Account Number to which amount should be transfered: "))
    money=int(input("Enter the money to be transferd: "))
    for i in objects:
        if(i.a_n==n):
            i.withdraw(money)
        if(i.a_n==m):
            i.deposit(money)
    print("transaction sucsessful!!")
while True:
    print("Hey customer Enter the below numbers for respective  services:")
    print("1.craete an Account")
    print("2.view Account details")
    print("3.withdraw")
    print("4.Deposit")
    print("5.transaction history")
    print("6.fund transfer")
    print("7.exit")
    num=int(input("Enter the service required: "))
    if num==1:
        createaccount()
    elif num==2:
        viewaccountdetails()
    elif num==3:
        withdraw()
    elif num==4:
        deposit()
    elif num==5:
        transaction()
    elif num==6:
        fundtransfer()
    elif num==7:
        print("Thankyou customer")
        break
        exit

