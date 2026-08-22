def get_data_information() -> tuple[str, int, int]:
    while True:
        card_company = input("カード会社(rakuten,smbc)：")
        if (card_company != "rakuten" and card_company != "smbc"):
            print("カード会社名の入力値が不正です。")
            continue
        break

    while True:
        try:  
            year = int(input("年(2026)："))
        except ValueError:
            print("整数以外が入力されました。")
            continue
        else:
            if (year <= 1999 or 2200 <= year):
                print("入力値が不正です。2000~2199の数字を入力してください。")
                continue
            break

    while True:
        try:
            month = int(input("月(08)："))
        except ValueError:
            print("整数以外が入力されました。")
            continue
        else:
            if (month < 1 or 12 < month):
                print("入力値が不正です。1~12の数字を入力してください。")
                continue
            break

    return card_company, year, month

    

