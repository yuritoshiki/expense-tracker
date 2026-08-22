from pathlib import Path

import pandas

def load_csv(file_path : Path) -> pandas.DataFrame:
    return pandas.read_csv(file_path)