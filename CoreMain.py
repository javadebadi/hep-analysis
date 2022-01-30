from sqlalchemy import (
    create_engine, 
    text, 
    Table, 
    Column, 
    Integer, 
    String, 
    MetaData,
    ForeignKey,
    insert, 
    select
)
from sqlalchemy.orm import (
    declarative_base, 
    relationship
)

from hep_analysis.settings import (
    DB_CONNECTION_STRING
)
import json

engine = create_engine(DB_CONNECTION_STRING, echo=True, future = True)

conn = engine.connect() 

meta_HEP = MetaData()

#Creatinf Tables using Core commands: 
Job_table = Table(
        "Jobs",
    meta_HEP,
    Column('job_id', Integer, primary_key=True),
    Column('Job_title', String(30)),
    Column('university_id', ForeignKey('University.university_id'), nullable=False),
    Column('region_id', ForeignKey('Country.region_id'), nullable=False),
    Column('rank_id', ForeignKey('Rank.rank_id'), nullable=False),
    )


Field_table = Table(
        "Fields",
    meta_HEP,
    Column('field_id', Integer, primary_key=True),
    Column('field_title', String(30)),
    )


University_table = Table(
        "University",
    meta_HEP,
    Column('university_id', Integer, primary_key=True),
    Column('university_title', String(30)),
    Column('address', String(100)),
    Column('country_id', ForeignKey('Country.country_id'), nullable=False),
    Column('region_id', ForeignKey('Country.region_id'), nullable=False),
    )

Rank_table=Table(
        "Rank",
    meta_HEP,
    Column('rank_id', Integer, primary_key=True),
    Column('rank_title', String(30),nullable=False),
    )

Country_table = Table(
        "Country",
    meta_HEP,
    Column('country_id', Integer, primary_key=True),
    Column('country_title', String(30),nullable=False),
    Column('region_id', Integer, nullable=False),
    Column('region_title', String(30), nullable=False),
    )

JobFileds_table = Table(
        "Job_Fileds",
    meta_HEP,
    Column('job_id', ForeignKey('Jobs.job_id'), primary_key=True),
    Column('field_id', ForeignKey('Fields.field_id'), primary_key=True),
)

Authors_table = Table(
        "Authors",
    meta_HEP,
    Column('Author_id', Integer, primary_key=True),
    Column('Author_name',String(30)),
)

with open('authors.json') as f:
    data = json.load(f)



# it is already created. 


if __name__ == '__main__':
    meta_HEP.create_all(engine)
    with engine.connect() as conn:
        for A_id in data:
            query = insert(Authors_table).values(Author_id= A_id, Author_name= data[A_id]['name']['value'])
            result = conn.execute(query)
        conn.commit()