# ex 1
# def gen_squares(N):
#     for i in range(1, N + 1):
#         yield i*i
# num = int(input("Write the number: "))
# gen = gen_squares(num)
# for a in gen:
#     print(a)


#ex 2
# def gen_onlyeven(N):
#     for i in range(N+1):
#         if i % 2 == 0:
#             yield i

# num = int(input("Write the number: "))
# gen = gen_onlyeven(num)
# evennums = []
# for a in gen:
#     evennums.append(a)

# print(evennums)    


#ex 3
# def gen_divby3and4(N):
#     for i in range(N+1):
#         if(i % 3 == 0) and (i % 4 == 0):
#             yield i
# num = int(input("Write the number: "))
# gen = gen_divby3and4(num)
# for a in gen:
#     print(a)


#ex 4
# def squares_atob(a, b):
#     for i in range(a, b + 1):
#         yield i * i

# a = int(input("Write the number a: "))
# b = int(input("Write the number b: "))
# squares = squares_atob(a, b)
# for a in squares:
#     print(a)


#ex 5
def return_all_num(N):
    for i in range(N, -1, -1):
        yield i

num = int(input("Write the number: "))
gen = return_all_num(num)
for a in gen:
    print(a)