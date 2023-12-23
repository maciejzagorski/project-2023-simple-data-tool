import lxml
import pandas as pd
from pathlib import Path
from src.data.Dataset import Dataset
from src.exceptions.DataProcessingError import DataProcessingError


class DataLoader:

    def __init__(self, path_to_data_directory):
        self.filetypes_loaders = {
            "xml": lambda path: pd.read_xml(path, parser='lxml', xpath='(.//user|./user/children/*)', dtype=str),
            "csv": lambda path: pd.read_csv(path, sep=";"),
            "json": lambda path: pd.read_json(path),
        }
        self.datasets = self._load_data(path_to_data_directory)

    def _load_data(self, path_to_data_directory):
        datafiles_paths = DataLoaderUtilities.get_datafiles_paths(path_to_data_directory)
        loaded_datasets = [self._load_data_from_file(datafile_path) for datafile_path in datafiles_paths]
        return loaded_datasets

    def _load_data_from_file(self, datafile_path):
        filetype = datafile_path.suffix[1:]
        loader_function = self.filetypes_loaders.get(filetype)
        if loader_function:
            return Dataset(filetype, loader_function(datafile_path))
        else:
            raise DataProcessingError()


class DataLoaderUtilities:
    @staticmethod
    def get_datafiles_paths(path_to_data_directory):
        data_directory = Path(path_to_data_directory)
        return data_directory.rglob("*.*")
