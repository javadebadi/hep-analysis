from pathlib import Path
import json
import os
from glob import glob


BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
files_path = os.path.join(BASE_BASE_DIR, "literature")

files_path_list = sorted([i for i in Path(files_path).iterdir() if not i.name.startswith(".")], key=os.path.getmtime)

def every(thing, n):                                     
    toexit = False
    it = iter(thing)
    while not toexit:
        batch = []
        for i in range(n):
            try:
                batch.append(next(it))
            except StopIteration:
                toexit = True
        if not batch:
            break
        yield batch

def data_literature_list_func(Batch_size):
    data_Path_list = []
    filenames_i = sorted(glob(os.path.join(files_path,"*.json")), key=os.path.getmtime)
    for batch in every(filenames_i, Batch_size):
        data_Path_list.append(batch)
    return data_Path_list

batch_size = 5
data_Path_list = data_literature_list_func(batch_size) 


def data_batch_gen(n):
    length_files = len(files_path_list)
    if 0 <= n <= round(length_files/batch_size) and batch_size <=length_files:
        
        data_literature_list = []
        print(f"this is the {n+1}th batch")
        for file in data_Path_list[n]:
            with open(file) as f:
                data_literature_list.append(json.load(f))
        return data_literature_list 