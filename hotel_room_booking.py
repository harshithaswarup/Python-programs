import datetime
from datetime import timedelta
class Room:
    def get_room_cost(self):
        wkd_cost=500
        wknd_cost=600
        discount=0.05
        return wkd_cost,wknd_cost,discount

    def get_cust_details(self):
        cust_type=['Normal','Reward']
        return cust_type
    
    def get_check_in_date(self):
        print "Enter the date of check-in:"
        year=int(input("enter a year:"))
        month=int(input("enter a month:"))
        day=int(input("enter the day:"))
        check_in_date=datetime.date(year,month,day)
        check_out_date=check_in_date+timedelta(2)
        self.day_1=check_in_date.weekday()
        return check_in_date,check_out_date

    def get_no_days(self,check_in_date,check_out_date):
        #days=check_out_date-check_in_date
        days=2
        return days
    
    def get_total_cost(self,days,wkd_cost,wknd_cost):
        if self.day_1 in range(0,5):
            total_cost=(days)*(wkd_cost)
            return total_cost
        else:
            total_cost=(days)*(wknd_cost)
            return  total_cost

    def get_discount(self,total_cost,discount):
        if(total_cost>1000):
            discount_amt=(total_cost)*(discount)
            return discount_amt

    def get_final_cost(self,total_cost,discount_amt,cust_type):
        cust_inp=raw_input("enter the type:")
        if(cust_inp==cust_type[1] and total_cost>1000):
            discount_cost=(total_cost)-(discount_amt)
            print "The cost of the room after discount is:",discount_cost
        else:
            print "The cost of the room is:",total_cost

    

r=Room()
wkd_cost,wknd_cost,discount=r.get_room_cost()
cust_type=r.get_cust_details()
check_in_date,check_out_date=r.get_check_in_date()
days=r.get_no_days(check_in_date, check_out_date)
total_cost=r.get_total_cost(days,wkd_cost,wknd_cost)
discount_amt=r.get_discount(total_cost,discount)
r.get_final_cost(total_cost,discount_amt,cust_type)
