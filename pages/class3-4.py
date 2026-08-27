import random

target = random.randint(1, 100)
low, high = 1, 100

while True:
    num = int(input(f"請輸入 {low} 到 {high} 的整數："))

    if num == target:
        print("猜中了！")
        break
    elif num < target:
        print("太小了！")
        low = num 
    else:
        print("太大了！")
        high = num 
    