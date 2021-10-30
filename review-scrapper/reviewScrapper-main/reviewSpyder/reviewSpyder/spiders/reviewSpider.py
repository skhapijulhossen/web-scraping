import scrapy
from reviewSpyder.items import ReviewspyderItem


class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewSpider'
    allowed_domains = ['https://www.shopvote.de/']
    start_urls = ['https://www.shopvote.de/bewertung_paarzeit_de_17441.html']

    def parse(self, response):

        reviewer = response.xpath(
            '/html/body/div[1]/div[2]/section/div/div[2]/div[2]/div/div/div[1]/div[2]/div/span/text()').getall()

        ratings = response.xpath(
            '/html/body/div[1]/div[2]/section/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]').getall()
        filtered_ratings = []
        for rating in ratings:
            filtered_ratings.append(rating.split('</span>')[1].split('<')[0])

        dates = response.xpath(
            '/html/body/div[1]/div[2]/section/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/text()').getall()
        filtered_dates = []
        for date in dates:
            filtered_dates.append(date.replace('\t', '').replace('\n', ''))

        message = response.xpath(
            '/html/body/div[1]/div[2]/section/div/div[2]/div[2]/div/div/div[2]/div[3]/div/p/span/text()').getall()
        # next = "https://www.shopvote.de/" + \
        #     response.xpath(
        #         '/html/body/div[1]/div[2]/section/div/div[2]/div[2]/div[22]/ul/li[8]/a/@href').getall()
        items = ReviewspyderItem()
        for index in range(len(reviewer)):
            items['reviewer'], items['rating'], items['date'], items['message'] = reviewer[
                index], filtered_ratings[index], filtered_dates[index], message[index]
            yield items
