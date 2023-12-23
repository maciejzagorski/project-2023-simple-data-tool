import pandas as pd
from src.data.DataLoader import DataLoader
from src.exceptions.DataProcessingError import DataProcessingError
from src.exceptions.ErrorHandler import ErrorHandler


class DataProcessor(DataLoader):

    def __init__(self, path_to_data_directory):
        try:
            super().__init__(path_to_data_directory)
        except DataProcessingError as data_err:
            ErrorHandler.handle_error(data_err)

        self.filetypes_processors = {
            "xml": lambda df: DataProcessorUtilities.process_data_xml(df),
            "csv": lambda df: DataProcessorUtilities.process_data_csv(df),
            "json": lambda df: DataProcessorUtilities.process_data_json(df),
        }
        self.dataframe = self._process_data()

    def _process_data(self):
        processed_dataframes = [self._process_dataset(dataset) for dataset in self.datasets]
        processed_dataframes = DataProcessorUtilities.concat_dataframes(processed_dataframes)
        return DataProcessorUtilities.change_data_types(processed_dataframes)

    def _process_dataset(self, dataset):
        processor_function = self.filetypes_processors.get(dataset.file_type)
        if processor_function:
            return processor_function(dataset.data)
        else:
            raise DataProcessingError()


class DataProcessorUtilities:
    @staticmethod
    def process_data_xml(df):
        df.insert(0, 'index', df['age'].isnull().cumsum())
        df.reset_index(drop=True, inplace=True)
        return df

    @staticmethod
    def process_data_csv(df):
        df['children'] = df['children'].str.split(',')
        df = DataProcessorUtilities.explode_children(df)
        df[["name", "age"]] = df["children"].str.split(' ', expand=True)
        df['age'] = df['age'].astype(str).str.strip('()')
        return df

    @staticmethod
    def process_data_json(df):
        df = DataProcessorUtilities.explode_children(df)
        df[["name", "age"]] = pd.json_normalize(df["children"])
        return df

    @staticmethod
    def explode_children(df):
        df = df.explode("children")
        df.reset_index(inplace=True)
        return df

    @staticmethod
    def concat_dataframes(dfs):
        for i in range(1, len(dfs)):
            last_index = dfs[i - 1]['index'].tail(1).values + 1
            dfs[i]['index'] = dfs[i]['index'] + last_index

        return pd.concat(dfs).set_index('index')

    @staticmethod
    def change_data_types(df):
        df['created_at'] = pd.to_datetime(df['created_at'], format='%Y-%m-%d %H:%M:%S')
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
        return df
