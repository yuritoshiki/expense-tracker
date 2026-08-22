import pandas

# 取得したデータの中から次のデータを取り出して共通化を行う。
# 利用日、店名、利用金額、支払金額

def convert_rakuten(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    converted_data_frame = data_frame[
        [
            "利用日",
            "利用店名・商品名",
            "利用金額",
            "支払総額",
        ]
    ].copy()

    converted_data_frame = converted_data_frame.rename(
        columns={
            "利用店名・商品名": "店名",
            "支払総額": "支払金額",
        }
    )

    converted_data_frame["利用日"] = pandas.to_datetime(
        converted_data_frame["利用日"]
    )

    return converted_data_frame

def convert_smbc(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    converted_data_frame = data_frame.iloc[1:].copy()

    converted_data_frame.columns = [
        "利用日",
        "店名",
        "利用金額",
        "支払い区分",
        "今回回数",
        "支払金額",
    ]

    converted_data_frame = converted_data_frame[
        [
            "利用日",
            "店名",
            "利用金額",
            "支払金額",
        ]
    ]

    converted_data_frame["利用日"] = pandas.to_datetime(
        converted_data_frame["利用日"]
    )

    return converted_data_frame
