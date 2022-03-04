# with open("file_name","w+") as f:  # create and write  file if doesn't exists

# # Exercise 1, read an entire text file
# with open("sample_text","r") as f:
#     print(f.read())

# # Exercise 2, read first n lines of file
# # 1st method
# with open("sample_text","r+") as f:
#     k = [(next(f)) for i in range(2, 4)]
#     print(k,end="")
# # 2nd method
# with open("sample_text", "r+") as f:
#     for i in range(2,4):  # line 2-3
#         print(next(f),end="")  # next(), returns next item from iterator

# # Exercise 3, count most frequent word
# def fre_word(file):
#     with open(file,"r") as f:
#         words = f.read().split()
#         max_f = 0
#         for i in words:
#             freq = words.count(i)
#             if freq > max_f:
#                 max_f = freq
#                 wor = i
#         return max_f,wor
#
# print(fre_word("poem.txt"))

# # Exercise 4, find longest word
# def read(file):
#     with open(file,"r") as f:
#         text = f.read().split()
#         max = 0
#         for i in text:
#             if len(i) > max:
#                 max = len(i)
#                 max_word = i
#         return max_word,max
#
# print(read("poem.txt"))