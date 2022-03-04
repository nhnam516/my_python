# add_15 = lambda x: x+15
# print(add_15(10))
#
# times = lambda x,y: x*y
# print(times(6,8))

# # //////////////////////////////////////
# def mult(n):
#     return lambda x:x*n
#
# result = mult(5)
# print(result(4))

# # //////////////////////////////////////
# list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# list.sort(key=lambda x: x[1])
# print(list)

# # //////////////////////////////////////
# given_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# given_list.sort(key=lambda x:x["color"])
# print(given_list)

# # //////////////////////////////////////
# given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print("Even number is: {}".format(list(filter(lambda x: x % 2 == 1,given_list))))
# print("Odd number is: {}".format(list(filter(lambda x: x % 2 == 1,given_list))))

# # //////////////////////////////////////
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# square_ans = map(lambda x : x**2, numbers)
# print(list(square_ans))
# cube_ans = map(lambda x: x**3, numbers)
# print(list(cube_ans))

# # //////////////////////////////////////
# first_char = lambda x: True if x[0] == "h" else False
# print(first_char("hasid"))

# # //////////////////////////////////////
# import datetime
# current_datetime = datetime.datetime.now()
#
# print(current_datetime.year)
# print(current_datetime)
#
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# time = lambda x: x.time
#
# print(year(current_datetime))
# print(month(current_datetime))
# print(day(current_datetime))
# print(t(current_datetime))

# # //////////////////////////////////////
# given_str = "hi, how are you today, I am fine!"
# ans = lambda x: True if isinstance(x,str) else False
# print(ans(given_str))

# # //////////////////////////////////////
# nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# nums2 = [1, 2, 4, 8, 9]
#
# ans = filter(lambda x: x in nums1, nums2)
# print(list(ans))

# # //////////////////////////////////////
# numbers = [1, 2, 3, 5, 7, 8, 9, 10]
# ans_even = filter(lambda x: x % 2 == 0, numbers)
# ans_odd = filter(lambda x: x % 2 == 1, numbers)
# print(f"number of even numbers are: {len(list(ans_even))}")
# print(f"number of odd numbers are: {len(list(ans_odd))}")

# # //////////////////////////////////////
# given_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
#
# given_list.sort(key=lambda x:(len(x),x[0]))
# print(given_list)

# # //////////////////////////////////////
# nums = [12,33,23,10.11,67,89,45,66.7,23,12,11,10.25,54]
#
# result_max = max(enumerate(nums),key=lambda x:x[1])
# result_min = min(enumerate(nums),key=lambda x:x[1])
# print(result_max)
# print(result_min)