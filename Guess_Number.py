import random

# 定義 + 函式
def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0 # 猜幾次

    print("🎯猜數字遊戲！（1~100）")
    while True:
        guess = int(input("請輸入您猜的數字："))
        attempts += 1

        if guess < number:
            print(f"比{guess}大！")
        elif guess > number:
            print(f"比{guess}小！")
        else:
            print(f"恭喜你猜對了！答案是 {number}，共猜了 {attempts} 次。")
            break

guess_the_number()
