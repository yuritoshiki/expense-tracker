from pathlib import Path

def input_file_path() -> Path:
    while True:
        file_path = Path(input("CSVファイルのパスを入力してください："))

        if file_path.is_file():
            print("ファイルが見つかりませんでした。")
            continue

        if file_path.suffix.lower() != ".csv":
            print("指定されたファイルがCSVファイルではありませんでした。")
            continue

        return file_path