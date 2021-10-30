import scrapy
import csv
import re
# from ..items import JobItem


class JobSpyderBot(scrapy.Spider):
    name = 'jobScraperBot'
    # Loading Links
    links = []
    with open(r"C:\PYTHON\job-Scrapping-Bot\links.csv", mode='r') as f:
            reader = csv.reader(f)
            links = [link[0] for link in reader]
    
    # start_urls = links[0:21]
    start_urls = [links[0]]

    def parse(self, response):

        # item = JobItem()
        url = (response.url.split('/')[-1]).split('?')[0]
        if url[-2] == '-':
            filename = (response.url.split('/')[-1]).split('?')[0][0:-2]
        elif url[-3] == '-':
            filename = (response.url.split('/')[-1]).split('?')[0][0:-3]
        elif url[-4] == '-':
            filename = (response.url.split('/')[-1]).split('?')[0][0:-4]
        else:
            filename = url
            file=r"C:\PYTHON\job-Scrapping-Bot\ScrappedJobs\{}.csv".format(url)
            with open(file, mode='a') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow(["jobTitles", "Company", "jobLocations",
                                    "requiredExperiance", "Salary", "JobDescription", "Skills"])
        jobTitles = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div/div/div/h3/a/text()').getall()

        JobDescription = []
        for i in range(1, len(jobTitles)):
            JobDescription.append(' | '.join(response.xpath(
                f'//*[@id="srp-jobList"]/div/div[{i}]/div/div/div/p[1]/text()').getall()))

        skills = ''
        Skills = []
        for i in range(1, len(jobTitles)):
            skills = ''
            for skill in response.xpath(f'//*[@id="srp-jobList"]/div/div[{i}]/div/div[1]/div/p[2]/label/a/text()').extract():
                skills += f"{skill}|"
            Skills.append(re.sub(r"[\n\s]", '', skills).replace('||', '|'))

        Company = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/span/a/text()').extract()

        jobLocations = []
        for i in range(1, len(jobTitles)):
            jobLocations.append(re.sub(r'[\n\s]', '', ' | '.join(response.xpath(
                f'//*[@id="srp-jobList"]/div/div[{i}]/div/div[1]/div/div/div/div[1]/span/small/text()').extract()[0::2])))

        requiredExperiance = re.sub(r'[\n\s]', '', ' | '.join(response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/div/div[2]/div/span/small/text()').extract()[1::2])).split('|')

        Salary = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/div/div[3]/span/small/text()').extract()

        filename=r"C:\PYTHON\job-Scrapping-Bot\ScrappedJobs\{}.csv".format(filename)
        with open(filename, mode='a',encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            try:
                for row in range(len(jobTitles)):
                    # item["jobTitles"], item["Company"], item["jobLocations"], item["requiredExperiance"], item["Salary"], item["JobDescription"], item["Skills"] = [(re.sub(
                    #     r'[\n]', '', data).lstrip()).rstrip() for data in [jobTitles[row], Company[row], jobLocations[row], requiredExperiance[row], Salary[row], JobDescription[row], Skills[row]]]
                    # yield item
                    rowData = [(re.sub( r'[\n]', '', data).lstrip()).rstrip() for data in [jobTitles[row], Company[row], jobLocations[row], requiredExperiance[row], Salary[row], JobDescription[row], Skills[row]]]
                    csvwriter.writerow(rowData)
            except IndexError:
                pass
        
        nextPage = response.xpath('//*[@id="pag-data"]/a/@href').extract()[-1]
        if nextPage:
           yield  response.follow(nextPage, callback=self.parse)
