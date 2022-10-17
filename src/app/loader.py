import sys

sys.path.insert(0, '/src')
from utils.utils_es import index_data


class Loader:

    def __init__(self, es_conection_obj, index_name: str):
        """

        :param es_conection_obj:
        :param index_name:
        """
        self.__es_connector = es_conection_obj
        self.__index_name = index_name

    def load(self, data: dict):
        """

        :param data:
        :return:
        """
        index_data(es_connector=self.__es_connector,
                   index_name=self.__index_name,
                   data_dict=data)
