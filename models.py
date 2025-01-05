import _io
import json

import sqlalchemy.engine
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass


class Classrooms(Base):
    __tablename__ = 'classrooms'

    classroom_number: Mapped[int] = mapped_column(primary_key=True)
    classroom_chairs: Mapped[int] = mapped_column(Integer)
    with_projector: Mapped[bool] = mapped_column(default=False)
    is_being_computer_office: Mapped[bool] = mapped_column(default=False)
    is_small: Mapped[bool] = mapped_column(default=False)
    is_being_gym: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"Classroom(id={self.classroom_number!r}, chairs={self.classroom_chairs})"


if __name__ == '__main__':
    """Создаёт таблицу classrooms в той бд, что указанна в config.json"""
    CONFIG_PATH: str = 'static/config.json'
    config_file = open(CONFIG_PATH, 'r', encoding='utf8')
    config: dict = json.load(config_file)
    config_file.close()

    # database_login database_password database_host database_name
    login: str = config['database_login']
    password: str = config['database_password']
    host: str = config['database_host']
    db_name: str = config['database_name']
    connection_string: str = f'postgresql+psycopg2://{login}:{password}@localhost/{db_name}'
    engine: sqlalchemy.engine.base.Engine = sqlalchemy.create_engine(connection_string, isolation_level="SERIALIZABLE")
    Base.metadata.create_all(engine)
