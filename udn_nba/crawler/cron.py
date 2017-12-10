# -*- coding: utf-8 -*-
from crawler.tasks import crawl


def update():
    crawl('https://nba.udn.com/nba/index?gr=www')
