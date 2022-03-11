
import os
from hep_analysis.settings import BASE_DIR

from data.data_loading import (
    length_files,
    data_one_gen,
)
import json
def pdata_load():
    with open(os.path.join(BASE_DIR, 'citations.json')) as f:
        return json.load(f)

# pdata = pdata_load()

# print(len(pdata))

paper_ids = []

def pids_add(onedata):
    
    for item in onedata:
        pid = item["id"]
        paper_ids.append(pid)
    
def pids_gen():

    for n in range(length_files):
        pids_add(data_one_gen(n))
        

pids_gen()
print(len(set(paper_ids)))
   