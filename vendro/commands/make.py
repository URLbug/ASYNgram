import os


class Make:
    def write(self, name: str, code: str) -> None:
        with open(f'{name}.py', 'w') as file:
            file.write(code)

            file.close()
    
    def writeInit(self, name: str) -> None:
        with open('__init__.py', 'a') as file:
            file.write(f'from .{name} import {name.title()}\n')

            file.close()
    
    def full_write(self, 
                   name: str, 
                   path: str, 
                   code: str, 
                   exeception: str
                   ) -> None:
        os.chdir(path)

        if os.path.isfile(name):
            raise Exception(exeception)

        self.write(name, code)
        self.writeInit(name)

    def handler(self, name) -> None:
        code = (
                'from aiogram import Router\n'
                '\n'
                f'class {name.title()}:\n'
                '   router = Router(name=__name__)'
            )
        
        self.full_write(name, 
                        './src/handler',
                        code,
                        'A handler with the same name already exists'
                        )

        print("Create handler: " + name)
    
    def filter(self, name: str) -> None:
        code = (
            'from aiogram.filters import Filter\n'
            '\n'
            f'class {name.title()}(Filter):\n'
            '   def __init__(self):\n'
            '       pass'
            )
        
        self.full_write(name, 
                        './src/filter',
                        code,
                        'A filter with the same name already exists'
                        )

        print("Create filter: " + name)
    
    def button(self, name: str) -> None:
        code = (
            'from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder\n'
            'from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup\n'
            '\n'
            f'class {name.title()}:\n'
            '   def inline(self) -> InlineKeyboardMarkup:\n'
            '       build = InlineKeyboardBuilder()\n'
            '\n'
            '       build.button(text="Home", callback_data="home")\n'
            '\n'
            '       return build.as_markup()\n'
            '\n'
            '   def reply(self) -> ReplyKeyboardMarkup:\n'
            '       build = ReplyKeyboardBuilder()\n'
            '\n'
            '       build.button("Home")\n'
            '\n'
            '       return build.as_markup()\n'
            )
        
        self.full_write(name, 
                        './src/button',
                        code,
                        'A button with the same name already exists'
                        )

        print("Create button: " + name)
    
    def state(self, name) -> None:
        code = (
            'from aiogram.fsm.state import State, StatesGroup\n'
            '\n'
            f'class {name.title()}(StatesGroup):\n'
            f'   {name} = State()'
            )
        
        self.full_write(name, 
                        './src/state',
                        code,
                        'A state with the same name already exists'
                        )

        print("Create state: " + name)
    
    def state(self, name) -> None:
        code = (
            'from tables import Table\n'
            '\n'
            f'class {name.title()}(Table):\n'
            f'   __tablename__ = {name}'
            )
        
        self.full_write(name, 
                        './src/database',
                        code,
                        'A table with the same name already exists'
                        )

        print("Create table: " + name)


