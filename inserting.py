from sqlalchemy import (
     insert
)
from math import ceil

from data.data_loading import (
    data_batch_gen,
    litfiles_list,
    data_Path_list,
    literuture_path,
    batch_size,
    data_one_gen,
    #folder_list,
    #data_batch_gen_wpath
)
from tables import (
    engine,
    Authors_Papers_table_new
)

from networkx_authors import (
    ContributionGraph,
    net_save,
    edge_gen,
)

from itertools import combinations

from control import st_time

from threading import Thread

def inserting_ap(paperid, authorheplist):
    with engine.connect() as conn:
        for hepauthor in authorheplist:
            query = insert(Authors_Papers_table_new).values(paper_id= paperid, author_id=hepauthor)
            result = conn.execute(query)
        return conn.commit()

def data_inserting(data_literature_list):
    number_of_data_wout_author = 0
    number_of_data_wout_InspireID = 0
    for data_literature in data_literature_list:
        for item in data_literature:
            # pid = item["id"]
            try:
                alist = item["metadata"]["authors"]
                author_list = []
                for author in alist:
                    ids_list = author["ids"]
                    id_index = list(map(lambda x: x["schema"],ids_list)).index('INSPIRE BAI')
                    adata = ids_list[id_index]["value"]
                    author_list.append(adata)
                


                edge_gen(author_list)
                #inserting_ap(pid,author_list)
            except KeyError:
                number_of_data_wout_author += 1
                #print(f"there is no authors data for {item['id']}")

            except ValueError as e:
                if str(e) == "'INSPIRE BAI' is not in list":
                    number_of_data_wout_InspireID += 1
                    #print("We do not have INSPIRE BAI for this record!")
                else:
                    print(f"we have problem {str(e)}")
    print(f"We had {number_of_data_wout_author} data without author!")
    print(f"We had {number_of_data_wout_InspireID} data without InspireHepID!") 

def data_inserting_one(onedata):
    number_of_data_wout_author = 0
    number_of_data_wout_InspireID = 0

    for item in onedata:
        # pid = item["id"]
        try:
            alist = item["metadata"]["authors"]
            author_list = []
            for author in alist:
                ids_list = author["ids"]
                id_index = list(map(lambda x: x["schema"],ids_list)).index('INSPIRE BAI')
                adata = ids_list[id_index]["value"]
                author_list.append(adata)
            


            edge_gen(author_list)
            #inserting_ap(pid,author_list)
        except KeyError:
            number_of_data_wout_author += 1
            #print(f"there is no authors data for {item['id']}")

        except ValueError as e:
            if str(e) == "'INSPIRE BAI' is not in list":
                number_of_data_wout_InspireID += 1
                #print("We do not have INSPIRE BAI for this record!")
            else:
                print(f"we have problem {str(e)}")
    print(f"We had {number_of_data_wout_author} data without author!")
    print(f"We had {number_of_data_wout_InspireID} data without InspireHepID!")

@st_time
def NetConstruct():
    for n in range(ceil(len(litfiles_list)/batch_size)):
        data_inserting(data_batch_gen(n))
    #net_save("Contributaion_graph","graphml")
    
  
@st_time
def NetConstruct_one_one():
    for n in range(ceil(len(litfiles_list))):
        data_inserting_one(data_one_gen(n))
    net_save("Contributaion_graph","graphml")


NetConstruct()


# @st_time
# def NetConstruct_folder():
#     for path in folder_list:
#         for n in range(ceil(len(litfiles_list(path))/batch_size)):
#             data_inserting(data_batch_gen_wpath(n, path))
#     net_save("Contributaion_graph","graphml")
    
# NetConstruct_folder()

# thread1 = Thread(target=NetConstruct)
# thread2 = Thread(target=net_save, args=("Contributaion_graph","graphml"))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()






   