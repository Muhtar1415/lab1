#exercise1
class Strings:
    def getString(self,a):
        print(a)
    def printString(self,a):
        a=a.upper()
        print(a)
        
result=Strings()
result.getString("hello!")
result.printString("hello!")

#exercise 2,3
class Shape:
    def __init__(self):
        pass
    
    
    def area(self):
        return 0
        
        
    def rectangle(self):
        return self.length*self.width
        
class Square(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length*self.length
        
square=Square(3, 8)

print(square.area())
print(square.rectangle())


#exersice4
import math
class Point:
    def __init__(self, a1, b1, a2, b2):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        
    def show(self):
        return self.a1, self.b1, self.a2, self.b2
    
    def move(self):
        points=[]
        self.a1 = int(input("a1:"))
        self.b1 = int(input("b1:"))
        self.a2 = int(input("a2:"))
        self.b2 = int(input("b2:"))
        points.append(self.a1)
        points.append(self.b1)
        points.append(self.a2)
        points.append(self.b2)
        
        return points
    
    def dist(self):
        return math.sqrt((self.a1 - self.a2)**2 + (self.b1 - self.b2)**2)

point = Point(1,4,6,3)

print(point.show())
print(point.move())
print(point.dist())
        

#exercise5
class MyBank:
    def __init__(self, profile, money):
        self.profile=profile
        self.money=money
        
    def owner(self):
        return self.profile
    
    def balance(self):
        return self.money
    
    def deposite(self, money):
        self.money+=money
        return f"deposite {money}"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "no money"
        else:
            self.money-=money
            return f"You balance: {self.money}, and you take: {money}"
        
        
user=MyBank("Muhtar", 4000)
print(user.owner())
print(user.balance())
print(user.deposite(4000))
print(user.withdraw(6000))
print(user.withdraw(5000))



#exercise6
class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [5, 14, 13, 17, 19, 23]
prime_filter = Prime(numbers)
prime_numbers = prime_filter.filter_primes()

print("Prime numbers:", prime_numbers)
    
    
    