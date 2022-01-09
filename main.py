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

from setting import (
    DB_CONNECTION_STRING
)

engine = create_engine(DB_CONNECTION_STRING, echo=True)

conn = engine.connect() 

meta_HEP = MetaData()

#Creatinf Tables using Core commands: 
Job_table = Table(
        "Jobs",
    meta_HEP,
    Column('job_id', Integer, primary_key=True),
    Column('Job_title', String(30)),
    Column('university_id', ForeignKey('University_table.univarsity_id'), nullable=False),
    Column('region_id', ForeignKey('Country_table.region_id'), nullable=False),
    Column('rank_id', ForeignKey('Rank_table.rank_id'), nullable=False),
    )


Field_table = Table(
        "Fields",
    meta_HEP,
    Column('field_id', Integer, primary_key=True),
    Column('field_title', String(30))
    )


University_table = Table(
        "University",
    meta_HEP,
    Column('university_id', Integer, primary_key=True),
    Column('university_title', String(30)),
    Column('address', String(100)),
    Column('country_id', ForeignKey('Country_table.country_id'), nullable=False),
    Column('region_id', ForeignKey('Country_table.region_id'), nullable=False)
    )

Rank_table=Table(
        "Rank",
    meta_HEP,
    Column('rank_id', Integer, primary_key=True),
    Column('rank_title', String(30),nullable=False)
    )

Country_table = Table(
        "Country",
    meta_HEP,
    Column('country_id', Integer, primary_key=True),
    Column('country_title', String(30),nullable=False),
    Column('region_id', Integer, nullable=False),
    Column('region_title', String(30), nullable=False)
    )

JobFileds_table = Table(
        "Job_Fileds",
    meta_HEP,
    Column('job_id', ForeignKey('Job_table.job_id'), primary_key=True),
    Column('field_id', ForeignKey('Field_table.field_id'), primary_key=True)
)



# Using ORM commands: 
Base = declarative_base()

class Jobs(Base):
    __table__ = Job_table
    
    field = relationship("Fields", secondary = JobFileds_table, back_populates="job")
    university = relationship("University", back_populates="job")
    rank = relationship("University", back_populates="job")
    region = relationship("Country", back_populates="job")
    
    def __repr__(self):
        return f"Jobs({self.jobs_title!r}, {self.fullname!r})"


class Fields(Base):
    __table__ = Field_table

    job = relationship("Jobs", secondary=JobFileds_table, back_populates="field")

    def __repr__(self):
         return f"Fields({self.field_title!r})"


class University(Base):
    __table__ = University_table

    job = relationship("Jobs", back_populates="university")

    def __repr__(self):
        return f"Jobs({self.jobs_title!r}, {self.fullname!r})"

class Country(Base):
    __table__ = Country_table

    def __repr__(self):
        return f"Jobs({self.jobs_title!r}, {self.fullname!r})"

class Rank(Base):
    __table__ = Rank_table
    
    job = relationship("Jobs", back_populates="rank")

    def __repr__(self):
        return f"Jobs({self.jobs_title!r}, {self.fullname!r})"

class JobFileds(Base):
    __table__ = JobFileds_table

    def __repr__(self):
         return f"Fields({self.field_title!r})"




if __name__ == '__mane__':
    Base.metadata.create_all(engine)