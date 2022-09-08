word_list =[]
index_list = []
amount_change = 0
text = input("Введите строку: ")
word_list = list(text)
for index, sym in enumerate(word_list):
    if sym == ":" :
        word_list[index] = ";"
        amount_change += 1

print("Исправленная строка:", end=" ")
for sym in word_list:
    print(sym, end="")

print("\nКол-во замен:", amount_change)