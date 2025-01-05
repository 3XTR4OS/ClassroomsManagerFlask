import logging

import pandas.core.frame
import sqlalchemy
import json
from excel_reader import Excel


class DataBase:
    def __init__(self):
        """ Создаёт соединение по данным из config'а """
        self.__config_path = 'static/config.json'

        with open(file=self.__config_path, mode='r', encoding='UTF8') as file:
            json_file = json.load(file)
            __login = json_file['database_login']
            __password = json_file['database_password']
            __host = json_file['database_host']
            __db_name = json_file['database_name']

        connection_string: str = f'postgresql+psycopg2://{__login}:{__password}@{__host}/{__db_name}'
        self.engine: sqlalchemy.engine.base.Engine = sqlalchemy.create_engine(connection_string,
                                                                              isolation_level="SERIALIZABLE")

    def load_dataframe_to_postgres_table(self, dataframe: pandas.core.frame.DataFrame, table_name):
        dataframe.to_sql(table_name, self.engine, if_exists='replace')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    ex: Excel = Excel()
    db: DataBase = DataBase()
    cabs_data: pandas.core.frame.DataFrame = ex.read_excel_file('saved/ClassRoomsData.xlsx')

    try:
        db.load_dataframe_to_postgres_table(dataframe=cabs_data, table_name='classrooms')
        logging.log(logging.DEBUG, 'SUCCESS EXPORT')
    except Exception as e:
        logging.log(logging.DEBUG, f'Произошла ошибка \n {e}')
