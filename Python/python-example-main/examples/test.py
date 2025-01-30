import time

n = int(input("Введите число для обратного отсчёта: "))
print("Стартуем через: ")
while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)
    if(n == 0):
        print('Старт')
        break
