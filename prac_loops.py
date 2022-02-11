#1 first 10 natural num
x = 1
while x < 11:
    print(x)
    x += 1

#2 pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print("")

#3 sum of all num
sum = 0
numbers = input("Enter number: ")
for i in range(len(numbers)):
    sum += i
print(f"Sum of the numbers is: {sum}")

#4 display num from list
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
#given: numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]
result = ""
for i in numbers:
    if i <= 500:
        if i >= 150:
            if i % 5 == 0:
                print(i)
            else:
                print(f"{i} is not divisible by 5")
        else:
            print(f"{i} is smaller than 150")
    else:
        break

#5 Count num of digit
def count_num(x):
    count = 0
    while x != 0:
        x = int(x//10)
        count += 1
    return count

number = input("Give me a number: ")
print(f"Number of digits are: {count_num(int(number))}")

6 print pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
for i in range(0,5):
    for j in range(0,i+1):
        print("*", end="")
    print("")
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print("")


#generate a list of num
#between 4-30, even num
print(list(range(4,30,2)))




