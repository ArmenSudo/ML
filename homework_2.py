# Digit_Product

number = int(input())
product = 1
while number > 0:
    if number % 10:
        product *= number % 10
    number //= 10
print(product)


# Largest Power of 3

number = int(input())
l = 0

while True:
    if 3**l > number:
        print(3**(l-1))
        break
    l += 1

# Triangle

sides = [int(input()), int(input()), int(input())]
sides.sort()
if sides[2] >= sides[1] + sides[0] or sides[0] <= 0:
    print('No Triangle')
elif sides[2] ** 2 > sides[1] ** 2 + sides[0] ** 2:
    print('Obtuse Triangle')
elif sides[2] ** 2 == sides[1] ** 2 + sides[0] ** 2:
    print('Right Triangle')
else:
    print('Acute Triangle')

# The Root of the Number

number = int(input())


def sum_n(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


while number >= 10:
    number = sum_n(number)
    print(number)


# Number Of Divisors

number = int(input())
count = 1
for x in range(2, (number // 2) + 1):
    if not(number % x):
        count += 1

print(count + 1 if number != 1 else count)

# Quadratic Equation

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print('Non-quadratic equation')
    if b == 0 and c == 0:
        print('Infinite solutions')
    elif b == 0:
        print('No Solutions')
    else:
        print('One solution: ', -c / b)
else:
    print('Quadratic equation')
    disc = b ** 2 - 4 * a * c
    print('Discriminant:', disc)
    arm_dis = disc ** (1 / 2)
    if disc < 0:
        print('No Solutions')
    if disc > 0:
        print('Two solut ions:', - b + arm_dis / 2 / a, - b - arm_dis / 2 / a)
    if disc == 0:
        print('One solution: ', - b / 2 / a)
