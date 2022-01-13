# Using ORM commands: 
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

from main import (
    Job_table,
    Field_table,
    Rank_table,
    JobFileds_table,
    University_table,
    Country_table
)

engine = create_engine(DB_CONNECTION_STRING, echo=True, future = True)

conn = engine.connect() 

meta_HEP = MetaData()


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

