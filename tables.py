from sqlalchemy import (
    create_engine, 
    Table, 
    Column, 
    Integer, 
    String, 
    MetaData,
    ForeignKey
)


from hep_analysis.settings import (
    DB_CONNECTION_STRING
)


engine = create_engine(DB_CONNECTION_STRING, echo=False, future=True)

meta_HEP = MetaData()


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

Papers_table = Table(
        "Papers",
    meta_HEP,
    Column('Paper_id', Integer, primary_key=True),
    Column('Paper_title',String),
)

Authors_Papers_table = Table(
        "Authors_Papers",
    meta_HEP,
    Column('author_id', ForeignKey('Authors.Author_id'), primary_key=True),
    Column('paper_id', ForeignKey('Papers.Paper_id'), primary_key=True),
)


Authors_Papers_table_new = Table(
        "Authors_Papers_new",
    meta_HEP,
    Column('author_id', String(50), nullable=True),
    Column('paper_id', String(10), nullable=False),
)


if __name__ == '__main__':
    meta_HEP.create_all(engine)
    