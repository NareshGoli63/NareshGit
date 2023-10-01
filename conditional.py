'''
decision making statements
if
else
elif
nested if

'''


'''
Syntax
if condition:
     statements
else
     statements
'''

if True:
    print("abc")
elif True:
    print("abcd")
else:
    print("bca")


if False:
    print("Outer if")
    if True:
        print("inner if")
elif False:
    print("else if")
else:
    print("Outer else")

age = 19
if age>18:
 print("naresh")
 if age>=18:
  print("mahesh")
elif age<18:
 print("rajesh")
else:
   print("sarath")


age = 19
if age>18 or age==18:
 print("naresh")
 if age>=18:
  print("mahesh")
elif age<18:
 print("rajesh")
else:
   print("sarath")