'''
if (condition):
    print("")
elif (condition):
    print("")
elif (condition):
    print("")
elif (condition):
    print("")
else:
    print("")

Equals: a==b
Not equals: a!=b
Less than: a<=b
Greater tha: a>=b

'''
# num1 = int(input("Number1:- "))
# num2 = int(input("Number2:- "))
# num3 = int(input("Number3:- "))

#user will input 3 diff no you have to guess greater among the three
# if(num1>num2 and num1>num3):
#    print("num1 is greater", num1)
# elif(num2>num3 and num2>num1):
#     print("num2 is greater", num2)
# else:
#     print("num3 is greater", num3)


'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.

salary, yos, yos greater 5   salary + 5% salary

10000, 6, salary = 10000+500 = 10500
'''
# salary=int(input("enter salary:- "))
# yos=int(input("enter no years:- "))
# if( yos>5 and yos<=10):
#     salary=salary+int(salary*0.05)
#     print ("bonus salary=",salary)
# elif(yos>10):
#     salary=salary + int(salary*0.1)
#     print("bonus salary=",salary)
# else:
#     print("nothing bonus ")


'''
students will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

no_cls_held, no_cls_attended, perce

12 , 3, 40%
if p>75:

'''
# no_cls_held = int(input("Number of class Held :"))
# no_cls_attended = int(input("Number of class attended :"))
# percentage = (no_cls_attended/no_cls_held )*100
# if percentage>75 :
#     print("Student is allowed to sit in exam")
# else :
#     print("Student is not allowed to sit in exam")

'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.


q = 16
total = q*100

total>100:
  10% total


q = 11
total= q*100 = 11*100= 1100

total>1000:
1100>1000:
10% of total
10% of 1100
10/100 of 1100
0.1*1100 = 17
total - 17


q = 20
total =20000
total>1000:

discount = 0.1*20000= 2000

total - dis
18000

'''
q=int(input("enter number of quantity:-"))
total=q*100 
print("total amount is :- ", total)
if(total>1000): 
    total=total-total*0.1
    print("total=",total) 
else: 
    print("total =",total)
