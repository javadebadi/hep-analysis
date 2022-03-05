from sqlalchemy import (
     insert
)
from math import ceil

from data.data_loading import (
    length_files,
    data_one_gen,
)

from data.data_batch_loading import (
    batch_size,
    data_batch_gen,
)

from tables import (
    engine,
    Authors_Papers_table_new
)


from control import st_time

def inserting_ap(paperid, authorheplist):
    with engine.connect() as conn:
        for hepauthor in authorheplist:
            query = insert(Authors_Papers_table_new).values(paper_id= paperid, author_id=hepauthor)
            result = conn.execute(query)
        return conn.commit()

def data_inserting(data_literature_list):
    number_of_data_wout_author = 0
    number_of_data_wout_InspireID = 0
    number_of_data_wout_a_ids = 0

    for data_literature in data_literature_list:
        for item in data_literature:
            pid = item["id"]
            try:
                alist = item["metadata"]["authors"]
                author_list = []
                for author in alist:
                    ids_list = author["ids"]
                    id_index = list(map(lambda x: x["schema"],ids_list)).index('INSPIRE BAI')
                    adata = ids_list[id_index]["value"]
                    author_list.append(adata)
                


           
                inserting_ap(pid,author_list)
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

def data_inserting_one(onedata, up_limit_authors = 5):
    number_of_data_wout_author = 0
    number_of_data_wout_InspireID = 0
    number_of_data_wout_a_ids = 0
    

    for item in onedata:
        pid = item["id"]
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
            
            inserting_ap(pid,author_list)
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

@st_time
def inserting_batch():
    for n in range(ceil(length_files/batch_size)):
        data_inserting(data_batch_gen(n))
    
  
@st_time
def inserting_one():
    for n in range(length_files):
        data_inserting_one(data_one_gen(n))


if __name__ == "__main__":
    inserting_one()
    
     












   