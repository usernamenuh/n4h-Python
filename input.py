name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer
height = float(input("Enter your height in meters: "))  # Convert input to float
is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'  # Convert input to boolean
courses = input("Enter your courses (comma separated): ").split(',')  # Convert input to list
grades = [float(grade) for grade in input("Enter your grades (comma separated): ").split(',')]  # Convert input to list of floats

print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Courses:", [course.strip() for course in courses])  # Strip whitespace from each course
print("Grades:", grades)    


x = input("Masukan Angka Pertama : ")
y = input("Masukan Angka Kedua : ")

h = int(x) + int(y)
print("Hasilnya adalah : " + str(h))