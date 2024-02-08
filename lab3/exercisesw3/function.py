# def recursion(k):
#     if k > 0:
#         res = k + recursion(k - 1)
#         print(res)
#     else:
#         res = 0
#     return res

# recursion(6)


#ex1
def my_function():
    print("Hello from a function")


#ex2
def my_function():
    print("Hello from a function")
my_function()

#ex3
def my_function(fname, lname):
    print(fname)

my_function("Aigerim", "Manat")


#ex4
def my_function(x):
    return x + 5
print(my_function(5))

#ex5
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Fred", "George", "Ron")


#ex6
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Aigerim", lname = "Manat")
