import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Engine
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

class Migrate:
    def __init__(self) -> None:
        self.metadata_obj = MetaData()
        self.Base = declarative_base(metadata=self.metadata_obj)

        self.engine = self.connect()

        Session = sessionmaker(bind=self.engine)

        self.session = Session()
    
    def connect(self) -> Engine:
        USERNAME = os.getenv('USERNAME_DATABASE')
        PASSWORD = os.getenv('PASSWORD_DATABASE')
        HOST = os.getenv('HOST_DATABASE')
        PORT = os.getenv('PORT_DATABASE')
        DATABASE = os.getenv('DATABASE')

        URL = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

        engine = create_engine(URL)

        if not database_exists(engine.url):
            create_database(engine.url)

        return engine

    def create_table(self) -> None:
        self.Base.metadata.create_all(self.engine)

    def drop_table(self) -> None:
        self.Base.metadata.drop_all(self.engine)