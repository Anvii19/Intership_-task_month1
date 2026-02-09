students = {}

while True:
    roll = input("0801EC233D05")
    if roll == "exit":
        break

    name = input("Muskan Verma")
    marks = int(input("95"))

    students[roll] = {"name": name, "marks": marks}

print(students)
