'''
Method              	Description
append()    	Adds an element at the end of the list
clear()     	Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()      	Sorts the list
'''

#List Comprehension

# for loop
'''
slicing[start:end:step]

for i in range(1,11):
    print(i)

'''

# for i in range(0,11,2):
#     print("The numbers are;- ",i)

# append( ) ?

# list_new = []
# print("Before using for loop:- ",list_new)

# for i in range(11):
#     list_new.append(i*i)
# print(list_new)
# print("After for loop:- ",list_new)
   



# list_new.append(0)
# list_new.append(2)
# list_new.append(4)
# list_new.append(6)
# list_new.append(8)
# list_new.append(10)
# print(list_new)




# lst = ["india","USA"]
# name = "Sandeep"

# for i in ["india","USA"]:
#     print(i) #




fruits = ["apple","mango","grapes","kiwi"]

# a_name = []

# for i in fruits:
#     if "a" in i:
#         a_name.append(i)
# print(a_name)


fruits_new = ["apple","mango","cherry","pineapple"]


'''
take ele using for loop
if condition
print()
'''
E_Name = [ i for i in fruits_new if "e" in i ]
print(E_Name)



numb = [1,2,3,4,5,6,7,8,9,10]
even = []

# %2 == 0 

for i in numb:
    if i%2 == 0:
        even.append(i)
print(even)

'''
E_Name = [ i for i in fruits_new if "e" in i ]
print(E_Name)

'''

'''
take ele using for loop
if condition
print()


list_c = [(3) print    (1)for loop    (2)if logic]
'''
even = [i for i in numb if i%2 == 0]
odd = [i for i in numb if i%2 != 0]


lst_nub = [i for i in range(21) if i>7 ]

print(lst_nub)



fruits_new = ["apple","mango","cherry","pineapple"]
new = []

for i in fruits_new:
    new.append(i.upper())


UPPER = [i.lower() for i in fruits_new]
# UPPER = [i.upper()  for i in fruits_new  /]

print(UPPER)


'''
tuple()  and set{}
'''