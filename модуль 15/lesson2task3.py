N = int(input("Введите колличество собак: "))
dogs_points = []

for i in range(N):
    print("Кол-во очков", i + 1, "собаки:", end = " ")
    points = int(input())
    dogs_points.append(points)

if dogs_points:
    maximum = dogs_points[0]
    minimum = dogs_points[0]

    maximum_index = 0
    minimum_index = 0

    for index, i in enumerate(dogs_points):
        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    dogs_points[maximum_index], dogs_points[minimum_index] = dogs_points[minimum_index], dogs_points[maximum_index]
    print("Список очков:", dogs_points)
else:
    print("В списке нет чисел")
