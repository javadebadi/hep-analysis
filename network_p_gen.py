import networkx as nx
import os
from hep_analysis.settings import BASE_DIR

import json

PaperGraph = nx.DiGraph()

def pdata_load():
    with open(os.path.join(BASE_DIR, 'citations.json')) as f:
        return json.load(f)
        

def pnet_gen():
    pdata = pdata_load()
    x = 0 
    for pkey in pdata:
        x += 1
        print(f"record {x}")
        citelist = pdata[pkey]
        if len(citelist) == 0:
            PaperGraph.add_node(pkey)
        else:
            for cite in citelist:
                PaperGraph.add_edge(cite, pkey)
               
    

def net_save(name, suffix):
    OUT_GRAPH_PATH =  os.path.join(BASE_DIR, f"{name}.{suffix}")
    nx.write_graphml(PaperGraph,OUT_GRAPH_PATH)
    print(f"Directed network of papers with {PaperGraph.number_of_edges()} edges and {PaperGraph.number_of_nodes()} nodes is created") 

if __name__ == "__main__":
    pnet_gen()
    net_save("pgraph", "graphml")
