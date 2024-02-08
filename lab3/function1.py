#task1
def ounces(gramm):
    a=gramm/28.3495231
    return a

print(ounces(28.3495231))

#task2
def Farengeith(F):
    F-=32
    c=(5/9)*F
    return c
print(Farengeith(59))

#task3
def solve(numheads, numlegs):
    x=numheads*2
    x-=numlegs
    x/=-2
    numheads-=x
    return numheads,x
        
print(solve(35, 94))

#task4
def filter_prime(n):

    n=list(n.split())
    n=map(int, n)

    result = []

    for i in n:
        flag = True
        for j in range(2, i):
            if i%j==0:
                flag=False
        if flag:
            result.append(i)

    return result

print(filter_prime("1 12 13 24 45 56 17 82 93 10 14 32 53 94 15")) 

#task5
from itertools import permutations

def print_permutations():
    text = input("Enter text: ")
    perms = permutations(text)
    for perm in perms:
        print(''.join(perm))

print(print_permutations())

#task6
def word_reverse(text):
    text=text.split()
    text.reverse()
    for i in text:
        print(i, end=" ")
    
word_reverse("We are ready")

#task7
def has_33(numbs):
    i = 0
    while i < len(numbs)-1:
        if numbs[i] == 3:
            if numbs[i+1] == 3:
                return True
        i += 1
    return False

numbers = input('Enter numbers: ')
numbs = numbers.split()
numbs = [int(num) for num in numbs]
print(has_33(numbs))

#task8
def order(num):
    s=""
    for i in num:
        s+=i
        if "007" in s:
            return True
        return False
        
number=input("Enter num: ")
num=number.split()
print(order(num))

#task9
def radius(V):
    pi=3.1415
    a=4/3*V**3*pi
    return a
    
V=int(input("Enter number: "))
print(radius(V))

#task10
def a_unique(num):
    s=[]
    for i in num:
        if num.count(i)==1:
            s.append(i)
    print(s)
    
a_unique([1,1,4,0,0,4,5])
a_unique([1,3,2,7,5,5,5,2,9])

#task11
def palindrom(s):
    if s==s[::-1]:
        print("It is Palindrom")
    else:
        print("Not Palindrom")

palindrom("kazak")
palindrom("lamal")
palindrom("selfy")
palindrom("madam")

#task12
def histograme(num):
    for i in num:
        print("*"*i)
        
        
histograme([4, 9, 7])

#task13
import random

def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, KBTU! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)

name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
count = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find_num_random(number, count)


    