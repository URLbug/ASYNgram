import os
import __init__

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

class Migrate:
    def __init__(self) -> None:
        self.metadata_obj = MetaData()
        self.Base = declarative_base(metadata=self.metadata_obj)

        self.engine = self.connect()

        Session = sessionmaker(bind=self.engine)

        self.session = Session()
    
    def connect(self) -> Engine:
        TYPE = os.getenv('TYPE_DATABASE')
        USERNAME = os.getenv('USERNAME_DATABASE')
        PASSWORD = os.getenv('PASSWORD_DATABASE')
        HOST = os.getenv('HOST_DATABASE')
        PORT = os.getenv('PORT_DATABASE')
        DATABASE = os.getenv('DATABASE')

        if TYPE == 'pgsql':
            URL = f'postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
        else:
            URL = f'mysql+aiomysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

        engine = create_async_engine(URL)

        return engine

    async def create_table(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)
        
        print('Tables create!')

    async def drop_table(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.drop_all)
        
        print('Tables drop!')
