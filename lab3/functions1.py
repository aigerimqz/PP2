#ex1
# def convert(gram):
#     ounces = gram * 28.3495231
#     print(f'{gram} gram = {ounces} ounces')

# x = float(input("Write the amount of gram: "))
# convert(x)


#ex2
# def FahrenToCenti(f):
#     c = (5 / 9) * (f - 32)
#     print(f'{f} F = {c} C')
# x = float(input("Write the amount of Fahrenheit temperature: "))
# FahrenToCenti(x)


#ex3
# def solve(numheads, numlegs):
#     numrabbits = (numlegs - (numheads * 2))/2
#     numchickens = numheads - numrabbits
#     print(f'Number of rabbits: {numrabbits}')
#     print(f'Number of chickens {numchickens}')
# x = int(input("Write number of heads: "))
# y = int(input("Write numbers of legs: "))
# solve(x, y)


#ex4
# def filter_prime(listnum):
#     for x in listnum:
#         cnt = 0
#         for y in range(1, x + 1):
#             if(x % y == 0):
#                 cnt += 1
#         if(cnt == 2):
#             print(x)
       

# n = int(input("Write number of elements: "))

# mylist = list(map(int, input("Write the numbers: ").strip().split()))[:n]
# # for i in range(0, n):
# #     el = int(input())
# #     mylist.append(el)
# print("Prime numbers from the mylist: ")
# filter_prime(mylist)



#ex5
# from itertools import permutations
# def allperm(a):
#     p = permutations(x)
#     print(f"All permutations of {x}: ")
#     for i in p:
#         perm = ""
#         for j in i:
#             perm += j
#         print(perm)

# x = input("Write the string: ")
# allperm(x)




#ex6
# def func(s):
#     rev = ""
#     lst = s.split(" ")
#     for i in range(len(lst) - 1, -1, -1):
#         rev += lst[i] + " "
#     print(rev.strip())

# x = input("Write the string: ")
# print("Reversed: ")
# func(x)


#ex7
# def has_33(nums):
#     cnt = 0
#     for i in nums: 
#         if i == 3:
#             cnt += 1
#         else:
#             cnt = 0
#     if cnt >= 2:
#         return True
#     else:
#         return False


# lst = list(map(int, input("Enter the numbers: ").split()))
# print(has_33(lst))



#ex8
# def spy_game(nums):
#     cnt = 0
#     cnt7 = 0
#     for i in nums:
#         if i == 0:
#             cnt += 1
#         if cnt >= 2:
#             if i == 7:
#                 cnt7 += 1

#     if(cnt >= 2 and cnt7 >= 1):
#         print(True)
#     else:
#         print(False)
    
# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])


#ex9
# import cmath
# def volume(r):
#     v = 4/3*(cmath.pi)*(r**3)
#     print(v)

# x = float(input("Raduis: "))
# print("The volume: ")
# volume(x)

#ex10
# def uniq(lst):
#     uniqlist = []
#     for i in lst:
#         if i not in uniqlist:
#             uniqlist.append(i)
    
#     return uniqlist
# mylist = list(map(int, input("Write elements of list: ").split()))
# print("Unique list: ", uniq(mylist))



#ex11
# def isPalindrom(word):
#     rev = ""
#     for i in range(len(word) - 1, -1, -1):
#         rev += word[i]
#     if word == rev:
#         print("YES")
#     else:
#         print("NO")

# x = input("Write the word: ")
# isPalindrom(x)

#ex12
# def histogram(lst):
#     for i in lst:
#         print("*"*i)

# x = int(input("Write the number of elements in the list: "))
# mylist = list(map(int, input("Write the elements: ").strip().split()))[:x]
# histogram(mylist)



#ex13
# import random
# print("Hello! What is your name?")
# name = input()
# print(f"Well, {name}, I am thinking of a number between 1 and 20.")
# x = random.randint(1, 20)
# ans = False
# cnt = 0
# while(ans == False):
#     cnt += 1
#     print("Take a guess.")
#     num = int(input())
#     if(num < x):
#         print("Your guess is too low.")
#     elif(num > x):
#         print("Your guess is too high")
#     else:
#         ans = True
# print(f"Good job, {name}! You guessed my number in {cnt} guesses!")

