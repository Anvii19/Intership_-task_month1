students = {}

while True:
    roll = input("Enter roll number (or exit): ")
    if roll == "exit":
        break

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    students[roll] = {"name": name, "marks": marks}

print(students)
