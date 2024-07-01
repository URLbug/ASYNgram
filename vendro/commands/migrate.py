import os
import __init__

from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData


class Migrate:
    def __init__(self) -> None:
        self.metadata_obj = MetaData()
        self.Base = declarative_base(metadata=self.metadata_obj)

        self.__engine = self.__connect()
        
        self.__Session = sessionmaker(
            bind=self.__engine, 
            class_=AsyncSession,
            expire_on_commit=False
        )
        
    async def session(self) -> AsyncSession:
        async with self.__Session() as session:
            yield session
    
    def __connect(self) -> Engine:
        TYPE = os.getenv('TYPE_DATABASE')
        USERNAME = os.getenv('USERNAME_DATABASE')
        PASSWORD = os.getenv('PASSWORD_DATABASE')
        HOST = os.getenv('HOST_DATABASE')
        PORT = os.getenv('PORT_DATABASE')
        DATABASE = os.getenv('DATABASE')

        if TYPE == 'pgsql':
            URL = f'postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
        else:
            URL = f'mysql+asyncmy://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

        engine = create_async_engine(URL, echo=True)

        return engine

    async def create_table(self) -> None:
        async with self.__engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)

    async def drop_table(self) -> None:
        async with self.__engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.drop_all)

migrate = Migrate()