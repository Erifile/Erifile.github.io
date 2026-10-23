import random

randA = random.randint(0, 500)
randB = random.randint(0, 500)
print(randA)
print(randB)
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

# print("Введите 3 одинаковых и 1 отличное число")
# a = int(input("Число 1: "))
# b = int(input("Число 2: "))
# c = int(input("Число 3: "))
# d = int(input("Число 4: "))
# nums = [a, b, c, d]

# if (len(set(nums)) > 2):
#   print("Ошибка. Введите 1 отличное число")
#   exit()

# nums = [a, b, c, d]

# for num in nums:
#   if num != num[len(nums) - 1]:
#     print(num)


# ЦИКЛЫ

# FOR

# 1)

# a = 1
# b = 3
# sum = 0

# for i in range(a, b + 1, 1):
#   sum = sum + i
# print(f"Сумма чисел от {a} до {b} включительно: {sum}")

# 2)

# a = 1
# b = 3
# total = 1

# for i in range(a, b + 1, 1):
#   total = total * i
# print(f"Произведение чисел от {a} до {b} включительно: {total}")

# 3)

# a = 1
# b = 4
# total = 0

# for i in range(a, b + 1, 1):
#   numSquared = i**2
#   total = total + numSquared
# print(f"Сумма квадратов чисел от {a} до {b} включительно: {total}")

# 4)

# a = 3
# total = 0.0

# for i in range(1, a + 1, 1):
#   # начало с 1/1 (1)
#   num = 1/i
#   total = total + num
# print(f"Сумма чисел 1, 1/2, 1/3.. 1/{a} включительно: {total}")

# WHILE

# 5) 

# a = 10
# b = 5
# bLength = b
# bCount = 1
# while (bLength <= a):
#   bLength = bLength + b
#   if (bLength < a):
#     bCount += 1
#   if (bLength > a):
#     print(f"В отрезке длиной {a} уместятся {bCount} отрезков длиной {b}")

## def func_name (): ## дефолтные параметры задаются через =
  # instrcrtc

## при передаче параметров при вызове функции можно по порядку либо уточнять через 0 к какому параметру
## * все справа обязательно уточнять при вызове. / - слева.

# после return ничего не выполняется

# данные возвращаемые из функции можно записать в переменную
# def message():
  # print("Hello")
# message = get_message()














