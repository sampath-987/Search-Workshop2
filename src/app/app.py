import os
import sys

sys.path.insert(0, '/src')

from utils.utils_es import get_es_connection
from loader import Loader
from source_extraction import DataExtract


class Index:

    def __init__(self):
        es_obj = get_es_connection(host=os.environ['ES_HOST'],
                                   port=os.environ['ES_PORT'])
        self.__loader_obj = Loader(es_conection_obj=es_obj, index_name="product_index")

    @staticmethod
    def process(product_info_dict: dict, order_stats_dict: dict):
        processed_dict = {
            "productId": product_info_dict["id"],
            "productCategory": product_info_dict["product_category_name_english"],
            "OrderStats": {
                "orderCount": order_stats_dict["order_count"],
                "minPrice": order_stats_dict["min_price"],
                "maxPrice": order_stats_dict["max_price"],
            }
        }
        return processed_dict

    def main(self):
        """

        :param self:
        :return:
        """

        data_extractor_obj = DataExtract()
        product_info_dict_list = data_extractor_obj.get_products_info(limit=1000, offset=0)

        for product_info_dict in product_info_dict_list:
            order_stats_dict = data_extractor_obj.get_order_stats(product_info_dict['id'])

            proceesed_data_dict = self.process(product_info_dict, order_stats_dict)
            self.__loader_obj.load(data=proceesed_data_dict)


if __name__ == '__main__':
    INDEX_OBJ = Index()
    INDEX_OBJ.main()
