from pathlib import Path
import json
import os

BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
files_path = os.path.join(BASE_BASE_DIR, "literaturetest")

files_path_list = sorted([i for i in Path(files_path).iterdir() if not i.name.startswith(".")], key=os.path.getmtime)
length_files = len(files_path_list)

def data_one_gen(n):
    if 0 <= n <= length_files:

        print(f"this is the {n+1}th file")
        with open(files_path_list[n]) as f:
            return json.load(f)

