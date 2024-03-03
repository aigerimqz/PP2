import os
#ex1
# p = r"C:\Users\Aigerim\Desktop\pp2\lab6"
# d = []
# f = []
# for path, dires, fils in os.walk(p):
#     for dire in dires:
#         d.append(os.path.join(dire))
#     for fil in fils:
#         f.append(os.path.join(fil))
# print("This path:", p)
# print("-------------")
# print("Directories:", d)
# print("-------------")
# print("Files:", f)
# print("-------------")
# print("All directories and files:", os.listdir(p))


#ex2
# p = r"C:\Users\Aigerim\Desktop\pp2\lab6"
# existence = os.access(p, os.F_OK)
# read = os.access(p, os.R_OK)
# writ = os.access(p, os.W_OK)
# execut = os.access(p, os.X_OK)
# print("Existence:", existence)
# print("Readability:", read)
# print("Writability", writ)
# print("Executability", execut)


#ex3
# p = r"C:\Users\Aigerim\Desktop\pp2\lab6\dir_files.py"
# if os.path.exists(p):
#     print("Yes, path exists!")
#     print("File:", os.path.basename(p))
#     print("Directory portion:", os.path.split(p)[0])
    
# else:
#     print("No, path doesn't exist!")


# ex4
# with open("ex4.txt", "r") as txt:
#     cnt = 0
#     for line in txt:
#         cnt += 1
# print("Number of lines in the text file:", cnt)


#ex5
# lst = ["apple", "orange", "lemon"]
# with open("ex5.txt", "w") as txt2:
#     for line in lst:
#         txt2.write(line + "\n")


#ex6
# letters = []
# for i in range(65, 91):
#     letters.append(chr(i))

# for letter in letters:
#     with open(letter+".txt", "w") as filee:
#         pass
# # for letter in letters:
# #     os.remove(letter+".txt")



#ex7
# import shutil
# # with open("ex7.txt", "r") as txt3, open("ex7_2.txt", "w") as txt4:
# #     for line in txt3:
# #         txt4.write(line)

# shutil.copyfile("ex7.txt", "ex7_2.txt")


#ex8
p = r"C:\Users\Aigerim\Desktop\pp2\lab6\dir2\file2.txt"
if os.path.exists(p):
    os.remove(p)
else:
    print("File doesn't exist!")




        

