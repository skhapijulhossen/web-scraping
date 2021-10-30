import scrapy
import csv


class CityinsiderSpider(scrapy.Spider):
    name = 'cityInsider'
    allowed_domains = ['www.swiggy.com']
    # start_urls = ['http://www.swiggy.com/']

    cityLinks = []
    try:
        with open(r"C:\PYTHON\Swiggy-SpiderBot\swiggyBot\cityLinks.csv", mode='r') as f:
            csvreader = csv.reader(f)
            cityLinks = [row for row in csvreader][0::2]
        start_urls = [links[0] for links in cityLinks]
        # start_urls=['https://www.swiggy.com/abohar']
    except Exception:
        start_urls = ['https://www.swiggy.com/abohar']

    def parse(self, response):
        url = response.url

        # Exception Handeling if there only onepage
        try:
            nextPage = response.xpath(
                '//*[@id="restaurants_container"]/div[3]/a/text()').getall()
            lastpage = int(nextPage[-1])
        except Exception:
            lastpage = 0

        # Genarate all Pages Url
        urls = []
        if lastpage > 1:
            for page in range(2, lastpage+1):
                pageUrl = f'{url}?page={page}'
                urls.append([pageUrl])
            urls.append([url])
        else:
            urls.append([url])

        # Write to file
        with open(r'cityInsiderLinks.csv', mode='a') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(urls)
