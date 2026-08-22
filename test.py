from pathlib import Path

from src.input.cui_filepath import input_file_path
from src.input.csv_loader import load_csv

file_path = Path(input("CSVファイルのパスを入力してください: ").strip().strip('"'))

print(f"Path: [{file_path}]")
print(f"Exists: {file_path.exists()}")
print(f"Is file: {file_path.is_file()}")
print(f"Suffix: [{file_path.suffix}]")