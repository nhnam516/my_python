# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        return f"The rectangle with length and width of {self.length} and {self.width} gives" \
               f"perimeter of {self.perimeter()} and area of {self.area()}."

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.area() * self.height

my_rectangle = Rectangle(6, 5)
my_rectangle.display()
print("----------------------------------")
my_parallelepipede = Parallelepipede(6, 5, 3)
print(f"The volume of my_parallelepipede is {my_parallelepipede.volume()}")


# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The name is {self.name}.")
        print(f"The age is {self.age}.")

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print(f"Student name: {self.name}")
        print(f"The age is {self.age} ")
        print(f"Student section= {self.section}")

p = Person("Tom",23)
p.display()

s = Student("Mary", 56, "science")
s.displayStudent()

Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.
class Coputation:
    def __init__(self):
        pass

    def Factorial(self,x):
        n = 1
        for i in range(1, x + 1):
            n *= i
        return n

    def sum(self,x):
        sum = 0
        for i in range(x):
            sum += i
        return sum

    def test_prime(self, n):
        k = 0
        for i in range(1, n + 1):
            if n % i == 0:
                k += 1
        if k == 2:
            return True
        else:
            return False

    def tableMult(self, x):
        for i in range(1, 10):
            result = i * x
            print(f"{i} times {x} = {result}")

    def listDiv(self, n):
        lDiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                lDiv.append(i)
        return lDiv
