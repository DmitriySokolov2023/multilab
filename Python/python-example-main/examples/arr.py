arr = [10, 20, 30, 40, 50]
print(arr.count)
target = 50
count = 0

for i, value in enumerate(arr):
    if value == target:
        count = count + 1 
        print('Элемент', target,'имеет индекс:', i)  
    if i == len(arr) - 1 and count == 0:
        print('Элемент не найден!')