from sqlalchemy import (
    text
)

from tables import engine


v_query_new="CREATE VIEW v_collaboration_new AS \
    SELECT f.author_id as author1, g.author_id as author2, f.paper_id \
    FROM Authors_Papers_new as f JOIN Authors_Papers_new as g \
    ON f.paper_id = g.paper_id WHERE f.author_id != g.author_id"

v_query_new_withoutpapr="CREATE VIEW v_collaboration_new_WP AS \
    SELECT f.author_id as author1, g.author_id as author2 \
    FROM Authors_Papers_new as f JOIN Authors_Papers_new as g \
    ON f.paper_id = g.paper_id WHERE f.author_id != g.author_id"


with engine.connect() as conn:
    result = conn.execute(text(v_query_new_withoutpapr))


