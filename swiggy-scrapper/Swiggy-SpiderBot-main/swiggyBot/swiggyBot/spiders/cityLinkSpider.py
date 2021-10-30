import scrapy
import csv


class CitylinkspiderSpider(scrapy.Spider):
    name = 'cityLinkSpider'
    allowed_domains = ['www.swiggy.com']
    start_urls = ['https://www.swiggy.com/#city-links']

    def parse(self, response):
        citylinks = response.xpath(
            '//*[@id="city-links"]/div/ul/li/a/@href').extract()
        # city = response.url.split('/')

        with open(r"cityLinks.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            for citylink in citylinks:
                link = f'https://www.swiggy.com{citylink}/'
                writer.writerow([link])
