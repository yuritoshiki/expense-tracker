from src.io.cui_filepath import input_file_path
from src.io.csv_loader import load_csv

file_path = input_file_path()
data = load_csv(file_path)

print(data)