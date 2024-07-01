from sqlalchemy import insert, delete, update

from vendro.commands import migrate

class Table:
    __tablename__ = 'tables'

    session = migrate.session()

    @classmethod
    async def insert_data(self, **kwargs) -> None:
        ins = insert(self).values(**kwargs)

        await self.session.execute(ins)
    
    @classmethod
    async def delete_data(self, operator: bool) -> None:
        await self.session.execute(delete(self).where(operator))
    
    @classmethod
    async def update_data(self, operator: bool, **kwargs) -> None:
        upd = update(self)

        upd = upd.where(operator)
        
        upd = upd.values(**kwargs)

        await self.session.execute(upd)