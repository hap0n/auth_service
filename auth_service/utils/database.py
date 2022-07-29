import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class PostgresDB:
    _session_local = None

    @classmethod
    def get_connection_url(cls) -> str:
        usr = os.getenv("POSTGRES_USER")
        pwd = os.getenv("POSTGRES_PWD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        db_name = os.getenv("POSTGRES_DB")
        return f"postgresql://{usr}:{pwd}@{host}:{port}/{db_name}"

    @classmethod
    def get_session_local(cls) -> Session:
        if not cls._session_local:
            engine = create_engine(cls.get_connection_url(), connect_args={"check_same_thread": False})
            cls._session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return cls._session_local()

    @classmethod
    def get_instance(cls) -> Session:
        db = cls.get_session_local()
        try:
            yield db
        finally:
            db.close()
