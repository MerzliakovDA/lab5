def find_min_max(a, b, c):
  
  min_val = a
  if b < min_val:
    min_val = b
  if c < min_val:
    min_val = c

  max_val = a
  if b > max_val:
    max_val = b
  if c > max_val:
    max_val = c

  return min_val, max_val


if __name__ == "__main__":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))

        min_number, max_number = find_min_max(num1, num2, num3)

        print(f"Наименьшее число: {min_number}")
        print(f"Наибольшее число: {max_number}")
    except ValueError:
        print("Ошибка: Введите корректные числа.")

