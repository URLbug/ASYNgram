from sqlalchemy import insert, delete, update

from vendro.commands import Migrate

class Table:
    __tablename__ = 'tables'

    session = Migrate().session

    @classmethod
    def insert_data(self, **kwargs) -> None:
        ins = insert(self).values(**kwargs)

        self.session.execute(ins)
    
    @classmethod
    def delete_data(self, operator: bool) -> None:
        self.session.execute(delete(self).where(operator))
    
    @classmethod
    def update_data(self, operator: bool, **kwargs) -> None:
        upd = update(self)

        upd = upd.where(operator)
        
        upd = upd.values(**kwargs)

        self.session.execute(upd)