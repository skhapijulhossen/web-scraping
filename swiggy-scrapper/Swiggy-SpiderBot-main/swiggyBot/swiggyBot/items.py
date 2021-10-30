# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SwiggybotItem(scrapy.Item):
    # define the fields for your item here like:
    restaurantName = scrapy.Field()
    foodType = scrapy.Field()
    price = scrapy.Field()
    deliveryTime = scrapy.Field()
    city = scrapy.Field()
    
