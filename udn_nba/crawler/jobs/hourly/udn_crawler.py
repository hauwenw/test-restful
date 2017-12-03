from django_extensions.management.jobs import HourlyJob
from crawler.crawlers import Crawler


class UDNJob(HourlyJob):
    help = "UDN NBA crawler"

    def execute(self):
        print 'yoooo'
        c = Crawler('https://nba.udn.com/nba/index?gr=www')
        c.new_article_check()
