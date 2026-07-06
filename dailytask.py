a = int(input("Enter Number:"))
if a % 2 == 0:
    print("Even Number")
else:
    print(("Odd Number"))


for i in range(1, 8):
    print(i * " *")

print("\n")

for i in range(7, 0, -1):
    print(i * " *")

print("\n")
n = 8
for i in range(1, n):
    print(" " * (n-i), i * "* ")

print("\n")

for i in range(1, n):
    print(" "*(n-i), i*"* ")
for i in range(8, 0, -1):
    print(" "*(n-i), i*"* ")




a = "My name is Yuvaraj"
b = ""
for i in a:
    b = i + b
print(b)