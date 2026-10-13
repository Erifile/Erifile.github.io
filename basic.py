## 1)
# try:
#     a = int(input("Ваше число: "))
#     if a > 0:
#         a = a + 1
#     elif a < 0:
#         a = a - 2
#     elif a == 0:
#         a = 10
# except ValueError:
#     print("Ошибка. Введите целое число.")
# else:
#     print(f"Преобразованное число: {a}")

# 2)

# try:
#   a = int(input("Число 1: "))
#   b = int(input("Число 2: "))
#   c = int(input("Число 3: "))

#   nums = [a, b, c]

#   pluses = 0
#   minuses = 0



#   for num in nums:
#     if (num > 0):
#       pluses += 1
#     if (num < 0):
#       minuses += 1
# except ValueError:
#   print("Ошибка. Введите число")
# else:
#   print(f"Количество положительных: {pluses}")
#   print(f"Количество отрицательных: {minuses}")

# 3)

# try:
#   a = int(input("Число 1: "))
#   b = int(input("Число 2: "))

#   if (a != b):
#     if (a > b):
#       a = a + a
#       b = b + a
#     if (b > a):
#       a = a + b
#       b = b + b
#   if (a == b):
#     a = 0
#     b = 0

# except ValueError:
#   print("Ошибка. Введите число")
# else:
#   print(f"Преобразованные числа: {a}, {b}")


# 4)

# a = float(input("Введите рациональное число 1: "))
# b = float(input("Введите рациональное число 2: "))
# c = float(input("Введите рациональное число 3: "))

# if (a < b < c):
#   a = a * 2
#   b = b * 2
#   c = c * 2
# else:
#   a = -a
#   b = -b
#   c = -c

# print(f"Преобразованные числа: {a}, {b}, {c}")

# 5) 

print("Введите 3 одинаковых и 1 отличное число")
a = int(input("Число 1: "))
b = int(input("Число 2: "))
c = int(input("Число 3: "))
d = int(input("Число 4: "))
nums = [a, b, c, d]

if (len(set(nums)) > 2):
  print("Ошибка. Введите 1 отличное число")
  exit()

nums = [a, b, c, d]

for num in nums:
  if num != num[len(nums) - 1]:
    print(num)

