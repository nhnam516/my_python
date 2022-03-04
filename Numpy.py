import numpy as np

# # Exercise 1, check if none of the elements are zero
# x = np.array([0,1,2,3])
# y = np.array([1,2,3,4])
# print(np.all(x))  # check if all elements return True
# print(np.all(y))
#
# # Exercise 2, check if any of the elements are non-zero
# x = np.array([0,1,0,0])
# y = np.array([0,0,0,0])
# print(np.any(x))
# print(np.any(y))

# # Exercise 3, element-wise comparison of two arrays
# x = np.array([[2,5],[3,4]])
# y = np.array([[3,5],[1,6]])
# print(np.greater(x,y))  # compare if x is greater than y  # can great_equal / less...

# # Exercise 4  calculate array's memory size
# x = np.array([1,7,13,105,9,80])
# y = np.array([1,7])
# y = np.array([1,7,3])
# print(x.size)  # num of elements
# print(x.itemsize)  # space occupied by each elements
# print(x.size * x.itemsize)  # memory size occupied by array
#
# print(y.itemsize)
# print(np.array(["you","hi","lol",4]).itemsize)
# print(np.array(["you","hi","lol","4"]).itemsize)
# print(np.array(["you"]).itemsize)
# print(np.array(["hiiiiiiiiiiiiii"]).itemsize)

# # Exercise 5  create array
# ans_0 = np.zeros(10)
# print(ans_0)
#
# ans_1 = np.ones(10)  # just line
# print(ans_1)
#
# ans_5 = np.ones(10)*5  # create array of 1, then multiply element-wise by 5
# print(ans_5)
#
# x = np.zeros((2,5))  # have shape
# y = np.ones((5,2))
# print(x)
# print(y)

# # Exercise 6, len() and np.shape() difference
# a = np.array([1])
# x = np.array([[1],[2]])
# y = np.array([[1,2,3],[3,4,5]])
# print(a)
# print(x)
# print(y)
# print("/"*40)
#
# print(len(a))  # print length of axis 1 (num of rows)
# print(len(x))
# print(len(y))
# print("/"*40)
#
# print(np.shape(a))  # print matrix size (eg. 2 by 3)
# print(np.shape(x))
# print(np.shape(y))

# # Exercise 7, create array of int from 30 to 70
# x = np.arange(30,71)
# print(x)

# # Exercise 8, create 3 by 3 identity matrix
# x = np.eye(3)  # () input size of identity matrix (? by ?)
# print(x)
#
# print(np.eye(4)*8)  # can modify diagonals
# print(np.identity(4))*8  # can't modify diagonals

# # Exercise 9, generate a random number between 0 and 1
# x = np.random.randint(low=0,high=2,size=(2,2))
# print(x)

# # Exercise 10, generate 15 random num with normal distribution
# x = np.random.normal(loc=5,scale=4,size=15)  # loc: centre, scale: spread)
# print(x)

# # Exercise 11, create vector with values ranging 15-55,  print all except first and last
# x = np.arange(15,56)  # print array with 15-55
# print(x)
#
# x_sliced = x[1:-1]  # slice away first and last
# print(x_sliced)  # or simply print(x[1:-1])

# # Exercise 12, create 3X4 array using and iterate over it
# x = np.arange(12).reshape(3,4)  # create 3X4 array
# print(x)
# y = np.arange(11,20).reshape(3,3)
# print(y)
# for i in np.nditer(x):
#     print(i,end=" ")
# print()
# for i in np.nditer(y,order="F"):
#     print(i,end=",")

# # Exercise 13,  create vector of length 10 and values evenly distributed between 5 and 50
# x = np.linspace(5,50,10)
# print(x)

# # Exercise 14, create vector with values from 0 to 20, change the sign of the numbers in the range from 9 to 15
# x = np.arange(0,21)
# print(x)
# x[(9<=x) & (x<=15)] *= 3
# print(x)

# # Exercise 15, create vector of length 5 filled with arbitrary integers 0-10
# x = np.random.randint(0,11,size=5)
# print(x)

# # Exercise 16, multiply the values of two given vectors
# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])
# z = x * y
# print(z)

