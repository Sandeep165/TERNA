'''

Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
      Unit                                                               Price  
First 100 units(0-100)                                               no charge
Next 100 units(101-200)                                             Rs 5 per unit
After 200 units                                                      Rs 10 per unit


109 = 109-100= 9*5 = 45
99  = 0rs
101 = 5rs
199 = 99*5
150 = 50*5 = 250rs


210 = 210-100 = 100 * 5 + 10*10 = 500+100 = 600

170 = 70*5
240 = 100 + 100 + 40 =  0+ 500 + 400 = 900
(For example if input unit is 350 than total bill amount is Rs2000)

unit = 0-100 = 0
unit = 101-200 = 5rs per unit
unit = 200> = 10rs per unit

200> = 100*0 + 100*5 + 5*10

'''

# unit = int(input("Enter the unit :- "))

# if unit<=100:
#     print("Amount to pay is 0Rs")
# elif unit>100 and unit <=200:
#     print("Amount to pay is :-",(unit - 100)*5 )
# else :
#     print("Amount to pay is :- ", (unit-200)*10 + 500)


'''
Data type :-
Text Type:      	str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict {key:value}
Set Types:      	set, frozenset
Boolean Type -> bool :	    bool -> (True/False)
Binary Types:	    bytes, bytearray, memoryview

'''

'''
#List :-  []

1) List is used to save multiple data type
2) List is mutable (we can update,change,delete)
3) lst = [1,2,3,"apple","mango"]

'''

# list_num = [1,2,3,4,5,6]
# list_str = ["apple","mango","banana"]

# print(list_num)
# print(list_str)

list_combine = [1,2,3,4,5,6,"apple","mango","banana"]
# print(list_combine[4]) #5
# print(list_combine[-1]) #-1
# print(list_combine[0:5]) #-1   [1,2,3,4,5]
# print(list_combine[::-1]) #
'''
start :- inclusive (include that index)
end   :- exclusive (exclude that index)
step  :- 1
'''
#append() :-  add an element at the end of the list
#insert() :-  add an element at given index

# list_combine = [1,2,3,4,5,6,"apple","mango","banana"]
# print("Before updating:- ",list_combine)


# list_combine.append("grapes")
# print("After updating:- ",list_combine)


# list_combine.insert(1,"India")
# print("After inserting:- ",list_combine)
'''
create list = first till 10 even no :- [4,6,7,10]
update list = any one city name:- [...,"x","y","z"]
insert list = remaining nos from 1-10:-  [1,2,3,4,5,6,7,8,9,10]
'''
lis1=[2,4,6,8,10] 
# lis1.append("Osmanabad ","pune","mumbai") 
# lis1.append("Pune ") 
# lis1.append("Mumbai ") 
# print("List after updating:- ",lis1)
# lis1.insert(0,1)
# lis1.insert(2,3)
# lis1.insert(4,5)
# lis1.insert(6,7)
# lis1.insert(8,9)
# print("List after inserting:- ",lis1)

#clear() and copy()
# print("List after clearing:- ",lis1.clear())

lis1=[2,4,6,8,10] 

# # list_copy = lis1.copy()
# list_new = lis1


# list_new.append("Inida")
# # print(list_copy)
# print(lis1)
# print(list_new)

new_list = ["mumbai","pune","chennai","delhi"]
#pop() :- remove the value by taking an index
#remove():- remove the value by taking the value
# new_list.remove("chennai")
new_list.pop(2)

# print(new_list)


#count() and extend()

list_num = [1,2,6,8,1,6,4,1,9,1,96,1,1]
# print(list_num.count(2))


country = ["India","USA"]
city = ["Mumbai","Mexico"]

# country.extend(city)
city.extend(country)
print(city)


