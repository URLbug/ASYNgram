from typing import Any

from sqlalchemy import insert, delete, update

from vendro.commands import migrate

class Table:
    __tablename__ = 'tables'

    @classmethod
    async def create(self, **kwargs) -> None:
        ins = insert(self).values(**kwargs)

        await migrate.session(ins)
    
    @classmethod
    async def delete_data(self, operator: bool) -> None:
        await migrate.session(delete(self).where(operator))
    
    @classmethod
    async def update_data(self, operator: bool, **kwargs) -> None:
        upd = update(self)

        upd = upd.where(operator)
        
        upd = upd.values(**kwargs)

        await migrate.session(upd)