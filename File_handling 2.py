# def read_txt(file):
#     with open(file,"r+") as f:
#         text = f.readlines()
#         for i in text:
#             print(i,end="")
#             print(f.tell(),end="")
#
# read_txt("poem.txt")

# def read_txt(file):
#     with open(file,"r+") as f:
#         for i in f:
#             print(i, end="")
#             print("stop")
#
# read_txt("poem.txt")

infile = open('poem.txt', 'r')
# line1 = infile.readline()
# line2 = infile.readline()
# line3 = infile.readline()

line1 = infile.readline().rstrip('\n')
line2 = infile.readline().rstrip('\n')
line3 = infile.readline().rstrip('\n')
print(line1)
print(line2)
print(line3)