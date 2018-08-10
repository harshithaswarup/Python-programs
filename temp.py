import datetime
class Temperature:
    def __init__(self):
        self.fin_dict={}

    def add_value(self):
        choice1=['yes','no']
        dict1={'12/12/2018':[34,90],'13/12/2018':[45,80]}
        self.fin_dict=dict1
        return choice1

    def get_input_date(self):
        x=int(input("Enter a year:"))
        y=int(input("Enter a month:"))
        z=int(input("Enter the day:"))
        date1=datetime.date(x,y,z)
        date=date1.strftime('%d/%m/%y')
        return date

    def get_temp(self):
        temp_list=[]
        for x in range(2):
            temp_val=raw_input("Enter the temperature either in F or C:")
            m=t.to_check_temp(temp_val)
            temp_list.append(m)
        return temp_list,temp_val


    def to_check_temp(self,temp_val):
        degree=int(temp_val[:-1])
        i_convention=temp_val[-1]
        if i_convention.upper() == "F":
            res = int(round((degree - 32) * 5 / 9))
            return res
        else:
            return degree


    def add_temp_date(self,temp_list,date,choice1):
        key=date
        if date in self.fin_dict.keys():
            self.fin_dict[date].extend(temp_list)
        else:
            self.fin_dict.update({date:temp_list})
        inp=raw_input("would you like to add more input?")
        if(inp=='yes'):
            choice1=t.add_value()
            date=t.get_input_date()
            temp_list,temp_val=t.get_temp()
            t.add_temp_date(temp_list,date,choice1)
        else:
             return self.fin_dict
            #print self.fin_dict

    def get_user_date(self):
        user_choice=['min','max','avg']
        y=int(input("Enter a year:"))
        m=int(input("Enter a month:"))
        d=int(input("Enter the day:"))
        date1=datetime.date(y,m,d)
        date2=date1.strftime('%d/%m/%y')
        return date2,user_choice

    def get_min_temp(self,date2):
        min_temp=min(self.fin_dict[date2])
        return min_temp

    def get_max_temp(self,date2):
        max_temp=max(self.fin_dict[date2])
        return max_temp

    def get_avg_temp(self,date2,temp_list):
        diff_day=2
        avg_temp=float(sum(temp_list)/(diff_day))
        return avg_temp



    def display_temperature(self,date2,min_temp,max_temp,user_choice,choice1,avg_temp):
        user_inp=raw_input("enter the choice:")
        for keys in self.fin_dict:
            if(user_inp=='min' and date2==keys):
                print "The minimum temp is:",min_temp
            elif(user_inp=='max' and date2==keys):
                print "The maximum temp is:",max_temp
            elif(user_inp=='avg' and date2==keys):
                print "The average temp is:",avg_temp
        inp1=raw_input("Do you want to know more?")
        if(inp1=='yes'):
            min_temp=t.get_min_temp(date2)
            max_temp=t.get_max_temp(date2)
            avg_temp=t.get_avg_temp(date,temp_list)
            date2,user_choice=t.get_user_date()
            t.display_temperature(date2,min_temp,max_temp,user_choice,choice1,avg_temp)
        else:
            return
        

t=Temperature()
choice1=t.add_value()
date=t.get_input_date()
temp_list,temp_val=t.get_temp()
t.add_temp_date(temp_list,date,choice1)
date2,user_choice=t.get_user_date()
min_temp=t.get_min_temp(date2)
max_temp=t.get_max_temp(date2)
avg_temp=t.get_avg_temp(date2,temp_list)
t.display_temperature(date2,min_temp,max_temp,user_choice,choice1,avg_temp) 
