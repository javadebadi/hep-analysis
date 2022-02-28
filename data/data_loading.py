from pathlib import Path
import json
import os
from glob import glob, iglob


BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
literuture_path = os.path.join(BASE_BASE_DIR, "literature")

litfiles_list = [i for i in Path(literuture_path).iterdir() if not i.name.startswith(".")]



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
    filenames_i = glob(os.path.join(literuture_path,"*.json"))
    for batch in every(filenames_i, Batch_size):
        data_Path_list.append(batch)
    return data_Path_list

        
      
def data_batch_gen(n,Batch_size = 6):
    if 0 <= n <= round(len(litfiles_list)/Batch_size) and Batch_size <=len(litfiles_list):
        data_literature_list = []
        print(f"this is the {n}th batch")
        for file in data_literature_list_func(Batch_size)[n]:
            with open(file) as f:
                data_literature_list.append(json.load(f))
        return data_literature_list 
