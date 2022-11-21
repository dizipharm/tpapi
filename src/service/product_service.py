from src.models.product import Product
from src.service.db_service import DBService


class ProductService(DBService):

    def __init__(self):
        super().__init__()
        #TODO: this secret name should be loaded from config files
        self.conn = super().get_db_connection("tpadmin")

    def get_products(self):
        cursor = self.conn.cursor()
        cursor.execute(f"select * from {Product.TABLE}")
        rows = cursor.fetchall()
        return rows

    def create_product(self, product: Product):
        cursor = self.conn.cursor()
        cursor.execute("insert", product)





service = ProductService()
products = service.get_products()
print(products)




