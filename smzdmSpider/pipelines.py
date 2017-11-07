# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import HotSearchItem, Tags
import pymongo
from pymongo import IndexModel, ASCENDING

class SmzdmspiderPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Smzdm"]
        self.hotSearch = db["HotSearch"]
        idx = IndexModel([('name', ASCENDING)], unique=True)
        self.hotSearch.create_indexes([idx])

        self.tags = db['Tags']
        self.tags.create_indexes([idx])

    def process_item(self, item, spider):
        
        if isinstance(item,HotSearchItem):
            self.hotSearch.update_one({'name':item['name']},{'$set':dict(item)},upsert=True)        
        elif isinstance(item,Tags):
            self.tags.update_one({'name':item['name']},{'$set':dict(item)},upsert=True)        

        return item
