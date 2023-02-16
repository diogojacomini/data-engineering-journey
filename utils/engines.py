import os
import dotenv
import sqlalchemy

BASE_DIR = os.path.dirname(os.path.realpath("__file__"))
dotenv.load_dotenv(os.path.join(BASE_DIR, ".env"))


def get_engine(database: str):
    return sqlalchemy.create_engine(os.environ.get(f"{database}", False))

def get_api(name: str):
    return os.environ.get(name, False)
