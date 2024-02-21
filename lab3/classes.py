#ex1
# class String_up():
#     def __init__(self, str):
#         self.str = str
#     def getString(self):
#         self.str = str
#     def printString(self):
#         new = self.str
#         print(new.upper())


# x = String_up(input("Write the string: "))
# x.printString()


#ex2
# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
        
#     def area(self):
#         return (self.length*self.length)

# usernum = int(input("Write the number: "))
# p = Square(usernum)
# a = p.area()
# print(f"The area of length {usernum} is {a}")


#ex3
# class Shape():
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
        
#     def area(self):
#         return (self.length*self.length)

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = length
#         self.width = width
#     def area(self):
#         print("Area is", self.length * self.width)


# a = Rectangle(6, 4)
# a.area()



#ex4
# import math
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def show(self):
#         print("Coordinates of the current point:", self.x, self.y)

#     def move(self, newx, newy):
#         self.x = newx
#         self.y = newy
#     def dist(self, point_2):
#         dist = math.sqrt(((point_2.x - self.x)**2) + ((point_2.y - self.y)**2))
#         print("The distance =", dist)
    

# point1 = Point(1, 2)
# point2 = Point(4, 8)
# point1.show()
# point2.show()

# point1.move(0, 5)
# print("Updated")
# point1.show()
# point2.show()

# point1.dist(point2)



# ex5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print("Amount of deposit you are going to put is", deposit_amount)
        print("...")
        print("Updated balance is", self.balance)
    def withdraw(self, withdrawal_amount):
        print("Amount of withdrawal you are going to withdraw is", withdrawal_amount)
        print("...")
        if(withdrawal_amount <= self.balance):
            self.balance = self.balance - withdrawal_amount
            print("You succesfully withdrawed required amount. Updated balance is", self.balance)
        elif(withdrawal_amount > self.balance):
            print("Insufficient funds.")

name = input("Write the owner's name: ")
balance = float(input("Write the balance: "))
p1 = Account(name, balance)
d = float(input("Amount of deposit: "))

p1.deposit(d)
w = float(input("Amount of withdrawal: "))
p1.withdraw(w)

        


#ex6
# def filterprime(num):
#     cnt = 0
#     for i in range(1, num + 1):
#         if(num % i == 0):
#             cnt += 1

#     if cnt == 2:
#         return True
#     else:
#         return False
    
# nums = list(map(int, input().split()))
# filterednums = list(filter(lambda x: filterprime(x), nums))
# print("Prime numbers:", filterednums)