from data.data_loading import (
    length_files,
    data_one_gen,
)

import json 
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


from control import st_time

cite_dict = {}

def citation_add(onedata):
    n_paper = 0
    for item in onedata:
        n_paper += 1
        pid = item["id"]
        cite_dict[pid] = []
        reflist = item["metadata"]["references_ids"]
        for ref in reflist: 
            if ref in cite_dict:
                cite_dict[ref].append(pid) 
            else:
                cite_dict[ref] = [pid]

    return n_paper


@st_time
def cite_gen():

    total_paper = 0 
    for n in range(length_files):
        np = citation_add(data_one_gen(n))
        total_paper += np
    print(f"we had total {total_paper} paper")
    




if __name__ == "__main__":
    cite_gen()
    with open(os.path.join(BASE_DIR, 'citations.json'), 'w') as f:
        json.dump(cite_dict, f)

