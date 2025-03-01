from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.crawler.spiders.spider import Spider

def run_spider():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(Spider)
    process.start()

if __name__ == "__main__":
    run_spider()
