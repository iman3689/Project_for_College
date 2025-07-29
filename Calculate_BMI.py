def Calculate_BMI():
    print("BMI 計算器🙋‍♂️")
    # 定義
    height_cm = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入您的體重(公斤):"))

    # 換算
    height_m = height_cm / 100
    BMI = weight / (height_m ** 2)
    print(f"您的 BMI 為:{BMI:.2f}")

    if BMI < 18.5:
        print("🟡您體重過輕喔，記得多吃點🍙")
    elif 18.5 <= BMI < 24:
        print("🟢標準體重，繼續保持！")
    elif 24 <= BMI < 27:
        print("🟠有一點點超出標準啦，小控制就完美啦😳")
    elif 27 <= BMI < 30:
        print("🟠好像超出標準啦，最近要不要試試看211餐盤呢😊")
    elif 30 <= BMI < 35:
        print("🔴為了您的健康著想，要控制飲食啦😲")
    elif BMI > 35:
        print("⛔要努力控制飲食加上運動輔助啦，我們一起加油😰")

Calculate_BMI()