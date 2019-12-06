from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["https://www.vinabook.com/"]
    start_urls = [
        "https://www.vinabook.com/lop-hoc-mat-ngu-tap-dac-biet-3-p90463.html",
        "https://www.vinabook.com/sieu-tho-u-ngoi-bo-dau-tai-ban-2019-p90511.html",
        "https://www.vinabook.com/lop-hoc-vui-ve-hinh-dang-song-ngu-anh-viet-p90452.html",
        "https://www.vinabook.com/lop-hoc-vui-ve-thoi-gian-song-ngu-anh-viet-p90454.html",
        "https://www.vinabook.com/cung-be-kham-pha-tac-pham-kinh-dien-tam-quoc-dien-nghia-p90414.html",
        "https://www.vinabook.com/sieu-tho-u-ngoi-bo-dau-tai-ban-2019-p90511.html",
        
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="tygh_container"]')

        for question in questions:
            item = CrawlerItem()

            item['name'] = question.xpath('//*[@id="tygh_main_container"]/div[4]/div[1]/div[2]/div/div/div[1]/div/div[2]/h1/text()').get()
            item['description'] = ''.join(question.xpath('//*[@id="product-full-description"]/div[1]/div[1]/div/p').getall())
            item['image'] = question.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/ul/li/div[1]/div[1]/div[1]/img/@src').get()
            item['price'] = question.xpath('//*[@class="price-num"]/text()').get()
            item['author'] = question.xpath('//*[@id="product-full-description"]/div[1]/div[1]/div/div/div[2]/div/div/a/text()').get()
            item['category'] = 'Sách thiếu nhi'
            yield item