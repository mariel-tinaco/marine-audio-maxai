from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ID = 'audio'
DB_PATH = f'db/{ID}.sqlite'

# connect with database
engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)

# manage tables
base = declarative_base()

class audioclips (base):

    __tablename__ = "audioclips"

    audioclip_id = Column(Integer, primary_key = True)
    filename = Column(String)
    isLabeled = Column(Boolean)
    start_time = Column(Float)
    end_time = Column(Float)
    min_frequency = Column(Float)
    max_frequency = Column(Float)
    description = Column(String)

    def __init__ (self, *args, **kwargs):
        self.audioclip_id = kwargs['audioclip_id']
        self.filename = kwargs['filename']
        self.isLabeled = kwargs['isLabeled']
        self.start_time = kwargs['start_time']
        self.end_time = kwargs['end_time']
        self.min_frequency = kwargs['min_frequency']
        self.max_frequency = kwargs['max_frequency']
        self.description = kwargs['description']

base.metadata.create_all(engine)