#1 sum of num
def sum_list(given_list):
    if len(given_list) == 1:
        return given_list[0]
    else:
        return given_list[0] + sum_list(given_list[1:])

list = [2,4,6,8,9,422,233,1]
print(sum_list(list))

#2 check even or odd
input = int(input("Give me a number: "))
def check(x):
    if x == 0:
        return "even num."
    elif x % 2 == 0:
        return "even num"
    else:
        return "odd num"

print(f"The number {input} is a " + check(input))

#3 Factorial of a num
def factorial(num):
    factorial = 1
    while num != 0:
        factorial *= num
        num -= 1
    print(f"The factorial of it is {factorial}.")

x = input("What number?: ")
factorial(int(x))


