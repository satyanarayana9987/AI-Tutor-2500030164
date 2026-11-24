n = int(input("Enter a number of entries: "))
student={}
for _ in range(n):
    key = input("enter key ")
    value = input("enter value ")
    student[key] = value

print(student)
