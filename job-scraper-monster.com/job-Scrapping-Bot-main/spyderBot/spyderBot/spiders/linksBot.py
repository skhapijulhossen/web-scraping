import scrapy


class Bot(scrapy.Spider):
    name = "SpyderBot"
    start_urls = ["https://www.monsterindia.com/search/jobs-by-skill"]

    # response.xpath('//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li/a/@href').getall()
    # response.xpath('//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li[40]/ul/li/a/@href').getall()

    def parse(self, response):
        links = response.xpath('//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li/a/@href').getall()
        leftLinks = response.xpath('//*[@id="themeDefault"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div/div/ul/li[40]/ul/li/a/@href').getall()
        links.extend(leftLinks)
        with open('links.csv',mode='a') as f:
            f.write('\n'.join(links))
