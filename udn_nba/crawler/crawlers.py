# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from crawler.models import Article, Video

from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware


class Crawler(object):

    def __init__(self, article_list_url):
        self.article_list_url = article_list_url

    @staticmethod
    def _extract_raw_data(url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
        else:
            raise requests.ConnectionError('HTTP Status Code Not 200')

    @staticmethod
    def _extract_article_detail(url):
        detail_page_content = Crawler._extract_raw_data(url)
        soup = BeautifulSoup(detail_page_content, 'html.parser')
        title = soup.find('meta', property='og:title').attrs.get('content')
        posted = soup.select('.shareBar__info--author span')[0].text
        main_image = soup.find_all('meta', property='og:image')[0].attrs.get('content')
        videos = []
        content = soup.select('#story_body_content')[0]

        # remove unwanted tags
        for selector in ['script', '#shareBar']:
            for item in content.select(selector):
                item.extract()

        for video in content.select('iframe'):
            videos.append(video.attrs.get('src'))

        return {'title': title.replace(u'| NBA戰況 | NBA 台灣', ''),
                'main_image': main_image,
                'content': content.select('span p')[0].getText().replace(u'不想錯過 NBA 大小消息，就來加入NBA Taiwan 粉絲團吧！', ''),
                'videos': videos,
                'posted': make_aware(parse_datetime(posted))}

    def _extract_article_list(self):
        list_page_content = Crawler._extract_raw_data(self.article_list_url)
        soup = BeautifulSoup(list_page_content, 'lxml')
        article_a_tags = soup.select('#news dl dt a')
        for tag in article_a_tags:
            yield urlparse.urljoin(self.article_list_url ,tag.attrs.get('href'))

    def new_article_check(self):
        existing_urls = Article.objects.values_list('url', flat=True).distinct()
        try:
            for new_article_url in self._extract_article_list():
                if new_article_url not in existing_urls:
                    result = Crawler._extract_article_detail(new_article_url)
                    new_article = Article(url=new_article_url,
                                          title=result['title'],
                                          main_image=result['main_image'],
                                          content=result['content'],
                                          posted=result['posted'])
                    new_article.save()
                    for video in result['videos']:
                        new_video = Video(article=new_article,
                                          source=video)
                        new_video.save()

        except requests.ConnectionError:
            pass
