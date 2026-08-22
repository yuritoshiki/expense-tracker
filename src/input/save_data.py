from pathlib import Path
import pandas


def save_data(data_frame: pandas.DataFrame, file_path: Path):
    data_frame.to_csv(file_path, index=False)