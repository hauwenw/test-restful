# -*- coding: utf-8 -*-
from crawler.crawlers import Crawler


def update():
    c = Crawler('https://nba.udn.com/nba/index?gr=www')
    c.new_article_check()
