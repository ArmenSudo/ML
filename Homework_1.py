# ____  Digit Sum 3 _______

number = int(input())
print((number % 10) + (number // 10) % 10 + number // 100)

# _____  Area of a right triangle  ____

a = int(input())
b = int(input())

print(a*b/2)

# ______  Arithmetic Progression  ______

a1 = int(input())
a2 = int(input())
n = int(input())

print(a1 + (n-1)*(a2-a1))

# ______ Century from year  ________

year = int(input())
print((year+99)//100)


# ______  Two men ______

man1 = int(input())
man2 = int(input())

print(man2 - 1)
print(man1 - 1)

# _______ Knight’s Possible Moves _____

py = int(input())
px = int(input())

print(py-1, px-2)
print(py-1, px+2)
print(py+1, px-2)
print(py+1, px+2)
print(py-2, px-1)
print(py-2, px+1)
print(py+2, px-1)
print(py+2, px+1)