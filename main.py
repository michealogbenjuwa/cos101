def calculate_distance():
    speed = float(input("Enter the value for speed"))
    time = float(input("Enter the value for time"))
    distance = (speed * time)
    print("Enter the value for distance:",distance,"km")

def calculate_velocity():
    distance = float(input("Enter the value for distance"))
    time = float(input("Enter the value for time"))
    velocity = (distance * time)
    print("Enter the value for velocity:",velocity, "km/h")

def calculate_multiplication():
    a = float(input("enter the value for a "))
    b = float(input("enter the value for b "))
    result = (a * b)
    print("result:",result)


def calculate_exponentiation():
    a = float(input("enter the value for a "))
    b = float(input("enter the value for b "))
    result = (a ** b)
    print("result:",result)

def calculate_rectangle_area():
    length = float(input("enter the value for length "))
    width = float(input("enter the value for width "))
    area = (length * width)
    print("The value of area is:",area, "cm" )

start = int(input("Type 1 to calculate distance\nType 2 to calculate the length of the velocity\nType 3 to calculate multiplication\nType 4 to calculate exponentiation\nType 5 to calculate rectangle area"))

print(start)

if start == 1:
    calculate_distance()
elif start == 2:
    calculate_velocity()
elif start == 3:
    calculate_multiplication()
elif start == 4:
     calculate_exponentiation()
elif start == 5:
    calculate_rectangle_area()
else:
    print("Invalid entry")

