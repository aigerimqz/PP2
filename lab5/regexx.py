import re
with open('row.txt', 'r', encoding="UTF-8") as file1:
    object = file1.read()

# p = re.compile('ДУБЛИКАТ')
# f = re.findall("ДУБЛИКАТ", object)
# m = re.search(p, object)
# print(f)


#ex1 a and zero or more b
# t = "aabbb hello abb bbacc"
# user = "abbbbbb"
# p = re.compile("ab*")
# m = re.search(p, user)
# print("......")
# if m:
#     print(f"Yes, your string '{user}' it has an 'a' followed by zero or more 'b's")
# else:
#     print(f"No, your string  '{user}' hasn't an 'a' followed by zero or more 'b's")




#ex2 has an a followed by two to three b
# user = "abb"
# p = re.compile("ab{2,3}")
# m = re.match(p, user)
# print(".....")
# if m:
#     print(f"Yes, your string '{user}' has an 'a' followed by two to three 'b'")
# else:
#     print(f"No, your string '{user}' hasn't an 'a' followed by two to three 'b'")





#ex3 sequences of lowercase letters joined with a underscore
# user = "bvff_jjjrrr"
# p = re.compile("[a-z]+_[a-z]+")
# m = re.match(p, user)
# if m:
#     print(f"Yes, your string '{user}' has such sequence")
# else:
#     print(f"No, your string '{user}' hasn't such sequence")



#ex4 sequences of one upper case letter followed by lower case letters
# user = "Adhh_?dfAdhd"
# p = re.compile("[A-Z]{1}[a-z]+")
# m = re.match(p, user)
# f = re.findall(p, user)
# if m:
#     print(f"Yes, this string '{user}' has such sequence")
#     print(f)
# else:
#     print(f"No, this string '{user}' hasn't such sequence")



#ex5 matches a string that has an 'a' followed by anything, ending in 'b'
# user = "a-DID&b"
# p = re.compile("^a.+b$")
# m = re.match(p, user)
# if m:
#     print(f"Yes, this string '{user}' matches such string")
# else:
#     print(f"No, this string '{user}' doesn't match such string")


#ex6 replace all occurrences of space, comma, or dot with a colon
# user = "s.djhsd,hj s.jdjsd.js djsjss  djjsd"
# p = re.compile("[ |,|.]")
# res = re.sub(p, ":", user)
# print(res)


#ex7 convert snake case string to camel case string
# user = "apple_banana_pear_orange_lemon_watermelon"
# # user = input("Write your string in snake case: ")
# p = re.compile("_[a-z]")
# m = p.search(user)
# f = re.findall(p, user)
# lst = re.split(p, user)
# camel = lst[0]
# cnt = 1
# for i in f:
    
#     res = re.sub(p, i[1].upper(), m.group())
#     camel += res
#     camel += lst[cnt]
#     cnt += 1

# print("This is your string in camel case:", camel)


#ex8 split a string at uppercase letters
# user = "ccccSDccccSSSScccScc"
# p = re.compile("[A-Z]+")
# res = re.split(p, user)
# print(res)


#ex9 insert spaces between words starting with capital letters
# user = "AppleBookJokeshhsdhsdOpenCloseHello"
# # user = input("Write your string: ")
# p = re.compile(r"((?<!^)(?=[A-Z]))")
# res = re.sub(p, " ", user)
# print(res)


#ex10 convert a given camel case string to snake case
user = input("Write your string in camel case: ")
# p = re.compile("[?<!^][?=[A-Z]]")
p = re.compile("[A-Z]+")
m = re.findall(p, user)
# res = re.sub(p, "_", user)
s = re.split(p, user)
# print(res)
snake = ""
if s[0] != '':
    snake += s[0]
    snake += "_"

cnt = 1
for i in m:
    snake += i.lower()
    snake += s[cnt]
    if cnt != len(s) - 1:
        snake += "_"

    cnt += 1

print("This is your string in snake case:", snake)




