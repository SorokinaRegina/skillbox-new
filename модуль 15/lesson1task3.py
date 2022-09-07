employees_ID = []
amount_employees = int(input("Кол-во сотрудников в офисе: "))

for _ in range(amount_employees):
    new_ID = int(input("ID сотрудника: "))
    employees_ID.append(new_ID)

search_ID = int(input("Какой ID ищем? "))
if search_ID in employees_ID:
    print("Сотрудник на месте")
else:
    print("Сотрудник не работает!")
