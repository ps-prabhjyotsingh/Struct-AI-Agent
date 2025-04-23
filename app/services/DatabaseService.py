from typing import Optional

from app.common.Database import Database
from app.common.Singleton import Singleton


class DatabaseService(metaclass=Singleton):
    _db: Optional[Database]  = None

    @classmethod
    def set(cls, db: Database):
        cls._db = db
    @classmethod
    def get(cls) -> Database:
        if cls._db is None:
            raise Exception("DB is not connected")
        return cls._db