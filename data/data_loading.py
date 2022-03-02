from pathlib import Path
import json
import os
from glob import glob, iglob


BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
literuture_path = os.path.join(BASE_BASE_DIR, "literature")
# folder_list = [i for i in Path(literuture_path).iterdir() if i.is_dir()]

litfiles_list = [i for i in Path(literuture_path).iterdir() if not i.name.startswith(".")]
# def litfiles_list(path):
#      return [i for i in Path(path).iterdir() if not i.name.startswith(".")]


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

# def data_literature_list_func(Batch_size,path):
#     data_Path_list = []
#     filenames_i = glob(os.path.join(path,"*.json"))
#     for batch in every(filenames_i, Batch_size):
#         data_Path_list.append(batch)
#     return data_Path_list

batch_size = 5
data_Path_list = data_literature_list_func(batch_size) 

def data_batch_gen(n):
    if 0 <= n <= round(len(litfiles_list)/batch_size) and batch_size <=len(litfiles_list):
        
        data_literature_list = []
        print(f"this is the {n+1}th batch")
        for file in data_Path_list[n]:
            with open(file) as f:
                data_literature_list.append(json.load(f))
        return data_literature_list 

# def data_batch_gen_wpath(n, path):
#     if 0 <= n <= round(len(litfiles_list(path))/batch_size) and batch_size <=len(litfiles_list(path)):
        
#         data_literature_list = []
#         print(f"this is the {n+1}th batch for {path}")
#         for file in data_literature_list_func(batch_size, path)[n]:
#             with open(file) as f:
#                 data_literature_list.append(json.load(f))
#         return data_literature_list 

def data_one_gen(n):
    if 0 <= n <= len(litfiles_list):

        print(f"this is the {n+1}th file")
        with open(litfiles_list[n]) as f:
            return json.load(f)

