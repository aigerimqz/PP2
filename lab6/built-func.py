#ex1 bulit-in functions len(), print(), range() are used here
# def to_multiply(lst):
#     x = lst[0]
#     for i in range(1, len(lst)):
#         x *= lst[i]
#     print(x)
# x = list(map(int, input("Write the numbers:").split()))
# to_multiply(x)



#ex2 bulit-in functions ord(), print(), input() are used here
# s = input("Write the string:")
# def calc(str):
#     cntu = 0
#     cntl = 0
#     for i in str:
#         k = ord(i)
#         if k >= 65 and k <= 90:
#             cntu += 1
#         elif k >= 97 and k <= 122:
#             cntl += 1
#     print("Number of upper case letters:", cntu)
#     print("Number of lower case letters:", cntl)
    
# calc(s)




#ex3 bulit-in functions reversed(), print(), input() are used here
# s = input("Write the string:")
# def isPalindrome(str):
#     r = reversed(str)
#     rev = ""
#     for i in r:
#         rev += i

#     if (str == rev):
#         print("Yes, palindrome")
#     else:
#         print("No, not palindrome")


# isPalindrome(s)


#ex4 
# import math
# import time
# def sq_root(x):
#     s = math.sqrt(x)
#     return s
# num = int(input())
# mili = int(input())
# time.sleep(mili/1000)
# print(f"Square root of {num} after {mili} miliseconds is {sq_root(num)}")

#ex5 built-in functions all(), print() are used here
tup = (23, "hello", True, 0)
if all(tup):
    print("Yes, all elements are true!")
else:
    print("No, not all are true...")


            
