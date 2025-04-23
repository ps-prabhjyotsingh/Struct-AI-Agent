from sqlalchemy.engine import create_engine, URL
from sqlmodel import Session,SQLModel

from app.common.Singleton import Singleton


class Database(metaclass=Singleton):
    driver: str
    host: str
    database: str
    username: str|None = None
    password: str|None = None
    port: int|None = None
    engine = None
    session = None
    def __init__(self, driver: str, host: str, database: str, username: str|None = None,
                 password: str | None = None, port: int|None = None):
        self.driver = driver
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.connect()

    def connect(self):
        connection_str = URL.create(
            self.driver,
            self.username,
            self.password,
            self.host,
            self.port,
            self.database
        )
        self.engine = create_engine(connection_str, echo=True).connect()
        self.session = Session(self.engine)

    def save(self, model: SQLModel):
        self.session.add(model)
        self.session.commit()

    def exec(self, statement):
        return self.session.exec(statement)
    def refresh(self, instance):
        return self.session.refresh(instance)