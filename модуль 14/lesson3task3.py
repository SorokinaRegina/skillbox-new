def user_menu():
    result = 0
    conclusion = " "
    X = input("\nВведите операцию: ")
    if X == "+" or X == "-" or X == "*" or X == "/":
        numbers = int(input("Сколько операндов? "))
        num1 = int(input("Введите операнд 1: "))
        result = num1
        conclusion = str(num1)
        for count in range(2, numbers + 1):
            num = int(input(f"Введите операнд {count}: "))
            if X == "+":
              result += num 
              conclusion += " + "
              conclusion += str(num)
            elif X == "-":
              result -= num
              conclusion += " - "
              conclusion += str(num)
            elif X == "*":
              result *= num
              conclusion += " * "
              conclusion += str(num)
            elif X == "/":
              result /= num
              conclusion += " / "
              conclusion += str(num)
        print(conclusion, "=", result)    
    else:
        print("Ошибка: такой операции не существует.")
        print("Попробуйте еще раз.")
        user_menu()


user_menu()