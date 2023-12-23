from src.data.DataProcessor import DataProcessor
from src.exceptions.DataProcessingError import DataProcessingError
from src.exceptions.ErrorHandler import ErrorHandler

DATA_DIRECTORY = "./data/"
USERS_DATA = ['firstname', 'telephone_number', 'email', 'password', 'role', 'created_at']
CHILDREN_DATA = ['name', 'age']


class DataValidator(DataProcessor):
    def __init__(self, path_to_data_directory=DATA_DIRECTORY):
        try:
            super().__init__(path_to_data_directory)
        except DataProcessingError as data_err:
            ErrorHandler.handle_error(data_err)
        self.users, self.children = self._validate()

    def _validate(self):
        validated_users, validated_children = DataLoaderUtilities.extract(self.dataframe)

        validated_users = (
            validated_users
            .pipe(DataLoaderUtilities.dropna, subset='telephone_number')
            .pipe(DataLoaderUtilities.validate_email)
            .pipe(DataLoaderUtilities.validate_telephone_number)
            .pipe(DataLoaderUtilities.remove_duplicates)
            .pipe(DataLoaderUtilities.adding_id_column)
        )

        validated_children = (
            validated_children
            .pipe(DataLoaderUtilities.dropna)
            .pipe(DataLoaderUtilities.remove_rows_based_on_indexes, validated_users.index)
            .pipe(DataLoaderUtilities.adding_id_column)
        )
        return validated_users, validated_children


class DataLoaderUtilities:
    @staticmethod
    def extract(df):
        return df[USERS_DATA].dropna(subset='telephone_number'), df[CHILDREN_DATA].dropna()

    @staticmethod
    def dropna(df, subset=None):
        return df.dropna(subset=subset)

    @staticmethod
    def validate_email(df):
        return df.loc[df['email'].str.match("^[^ @]+[@][^. @]+[.][a-z0-9]{1,4}$")]

    @staticmethod
    def validate_telephone_number(df):
        df['telephone_number'] = df['telephone_number'].astype(str).str.replace(" ", "").str.slice(start=-9)
        return df

    @staticmethod
    def remove_duplicates(df):
        return (
            df.sort_values(by='created_at', ascending=False)
            .drop_duplicates(subset=['email'])
            .drop_duplicates(subset=['telephone_number'])
            .sort_values(by='index')
        )

    @staticmethod
    def remove_rows_based_on_indexes(df, indexes):
        return df[df.index.isin(indexes)]

    @staticmethod
    def adding_id_column(df):
        df['id'] = df.index
        return df
