import scrapy
import csv
import time
from ..items import SwiggybotItem


class CityspiderSpider(scrapy.Spider):
    name = 'citySpider'
    allowed_domains = ['www.swiggy.com']

    cityLinks = []
    try:
        with open(r"C:\PYTHON\Swiggy-SpiderBot\swiggyBot\cityLinks.csv", mode='r') as f:
            csvreader = csv.reader(f)
            cityLinks = [row for row in csvreader][0::2]
        start_urls = [links[0] for links in cityLinks]
    except Exception:
        start_urls=[]

    def parse(self, response):
        item = SwiggybotItem()
        city = (response.url.split('/')[-1]).split('?')[0]
        titles = response.xpath(
            '//*[@id="restaurants_container"]/div[2]/div/div/a/div/div/div/div/text()').getall()
        low = 0
        high = 6
        itemData = []

        while high <= (len(titles)):
            itemData = titles[low:high]
            item['restaurantName'] = itemData[0]
            item['foodType'] = itemData[1]
            item['price'] = itemData[5]
            item['deliveryTime'] = itemData[3]
            item['city'] = city
            yield item
            low = high
            high = high+6
