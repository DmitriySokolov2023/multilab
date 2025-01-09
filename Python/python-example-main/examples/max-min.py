

    


# Создали
arr = [1, 3, 55, 7, 9]

#Присваиваем переменные первому элементу массива
max_element = arr[0]
min_element = arr[0]

#Проходимся по всем элементам массива и сравниваем/присваиваем   
for value in arr:
  if value > max_element:
    max_element = value
  if value < min_element:
    min_element = value


print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)


## Альтернатива))
max_val = max(arr)
min_val = min(arr)