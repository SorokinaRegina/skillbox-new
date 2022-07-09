def user_menu():
    X = input("\nВведите операцию: ")
    if X == "+" or X == "-" or X == "*" or X == "/":
        A = float(input("Введите первое число: "))
        B = float(input("Введите второе число: "))
        if X == "+":
            C = A + B
        elif X == "-":
            C = A - B
        elif X == "*":
            C = A * B
        elif X == "/":
            C = A / B
        print(A, X, B, "=", C)
    else:
        print("Ошибка: такой операции не существует.")
        print("Попробуйте еще раз.")
        user_menu()
        

user_menu()