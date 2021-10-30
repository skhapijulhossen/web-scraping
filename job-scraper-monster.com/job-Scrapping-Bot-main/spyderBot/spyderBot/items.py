# Define here the models for your scraped items
# 
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    jobTitles = scrapy.Field()
    Company = scrapy.Field()
    jobLocations = scrapy.Field()
    requiredExperiance = scrapy.Field()
    Salary = scrapy.Field()
    JobDescription = scrapy.Field()
    Skills = scrapy.Field()
