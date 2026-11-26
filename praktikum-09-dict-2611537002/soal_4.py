student = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
submit = input("Yang mengumpulkan tugas: ").split()
murid_nakal = len(student) - len(submit)
malas = student - set(submit)

print("Submitted ", len(set(submit)))
print("Not submitted: ", murid_nakal, "Students")

for nakal in murid_nakal:
    print(nakal)
