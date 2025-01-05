import pandas as pd
import pandas.core.frame


class Excel:
    def __init__(self):
        pass

    def read_excel_file(self, file_path: str) -> pandas.core.frame.DataFrame:
        data: pandas.core.frame.DataFrame = pd.read_excel(file_path)
        # data = data.replace(True, 'да')
        # data = data.replace(False, 'нет')
        boolean_columns = ['Наличие проектора', 'Компьютерный кабинет', 'Небольшой', 'Явл. Спортзалом']
        # data[boolean_columns] = data[boolean_columns].map({'yes': 1, 'no': 0})
        for column in boolean_columns:
            data[column] = data[column].map({'да': True, 'нет': False})

        return data
