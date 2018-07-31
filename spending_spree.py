import sys
class Money:
    def __init__(self):
        self.balance=1000
        
    def get_initial_balance(self):
        balance=1000
        print "the initial balance available is:",balance
        return balance
    
    def get_item_cost(self):
        item_cost=int(input("Enter the cost of the item you want to buy:$"))
        print "Are you sure to buy the item which costs:$ ",item_cost,"?"
        x=raw_input("enter Yes or No:")
        user_choice=["yes","no"]
        return item_cost,x,user_choice
    
    def get_balance(self,item_cost,x,user_choice,balance):
        if(x==user_choice[0]):
            sub_balance=self.balance-item_cost
            self.balance=sub_balance
            print "The remaining money available to spend :$",sub_balance
        else:
            print "The available balance is:$",balance

    def get_debt_amount(self,item_cost,balance):
        if(item_cost>balance):
            print "Sorry you don't have sufficient balance to buy the item!!"
            debt_amt=item_cost-balance            
            print "You owe :$",debt_amt
            #sys.exit()
            return debt_amt

    def display_cost(self):
        item_cost,x,user_choice=m.get_item_cost()
        debt_amt=m.get_debt_amount(item_cost,balance)
        m.get_balance(item_cost,x,user_choice,balance)
        
m=Money()
balance=m.get_initial_balance()
item_cost,x,user_choice=m.get_item_cost()
debt_amt=m.get_debt_amount(item_cost,balance)
m.get_balance(item_cost,x,user_choice,balance)
m.display_cost()
