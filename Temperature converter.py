type_1 = input("Which kind of temperature are you converting from? (Celsius, Fahrenheit, Kelvin): ")
type_2 = input("Which kind of temperature are you converting to? (Celsius, Fahrenheit, Kelvin): ")
type_3 = input("What is the temperature? (only enter the number): ")

def change_temp(this, that, num):
    if this == "Celsius":
        if that == "Fahrenheit":
            return (int(num))*9/5 + 32
        elif that == "Kelvin":
            return (int(num)) + 273.15
        else:
            return num
    elif this == "Fahrenheit":
        if that == "Celsius":
            return (int(num)-32)*5/9
        elif that == "Kelvin":
            return (int(num)-32)*5/9 + 273.15
        else:
            return num
    else:
        if that == "Celcius":
            return num-273.15
        elif that == "Fahrenheit":
            return (num-273.15)*9/5+32
        else:
            return num

print(change_temp(type_1,type_2,type_3))