name = "Muhammad Enuh";
age = 20;
height = 5.9; # in feet
is_student = True;
courses = ["Math", "Science", "History"];
grades = {"Math": "A", "Science": "B", "History": "A"};
print("Name:", name);
print("Age:", age);
print("Height:", height);
print("Is Student:", is_student);
print("Courses:", courses);
print("Grades:", grades);
# This is a comment


# Bilangan INT yang tidak memiliki koma
x = 10
y = -5
z = 0

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'int'>


# Bilangan FLOAT yang memiliki koma
a = 10.5
b = -3.14
c = 0.0

print(type(a))  # Output: <class 'float'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'float'>

# notasi scientific
d = 1.5e3  # 1.5 x 10^3
print(d)    # Output: 1500.0
print(type(d))  # Output: <class 'float'>
e = 2.5e-4  # 2.5 x 10^-4
print(e)    # Output: 0.00025
print(type(e))  # Output: <class 'float'>


# Multiple assignment
x, y, z = 1, 2.5, "Hello"
print(x)  # Output: 1
print(y)  # Output: 2.5
print(z)  # Output: Hello

a = b = c = 100
print(a)  # Output: 100
print(b)  # Output: 100
print(c)  # Output: 100

# Constants (by convention, use uppercase variable names)
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458  # in meters per second
print(PI)
print(GRAVITY)
print(SPEED_OF_LIGHT)

# Type conversion
x = 10        # int
y = 3.14      # float
z = "100"     # string

# Convert int to float
x_float = float(x)
print(x_float)        # Output: 10.0
print(type(x_float))  # Output: <class 'float'>

# Convert float to int
y_int = int(y)
print(y_int)        # Output: 3
print(type(y_int))  # Output: <class 'int'>

# Convert string to int
z_int = int(z)
print(z_int)        # Output: 100
print(type(z_int))  # Output: <class 'int'>


# Mengubah Variabel
x = 5
print("Initial x:", x)  # Output: Initial x: 5
x = 10
print("Updated x:", x)  # Output: Updated x: 10