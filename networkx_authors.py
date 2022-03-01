import networkx as nx
from pathlib import Path
import os
from hep_analysis.settings import BASE_DIR


print(BASE_DIR)
from sqlalchemy import (
    text,
    select
)

from tables import engine


with engine.connect() as conn:
    limit = 100
    query = f"SELECT * FROM v_collaboration_new_WP LIMIT {limit}"
    result = conn.execute(text(query)).fetchall()


ContributionGraph = nx.Graph()

for item in result:
    ContributionGraph.add_edge(*item)

print(ContributionGraph.number_of_edges())
print(ContributionGraph.number_of_nodes())

OUT_GRAPH_PATH =  os.path.join(BASE_DIR, 'test.graphml')

nx.write_graphml(ContributionGraph,OUT_GRAPH_PATH) 



