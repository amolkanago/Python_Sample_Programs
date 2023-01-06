# Given two variable of integer type a and b, exchange their values without using
# a third temporary variable.
a = 10
b = 20

print(f"a = {a}")
print(f"b = {b}")

a, b = b, a
print("******************")
print(f"a = {a}")
print(f"b = {b}")




# Another method to solve is by using function.
def exchange1(a, b):
    a, b = b, a
    return a, b


print(exchange1(10, 20))
