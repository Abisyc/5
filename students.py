students={"alpha":55,"syc":77,'lapres':55}
a=input("enter the name of the student")
if a in students:
    print(f"{a}'s marks is {students[a]}")
    print(students["syc"])
else:
    print("student not found")