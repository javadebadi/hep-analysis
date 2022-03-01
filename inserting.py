from sqlalchemy import (
     insert
)
from math import ceil

from data.data_loading import (
    data_batch_gen,
    litfiles_list
)
from tables import (
    engine,
    Authors_Papers_table_new
)


def inserting_ap(paperid, authorheplist):
    with engine.connect() as conn:
        for hepauthor in authorheplist:
            query = insert(Authors_Papers_table_new).values(paper_id= paperid, author_id=hepauthor)
            result = conn.execute(query)
        return conn.commit()

def data_inserting(data_literature_list):
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
            except KeyError:
                print(f"there is no authors data for {item['id']}")
            except ValueError as e:
                if str(e) == "'INSPIRE BAI' is not in list":
                    print("We do not have INSPIRE BAI for this record!")
                else:
                    print(f"we have problem {str(e)}")


B_size = 6
for n in range(ceil(len(litfiles_list)/B_size)):
    data_inserting(data_batch_gen(n,B_size))
    





