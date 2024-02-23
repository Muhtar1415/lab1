#task1
def square(a,b):
    for i in range(a,b+1):
        yield i**2

squares = square(int(input()),int(input()))

for i in squares:
    print(i,end=".")
print()


#task2
def even(n):
    for i in range(0,n+1,2):
        yield i


n=int(input("Enter num: "))
generator=even(n)
for i in generator:
    print(i,end=", ")
    
    
#task3
def divisible(n):
    for i in range(1, n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i
            
n=int(input("Enter num:"))
generate=divisible(n)
for i in generate:
    print(i,end=" ")


#task4
def square(a,b):
    for i in range(a,b):
        yield i**2
        
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
generate=square(a,b)
for i in generate:
    print(i,end=" ")


#task5
def numbers(n):
    for i in range(n,-1,-1):
        yield i
n=int(input("Enter num:"))
lower=numbers(n)
for i in lower:
    print(i,end=" ")
