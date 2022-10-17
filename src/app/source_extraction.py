"""
Read the data from postgres tables.
"""
import logging
import sys

from psycopg2.extras import RealDictCursor
from pypika import functions, Parameter
from pypika.queries import Query, QueryBuilder, Table

sys.path.insert(0, '/src')

from utils.utils_postgres import set_connection

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)


class DataExtract:
    """
    Class to read data from the postgres database.
    """

    def __init__(self):
        self.postgres_conn = set_connection(LOGGER)
        self.cursor = self.postgres_conn.cursor(cursor_factory=RealDictCursor)

    def get_products_info(self, offset=0, limit=1000):
        """
        Method to get data from products table
        :param offset:
        :param limit:
        :return:
        """

        product_category_table = Table("product_category_table")
        products_table = Table("products")
        query_builder_obj: QueryBuilder = Query.from_(
            products_table
        ).join(
            product_category_table
        ).on(
            product_category_table.product_category_name == products_table.product_category_name
        ).select(
                products_table.id, product_category_table.product_category_name_english
        ).offset(
                offset
        ).limit(
                limit
        )
        self.cursor.execute(query_builder_obj.get_sql())
        products_data_dict_list = self.cursor.fetchall()

        return products_data_dict_list

    def get_order_stats(self, product_id: str):
        """
        Method to get a products order count and min, max price
        :param product_id:
        :return:
        """
        order_items = Table('order_items')

        query_builder_obj: QueryBuilder = Query.from_(
                order_items
        ).select(
                functions.Count('id').as_("order_count"), functions.Min(order_items.price).as_("min_price"), functions.Max(
                        order_items.price).as_("max_price")
        ).where(
                order_items.product_id == product_id
        )

        self.cursor.execute(query_builder_obj.get_sql())
        seller_data_dict_list = self.cursor.fetchone()
        return seller_data_dict_list
