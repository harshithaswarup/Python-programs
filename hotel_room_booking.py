import datetime
class Room:
    def get_cost(self):
        wkd_cost=500
        wknd_cost=600
        discount=0.05
        return wkd_cost,wknd_cost,discount

    def get_cust_details(self):
        cust_type=['Normal','Reward']
        return cust_type
    
    def get_check_in_date(self,cust_type):
        cust_inp=raw_input("enter the type of customer:")
        year=int(input("enter a year:"))
        month=int(input("enter a month:"))
        day=int(input("enter the day:"))
        check_in_date=datetime.date(year,month,day)
        day_1=check_in_date.weekday()
        return check_in_date,cust_inp,day_1
    
    def get_no_days(self,check_in_date):
        #days=check_out_date-check_in_date
        days=2
        return days
    
    def get_total_cost(self,days,wkd_cost,wknd_cost,day_1):
        if day_1 in range(0,5):
            total_cost=(days)*(wkd_cost)
            return total_cost
        else:
            total_cost=(days)*(wknd_cost)
            return  total_cost

    def get_discount(self,total_cost,discount):
        if(total_cost>1000):
            discount_amt=(total_cost)*(discount)
            return discount_amt

    def get_final_cost(self,total_cost,discount_amt,cust_inp):
        if(cust_inp=='Reward' and total_cost>1000):
            discount_cost=(total_cost)-(discount_amt)
            return discount_cost

    def display_Room_cost(self,discount_cost,total_cost,cust_inp,cust_type):
        if(cust_inp=='Reward' and total_cost>1000):
            print "The discount cost is:",discount_cost
        else:
            print "The total cost is:",total_cost
        user_input=raw_input("would you like to know some more details?:")
        if(user_input=='yes'):
            check_in_date,cust_inp,day_1=r.get_check_in_date(cust_type)
            total_cost=r.get_total_cost(days,wkd_cost,wknd_cost,day_1)
            discount_amt=r.get_discount(total_cost,discount)
            discount_cost=r.get_final_cost(total_cost,discount_amt,cust_inp)
            r.display_Room_cost(discount_cost,total_cost,cust_inp,cust_type)
        else:
            return
                

r=Room()
wkd_cost,wknd_cost,discount=r.get_cost()
cust_type=r.get_cust_details()
check_in_date,cust_inp,day_1=r.get_check_in_date(cust_type)
days=r.get_no_days(check_in_date)
total_cost=r.get_total_cost(days,wkd_cost,wknd_cost,day_1)
discount_amt=r.get_discount(total_cost,discount)
discount_cost=r.get_final_cost(total_cost,discount_amt,cust_inp)
r.display_Room_cost(discount_cost,total_cost,cust_inp,cust_type)

