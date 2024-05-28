from itemadapter import ItemAdapter
import sqlite3

class AmazonaiPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('./data/amazon-book.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tabBooks""")
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS tabBooks (
                name TEXT, 
                author TEXT, 
                price TEXT, 
                image TEXT
            )""")

    def store_db(self, item):
        name = item['product_name'][0] if item['product_name'] else 'No Name Available'
        author = ''.join(item['product_author']) if item['product_author'] else 'Unknown Author'
        price = ''.join(item['product_price'])[:6] if item['product_price'] else 'No Price'
        image = item['product_image'][0] if item['product_image'] else 'No Image Available'
        
        self.curr.execute("""
            INSERT INTO tabBooks (name, author, price, image) 
            VALUES (?, ?, ?, ?)
        """, (name, author, price, image))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item) 
        return item