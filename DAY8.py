#Tuple and set

'''
even= [ 2 -20 ]
list compr.
normal

odd= [ 1 -19 ]
list compr.
normal


numbs = [ 1 - 50 ]
updated = [ divisible by 3 or divisible by 5]
updated = [3 , 5 6 9 10 12 15 ]
list comp.
normal
'''

updated = [i for i in range(1,51) if i%3 == 0 or i%5 == 0]
l = []
for i in range(1,51):
    if i%3==0 or i%5 ==0:
        l.append(i)

'''
tuple :- ()
we cannot change the tuple

'''

fruits = ("apple","mango","banana", "apple",1,2,5,98,7,1,38,2,8,1,8,3,"mango","banana", "apple",500,600)
# print(len(fruits))
'''
(500,600,700,800)   ->3
len - > len
'''

# print(fruits[len
# -1])

string = ("hello")
num = (1,)
print(type(num))


# constructor list tuple set 

# lst = [1,2,3,4,5]
# tuple_new = tuple(lst)
# print(tuple_new)


tup = (1,2,3,4,5,5,5,5,5,3,6,2,11,1,1,1)

lst = list(tup)
print(lst)

# keyword()-----list()


# count() and index()

print(tup.count(1))
print(tup[0]) #1
print(tup[-1]) #1

'''
fruits = ("apple","banana","kiwi")

#grapes

print(fruits) --> (apple, grapes)
'''
fruits = ("apple","banana","kiwi")
fruits_new = fruits

# fruit_list = list(fruits)
# fruit_list.append("grapes")
# fruits = tuple(fruit_list)
# print(fruits)

# t1 = ("apple",)
# t2 = ("kiwi",)
# t3 = t1+t2
# print(t3)  #applekiwi
fruits = ("apple","banana","kiwi")
fruits_new = fruits



# print(fruits)
# print(fruits_new)

# del fruits

# print(fruits_new)

country = ("India","USA","UK",1,2,3,5,4,1,6,8,2)   #Packing

(c1,c2,*c3) = country   # (india,usa,uk)   #unpacking

print(c1)
print(c2)
print(c3)

