class Money:
    def __init__(self,balance):
        self.balance = balance
        
    def get_initial_balance(self):
        init_balance=1000.00
        self.balance=init_balance
        return init_balance

    def get_item_cost(self):
        item_cost=float(input("enter the cost of the item:"))
        print "Are you sure to buy the item which costs:$ ",item_cost,"?"
        user_choice=['yes','no']
        return item_cost,user_choice

    def get_confirmation(self,user_choice):
        user_inp=raw_input("enter the choice:")
        return user_inp


    def get_balance(self,user_inp,item_cost):
        if(user_inp=='yes'):
            self.balance-=item_cost
            return float(self.balance)

    def get_debt_amt(self,item_cost):
        if(item_cost>self.balance):
            item_cost-=self.balance
            return float(item_cost)

    def display_balance(self,item_cost,user_inp,user_choice):
        if(user_inp=='yes'):
            print "The balance available to spend is:",self.balance
        elif(user_inp=='no'):
            print "The balance available is:",self.balance
        elif(item_cost>self.balance):
            print "The debt amount is:",self.balance
        if(self.balance>0):
            item_cost,user_choice=m.get_item_cost()
            user_inp=m.get_confirmation(user_choice)
            m.get_balance(user_inp,item_cost)
            debt_amt=m.get_debt_amt(item_cost)
            m.display_balance(item_cost,user_inp,user_choice)
        else:
            return


m=Money(1000)
init_balance=m.get_initial_balance()
item_cost,user_choice=m.get_item_cost()
user_inp=m.get_confirmation(user_choice)
m.get_balance(user_inp,item_cost)
m.get_debt_amt(item_cost)
m.display_balance(item_cost,user_inp,user_choice)

