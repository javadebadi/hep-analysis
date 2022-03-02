import networkx as nx
from pathlib import Path
import os
from hep_analysis.settings import BASE_DIR
from itertools import combinations

print(BASE_DIR)
from sqlalchemy import (
    text,
    select
)

# from tables import engine


# with engine.connect() as conn:
#     limit = 10
#     query = f"SELECT * FROM v_collaboration_new_WP LIMIT {limit}"
#     result = conn.execute(text(query)).fetchone()

# print(result)

ContributionGraph = nx.Graph()

def edge_gen(a_list):
    for item in combinations(a_list, 2):
        if ContributionGraph.has_edge(*item):
            ContributionGraph[item[0]][item[1]]['weight'] += 1
        else:
            ContributionGraph.add_edge(*item, weight = 1)

    # print(ContributionGraph.number_of_edges())
    # print(ContributionGraph.number_of_nodes())

    
def net_save(name, suffix):
    OUT_GRAPH_PATH =  os.path.join(BASE_DIR, f"{name}.{suffix}")
    nx.write_graphml(ContributionGraph,OUT_GRAPH_PATH)
    print(f"Network with {ContributionGraph.number_of_edges()} edges and {ContributionGraph.number_of_nodes()} nodes is created") 



    








