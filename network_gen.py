import networkx as nx
import os
from pathlib import Path
from hep_analysis.settings import BASE_DIR
from itertools import combinations
from data.data_loading import (
    length_files,
    data_one_gen
)


ContributionGraph = nx.Graph()

def edge_gen(a_list):
    for item in combinations(a_list, 2):
        if ContributionGraph.has_edge(*item): # maybe we should use multigraph
            ContributionGraph[item[0]][item[1]]['weight'] += 1
        else:
            ContributionGraph.add_edge(*item, weight = 1)


    
def net_save(name, suffix):
    OUT_GRAPH_PATH =  os.path.join(BASE_DIR, f"{name}.{suffix}")
    nx.write_graphml(ContributionGraph,OUT_GRAPH_PATH)
    print(f"Network with {ContributionGraph.number_of_edges()} edges and {ContributionGraph.number_of_nodes()} nodes is created") 


def data_inserting_one(onedata, up_limit_authors = 5):
    number_of_data_wout_author = 0
    number_of_data_wout_InspireID = 0
    number_of_data_wout_a_ids = 0

    for item in onedata:
        # pid = item["id"]
        try:
            alist = item["metadata"]["authors"]
            if len(alist) >= up_limit_authors:
                continue

            author_list = []
            for author in alist:
                ids_list = author["ids"]
                id_index = list(map(lambda x: x["schema"],ids_list)).index('INSPIRE BAI')
                adata = ids_list[id_index]["value"]
                author_list.append(adata)
            
            edge_gen(author_list)

        except KeyError as e:
            if str(e) == "'authors'":
                number_of_data_wout_author += 1
            elif str(e) == "'ids'":
                number_of_data_wout_a_ids += 1
            else:
                raise e

        except ValueError as e:
            if str(e) == "'INSPIRE BAI' is not in list":
                number_of_data_wout_InspireID += 1
            else:
                print(f"we have problem {str(e)}")        

    return number_of_data_wout_author, number_of_data_wout_a_ids, number_of_data_wout_InspireID


def net_construct():
    total_na = 0
    total_ni = 0
    total_niI =0 

    print(f"We have Network with {ContributionGraph.number_of_edges()} edges and {ContributionGraph.number_of_nodes()} nodes")
    for n in range(length_files):
        na, ni, niI = data_inserting_one(data_one_gen(n))
        total_na += na
        total_ni += ni
        total_niI += niI
    print(f"we had {total_na} record without author, {total_ni} without id and {total_niI} without InspirehepID!")
    
     
if __name__ == "__main__":
    net_construct()
    net_save("Contributaion_graph","graphml")






