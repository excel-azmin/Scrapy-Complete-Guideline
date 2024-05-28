# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapperaiPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('./data/scrapperAI.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tabQuotes""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS tabQuotes(title TEXT, author TEXT, tag TEXT)""")    
    
    def strore_db(self, item):
        self.curr.execute("""INSERT INTO tabQuotes VALUES(?, ?, ?)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
    
    def process_item(self, item, spider):
        self.strore_db(item)
        print("\n\nPipeline: ", item['tag'])
        return item
