N = int(input("Кол-во чисел в списке: "))
numbers = []

for i in range(N):
    print("Введите", i + 1, "число: ", end = " ")
    num = int(input())
    numbers.append(num)
print()
print()

K = int(input("Введите делитель: "))
print()
print()

i_sum = 0
for i_number in range(N):
    if numbers[i_number] % K == 0:
        print("Индекс числа", numbers[i_number], ":", i_number)
        i_sum += i_number

print("Сумма индексов:", i_sum)