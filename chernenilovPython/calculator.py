result = 0
a = 0
b = 0


def plus(a, b):
  result = a + b
  print(f"Результат:\n{result}")
  return result
def minus(a, b):
  result = a - b
  print(f"Результат:\n{result}")
  return result
def multiply(a, b):
  result = a * b
  print(f"Результат:\n{result}")
  return result
def divide(a, b):
  result = a / b
  print(f"Результат:\n{result}")
  return result


try:
  a = float(input("Число 1:\n"))
  sign = input("Знак операции:\n")
  b = float(input("Число 2:\n"))
except ValueError:
  print("Ошибка ввода.")
else:
  match sign:
    case "+":
      result = plus(a, b)
    case "-":
      result = minus(a, b)
    case "*":
      result = multiply(a, b)
    case "/":
      result = divide(a, b)
    case _:
      print("Ошибка. Некорректный знак операции.")

def nextNum(result):
  a = result
  try:
    sign = input("Знак операции:\n")
    b = float(input("Число 2:\n"))
    
  except ValueError:
    print("Ошибка ввода.")
  else:
    match sign:
      case "+":
        result = plus(a, b)
      case "-":
        result = minus(a, b)
      case "*":
        result = multiply(a, b)
      case "/":
        result = divide(a, b)
      case _:
        print("Ошибка. Некорректный знак операции.")
    return result