# # Exercise 17, create 3x4 matrix filled with values from 10 to 21
# x = np.arange(10,22).reshape(3,4)  # gen number in a range and order it
# y = np.random.randint(10,22,size=(3,4))  # gen number randomly within the range
# print(x)
# print(y)

# # Exercise 18, find number of rows and columns of a given matrix
# x = np.random.randint(6,size=(2,3))
# print(x)
# print(x.shape)

# # Exercise 19, create a 3x3 identity matrix
# x = np.eye(3)
# print(x)

# # Exercise 20, create 10x10 matrix, elements on borders is 1, and inside 0
# x = np.ones((10,10))
# x[1:9,1:9] = 0
# print(x)

# # Exercise 21, create 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5
# x = np.diag([1,2,3,4,5])
# print(x)

# # Exercise 22, create 4x4 matrix in which 0 and 1 are staggered,zeros on main diagonal
# # O 1 O 1
# # 1 O 1 O
# # O 1 O 1
# # 1 O 1 O
# x = np.zeros((4,4))
# x[::2,1::2] = 1
# x[1::2,::2] = 1
# print(x)

# # Exercise 23, create a 3x3x3 array filled with arbitrary value
# x = np.random.random((3,3,3))  # when randomly make ? by ? matrix
# y = np.random.randint(1,100,size=(3,3,3))  # when need set max min value
# print(x)
# print(y)

# # Exercise 24, cal sum of all elements, sum of each column and sum of each row of a given array
# x = np.array([[2,2,2],[5,3,3]])
# print(x)
# print("sum of all elements: ", np.sum(x))
# print("sum of each column: ", np.sum(x,axis=0))
# print("sum of each row: ", np.sum(x,axis=1))

# # Exercise 25,  compute inner product of two given vectors
# x = np.array([3,5,6])
# y = np.array([[2],[4],[3]])
# print(x)  # 1*3
# print(y)  # 3*1
# print(np.dot(x,y))

# # Exercise 26, add a vector to each row of a given matrix
# x = np.array([[2,3],[4,6]])
# y = np.array([3,5])
# print(x)
# print(y)
# answer = np.empty_like(x)
# for i in range(len(x-1)):
#     answer[i, :] = x[i, :] + y
# print(answer)

# # Exercise 27, save a given array to a binary file
# import os
# x = np.arange(20)
# np.save('file_name.npy', x)  # (fname,var_name)
# my_list = [[1,4],[8,9]]
# x = np.array(my_list)
# y = x.tolist()
# # print(my_list)
# # print(x)
# # print(y)
# print(y == my_list)
# print(x == my_list)

# # Exercise 28, convert numpy dtypes to native python types
# x = np.float32(0)
# print(type(x))
# y = x.item()
# print(type(y))

# # Exercise 29, check whether two arrays are equal (element wise)
# x = np.array([0.5, 1.5, 0.2])
# y = np.array([0.4999999999, 1.500000000, 0.2])
# np.set_printoptions(precision=10)  # 10 decimal places
# print(x)
# print(y)
#
# print(np.all(x == y))
# print(x == y)
# print(np.equal(x, y))

# # Exercise 30, create one dimensional array of forty pseudo-randomly generated values
# # random numbers from a uniform distribution between 0 and 1
# x = np.random.normal(loc=0.5,scale=0.5,size=140)
# y = np.random.rand(40)  # default uniform distribution [0, 1)
# print(x)
# print(y)

# # Exercise 31,  convert a list into a one-dimensional NumPy array
# list = [12.23, 13.32, 100, 36.32]
# x = np.array(list)
# print(x)

# # Exercise 32. convert array to float type
# x = np.array([2,3,4,3,4,5])
# y = np.asfarray(x)
# print(y)

# # Exercise 33, test if each element of 1-D array is also in second array
# x = [0,10, 20, 40, 60]
# y = [0, 40]
# print(np.in1d(x,y))

# Exercise 34, find common values between two arrays
x = np.array([0, 10, 20,40, 60])
y = np.array([10, 40])
print(np.intersect1d(x,y))

# Exercise 35, get unique elements
x = [10, 10 ,20 ,20, 30,30]
print(np.unique(x))