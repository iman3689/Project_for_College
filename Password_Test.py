def Password_Strength():
    print("🔐密碼強度檢查")
    password = input("請輸入您的密碼:")

    allowed_symbols = "!@#$%^&*"
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in allowed_symbols for char in password)
    has_invalid_symbol = any(
        not char.isalnum() and char not in allowed_symbols
        for char in password
    )

    if all([length_ok, has_upper, has_lower, has_digit,  has_symbol]):
        print("✅密碼強度：強")
    else:
        print("⚠️密碼強度：弱，建議包含以下內容：")
        if not length_ok:
            print("至少 8 個字元")
        if not has_upper:
            print("至少一個大寫字母")
        if not has_lower:
            print("至少一個小寫字母")
        if not has_digit:
            print("至少一個數字")
        if not has_symbol:
            print("至少一個符號(!@#$%^&*)")
        if has_invalid_symbol:
            print("符號只能用：!@#$%^&*")

Password_Strength()