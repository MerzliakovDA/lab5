def decompose_number(n):

    k = n // 7  # Целая часть от деления на 7
    r = n % 7   # Остаток от деления на 7

    if r == 0:
        print(f"{n} = 7 * {k}")
    else:
        print(f"{n} = 7 * {k} + {r}")


if __name__ == "__main__":
    try:
        n = int(input("Введите натуральное число: "))
        if n <= 0:
            print("Пожалуйста, введите натуральное число (больше 0).")
        else:
            decompose_number(n)
    except ValueError:
        print("Ошибка: Введите целое число.")

