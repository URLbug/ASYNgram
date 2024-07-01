from sqlalchemy import Column, BigInteger

from .tables import Table
from vendro.commands import migrate

class Test(Table, migrate.Base):
   __tablename__ = "tests"
    
   id = Column(BigInteger, primary_key=True)