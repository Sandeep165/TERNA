'''
update()  -> last (val)
insert()  -> add at paticular index (index, val)

pop        -> remove value by taking an index
remove     -> remove the value by taking the value itself

clear      -> remove all the data (None)
count      -> count the no of occuerence

copy       ->  temp copy    
=          ->  connect the two list with a link

extend     -> add a list to a prev one

index      -> list(4) -> "pune"

sort       -> sort(reverse = False) - > ascending , sort(reverse = True) / [::-1]


'''
# l1 = [1,2,3,4]
# l1_new = l1

# lst = [1,2,3,4,"mumbai","punr",True,False]
# lst = [1,2,3,4,"mumbai","punr",True,False]
# lst.insert(1,"india")
# print(lst) 

# lst2=[1,2,2,5]
# lst[4]=6
# print(lst)
# lst.pop(4)
# lst.remove("india")
# lst.extend(lst2)
# lst.count(2)


# lst= [1,2,3,4,"mumbai","pune",True,False] 

# lst. append(5) 
# lst. append("osmanabad")
 
# print("after inserting new element list=",lst) 
# lst. insert(4,5)
# lst. insert(5,6) 
# print("after inserting new element at specified position list=",lst)
# lst. pop(5) 
# print("after deleting element at specified position list=",lst) 
# lst. remove("mumbai ") 
# print("after removing element in list=",lst)
# lst.count(5)
# l2=lst.copy() 
  
# l3=lst() 
# lst.clear()


# lst = [1,5,8,10,6,22,45,9]
# lst.sort(reverse=True)
# print(lst)


# fruit = ["apple","apple","banana","black berry","grapes","guava"]
# fruit.sort()
# print(fruit)

# lst = [1,2,3,4,5,8,10,16,0,22,17]
# lst.sort()
# print("Ascending order:- ",lst)
# print("Ascending order:- ",lst[::-1])


# str part
# palindrome 

lst = [[1,2,3,"india",[True,False,[15.0,25.0]],"Mumbai",[11,22,["USA",["sam","john"],"UK"],33,44]],"Hello"]
# print(lst[4][0])
# print(lst[4][1])
# print(lst[6][3])
# print(lst[4][2][1])
# print(lst[6][2][1])
# print(lst[6][2][1][0])

my_countries = ["mumbai","pune",[400078,4000081,4000095,400051],["USA","JAPAN","AUS",["MEXICO"]],"NASHIK","DELHI"]
# 400095,Mexico,delhi 

print(my_countries[2][2])
print(my_countries[3][3][0])
print(my_countries[5])



my_fruits = ["apple","mango",[[1,2,3,4],"hello_world"],"grapes"]
# 3, hello_world

print(my_fruits[2][1])
print(my_fruits[2][0][2])


list1 = [["harry","john"],1,4,6,9,["India"],400078]
# 9 , india, john, [india]
print(list1[4])
print(list1[5][0])
print(list1[0][1])
print(list1[5])