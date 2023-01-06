a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print("The value of a,b and c before swapping")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

t = a
a = c
c = b
b = t

print("The value of a,b and c after swapping")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")