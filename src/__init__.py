import os

from dotenv import load_dotenv
from aiogram import Bot
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


# Load ENV file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Bot conn
bot = Bot(os.getenv('TOKEN'))

# Database
# USERNAME = os.getenv('USERNAME_DATABASE')
# PASSWORD = os.getenv('PASSWORD_DATABASE')
# HOST = os.getenv('HOST_DATABASE')
# PORT = os.getenv('PORT_DATABASE')
# DATABASE = os.getenv('DATABASE')

# URL = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# engine = create_engine(URL)

# if not database_exists(engine.url):
#     create_database(engine.url)

# Session = sessionmaker(bind=engine)

# session = Session()

# from database.tables import create_table

# create_table()