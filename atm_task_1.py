import datetime
class Atm:

    '''The customer's details like name,pin and balance are set globally'''
    
    def __init__(self,bal,name,pin):  
        self.bal=bal
        self.name=name
        self.pin=pin
        
    ''' Default values are set to the customer details  '''

    def get_info(self):         
        cus_name='Harshi'
        cus_pin=0001
        cus_bal=100000
        self.name=cus_name
        self.bal=cus_bal
        self.pin=cus_pin

    ''' This function will get called when the user wishes to "deposit" money.
      The amount to be deposited is added to the available balance '''
 
    def get_deposit_amount(self):
        dep_amt=int(input('Enter the amount to deposit:'))
        return dep_amt
    

    def get_deposited_bal(self,dep_amt):
        (self.bal)+=(dep_amt)
        return self.bal
    
    ''' This function gets called when the user wishes to "withdraw" money.
        The money will get withdrawed from the available balance '''

    def get_withdraw_amount(self):
        withdraw_amt=int(input('Enter the amount to withdraw:'))
        return withdraw_amt

    def get_withdrawed_balance(self,withdraw_amt):
        (self.bal)-=(withdraw_amt)
        return self.bal
    
    ''' This function gets called when the user wishes to change the
       pin. '''
    
    def change_pin(self):
        old_pin=int(input('Enter your old pin:'))
        new_pin=int(input('Enter the new pin:'))
        confirm_pin=int(input('Confirm the pin:'))
        if(new_pin==confirm_pin):
            return new_pin,confirm_pin

    ''' The function displays the current available balance in
       the account '''
    
    def check_balance(self):
        return self.bal
    
    ''' The details like name,balance,time n date of transaction
        and card number will get displayed if the user wishes for
        a mini statement.

        The card number is set default '''


    def get_mini_statement(self):
        card_no='**** **** **** *002'
        date_time= datetime.datetime.now()
        return card_no,date_time

             

    def display(self,card_no,date_time):
        if(choice==1):
            print 'The balance available is:',self.bal
        elif(choice==2):
            print 'The balance available is:',self.bal
        elif(choice==3):
            print 'Your pin has been changed!!'
        elif(choice==4):
            print 'The  balance available is:',self.bal
        elif(choice==5):
            print 'Name:',self.name
            print 'card number:',card_no
            print 'Time and date of transaction:',date_time
            print 'The balance available is:',self.bal

    

            

process=True

''' Object created for the class'''

a=Atm(100000,'Harshi',0001)
user_pin=int(input('Enter your pin number:'))

while process:
    print('1.deposit')
    print('2.withdraw')
    print('3.change-pin')
    print('4.check-balance')
    print('5.get mini-statement')

    choice=int(input('what would you like to do?'))

    if(choice==1):
        dep_amt=a.get_deposit_amount()
        deposited_bal=a.get_deposited_bal(dep_amt)
        card_no,date_time=a.get_mini_statement()
        a.display( card_no,date_time)

    elif(choice==2):
        withdraw_amt=a.get_withdraw_amount()
        withdrawed_bal=a.get_withdrawed_balance(withdraw_amt)
        card_no,date_time=a.get_mini_statement()
        a.display( card_no,date_time)

    elif(choice==3):
        new_pin,confirm_pin=a.change_pin()
        card_no,date_time=a.get_mini_statement()
        a.display( card_no,date_time)
        
    elif(choice==4):
        a.check_balance()
        card_no,date_time=a.get_mini_statement()
        a.display( card_no,date_time)

    elif(choice==5):
        card_no,date_time=a.get_mini_statement()
        a.display( card_no,date_time)

    ''' The user is asked whether to make more transactions.
        If 'yes', the proess continues, else the process will
        terminate'''

    choice=['yes','no']
    user_inp = raw_input('Would you like to make another transaction yes/no:')
    if user_inp == 'yes':
        process = True
    else:
        process = False
        


        
        

