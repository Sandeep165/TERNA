# tupele :-
'''
immutable,
duplications are allowed

'''
tuple1 = (1,2,3)
tuple1 = (["India"],[1,2,3,4])
tuple1 = (["India"])
tuple1 = (["India"],)
print(type(tuple1))



tuple2 = (1,2,3,4,5,6)
# num>3    new_tuple = (4,5,6)

# tuplea= (1,2,3,4,5,6)
# a=tuple(tuplea)
# a=tuplea[3:]
# print(a)


lst =[]
for i in tuple2:
    if i>3:
        lst.append(i)
tuple_new = tuple(lst)
print(tuple_new)

fruits = ("apple","mango","banana")

# for i in range(len(fruits)):
#     print(fruits[i])

# # len - 1

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

names = ("mumbai","pune","delhi","Harry","john",98,9,1,89,3,569,100,True,False)

# for i in range(len(names)):
#     print(names[i])


# for i in range(10):
#     print(i)

# t1 = (1,2,3,4,5)
# t2 = t1*2
# print(t2)



'''
Set :- {}
sets element are unchangeble but you cann add or remove
Unorderd, unchangeable,unindexed
set1 = {1,2,3,4}
immutable :- we cannot, we cannot delete, we cannnot update


frozenset 
'''

# set1 = {"mumbai","delhi","pune"}
set1 = {"mumbai","delhi","pune","goa","mumbai","Pune"}
# print(set1)
# #mumbai delhi pune goa Pune

# print(len(set1))

list1 = [1,2,3,6,5,4,8,8,8,8]

set1 = set(list1)
# print(set1)

# for i in set1:
#     print(i)

'''
in
is
not
'''
fruits = {"apple","mango","banana"}
fruits.add("orange")
print(fruits)
fruits.remove("apple")
print(fruits)

new_fruits = frozenset(fruits)
print(new_fruits)

