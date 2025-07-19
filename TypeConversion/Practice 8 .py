# Q1 create a class student that takes name and marks of three subjects as arguments
# in constructor,then create a method to print the average ?



#...OR...

class student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Hi ",self.name,"Your average score is:",sum/5)

st1 = student("owais",[85,85,75,85,85])
st1.avg()

# Q2 Create account class with 2 attributes- balance and account no, create methods for debit,credit and printing the balance?

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs,",self.balance,"was debited.")
        print("Total balance:",self.total())
    
    def credit(self,amount):
        self.balance +=amount
        print("Rs,",self.balance,"was credited.")
        print("Total balance:",self.total())
    
    def total(self):
        return self.balance
    
a1 = Account(10000,1234)
a1.credit(1000)
a1.debit(500)
a1.debit(5000)


        



        
    
