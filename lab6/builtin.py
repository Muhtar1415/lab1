#task1
import math
def multi(num):
    result=math.prod(num)
    return result
    
num=[1,3,5,6]
print(multi(num))


#task2
def case(count):
    lowercase=0
    uppercase=0
    for i in count:
        if i>"A" and i<"Z":
            uppercase+=1
        elif i>"a" and i<"z":
            lowercase+=1
    result=[f"Output uppercase: {uppercase}", f"Output lowercase: {lowercase}"]
    return result
count="Hello World! Hello KBTU!"
print(case(count))


#task3
def isPalindrome(soz):
    for i in soz:
        if soz==soz[::-1]:
            return "It is Palindrome"
        else:
            return "Not Palindrome"
soz=input("Enter string: ")
print(isPalindrome(soz))

#task4
def squareroot():
    import time
    import math
    x = int(input("Input the value: "))
    y = int(input("Input the miliseconds: "))
    y=y/1000
    time.sleep(y)
    return f"Square root of {x} after {y} miliseconds is {math.sqrt(x)}"
    

#task5
def all_true_elements(tuple_data):
    boolean =  True
    for i in tuple_data:
        if i != True:
            boolean = False

    if boolean:
        return True
    else:
        return f"elements of tuple is different"
        
