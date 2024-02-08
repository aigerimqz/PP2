#ex1
# class MyClass:
#     x = 5
# print(MyClass.x)



#ex2
# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1)


#ex3
# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)


#ex4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print(self.age)

p1 = Person("Aigerim", 18)
p1.myfunc()
    