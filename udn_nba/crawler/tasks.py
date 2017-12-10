from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def crawl(start_url):
    from crawler.crawlers import Crawler
    c = Crawler(start_url)
    c.new_article_check()
