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



n = 9
for i in range(n+1):
    for j in range(n+1):
        if i == 0 or i == n or j == 0 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


a = "My name is Yuvaraj"
b = ""
for i in a:
    b = i + b
print(b)

c =""
for i in range(len(a)-1, -1, -1):
    c += a[i]
print(c)



name = "chetan"
count =0
aeiou = ""


for ch in name:
    if ch in "aeiouAEIOU":
        count = count + 1
        aeiou = ch + aeiou
print(count)
print(aeiou)


list = [1, 3, 4, 500, 9, 67]
largest = list[0]
for lar in list:
    if largest < lar:
        largest = lar
print(largest)



list1 = [1, 3, 4, 56, 67, 89, 454, 35, 7]
second_largest = sorted(list1)
print("Second Largest Number", second_largest[-2])


text = input("Enter String: ")
for ch in text:
    print(ch)


string = "my name is python"
Reverse = ""
for i in range(len(string)-1, -1, -1):
    Reverse += string[i]
print("Reverse String: ", Reverse)

SR = "My Name is Yuvaraj"
Vowels =""
for ch in range(len(SR)):
    if SR[ch] in "aeiouAEIOU":
        Vowels += SR[ch]
print("Vowels in String: ", Vowels)

SRE = "My Name is Yuvaraj"
count = 0
for ch in range(len(SRE)):
    if SRE[ch] in "aeiouAEIOU":
        count += 1
print("Count of Vowels in String: ", count)


name = "My Name is Yuvaraj & My Email is yuvaraj1223@gmail.com"
Lowercase = 0
Uppercase = 0
Digit = 0
Specialchar = 0
for ch in range(len(name)):
    if name[ch].islower():
        Lowercase += 1
    elif name[ch].isupper():
        Uppercase += 1
    elif name[ch].isdigit():
        Digit += 1
    else:
        Specialchar += 1
print(f"Lowercase: {Lowercase},\n Uppercase: {Uppercase}, \n Digit: {Digit}, \n Specialchar: {Specialchar}")

name = "My Name is Yuvaraj & My Email is yuvaraj1223@gmail.com"
Lowercase = ""
Uppercase = ""
Digit = ""
Specialchar = ""
for ch in name:
    if ch.islower():
        Lowercase += ch
    elif ch.isupper():
        Uppercase += ch
    elif ch.isdigit():
        Digit += ch
    else:
        Specialchar += ch
result = Digit + Specialchar + Lowercase + Uppercase
print("Total Characters in Order: ", result)


num = input("Enter Number: ")
Sum = 0
for ch in num:
    if ch.isditgit():
        Sum += int(ch)
print("Sum of Digits in Number: ", Sum)