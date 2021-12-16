#num1,num2     same     numbs are equal     numbs are not equal
# num1 = int(input("Enter a number:- "))
# num2 = int(input("Enter a number:- "))

# #    =    ==
# if num1 == num2:
#     print("Equals")
# else:
#     print("Not equals")

'''
mark < 35
fail

<35
pass

35
Reval


if elif else

'''

# marks = int(input("Enter your marks :- "))

# if marks<35:
#     print("Fail")
# elif marks == 35:
#     print("reval")
# else:
#     print("Pass")

'''

(either of the condtion should be true -> True)
T or T -> true
T or F -> true
F or T -> true
F or F -> False


(either of the condtion is false -> False)
T and T -> true
T and F -> False
F and T -> False
F and F -> False



A school has following rules for grading system:
a. Below 25 - F
b. >=25 to <45 - E
c. >=45 to <50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.



num<5 = less
5-10 = in-between
10-15 = in-between-Num
numb>15 = more
'''

# num = int(input("Number :- "))
# if num<5:
#     print("Less")
# elif num>=5 and num<10:
#     print("in-between")
# elif num>= 10 and num<15:
#     print("in-between-Num")
# else:
#     print("more")

num=int(input ("Input any nub:- ") )
if num<25:
     print("F") 
elif num>=25 and num<50:  #45,46,47,48,49
    print("E") 
elif num>=50 and num<60:
    print("C") 
elif num>=60 and num<80:
    print("B") 
else:
    print("A")
