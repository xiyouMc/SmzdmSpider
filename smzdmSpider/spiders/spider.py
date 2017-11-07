from smzdmSpider.items import SmzdmspiderItem, HotSearchItem
# from smzdmSpider.items import HotSearchItem
import scrapy


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    start_urls = ['https://www.smzdm.com/']

    def parse(self, response):
        # print response.body
        selector = scrapy.Selector(response)
        hotSearchs = selector.xpath(
            '//form[@id="search-form"]/div[@class="hot-words"]/a')
        for hotSearch in hotSearchs:
            print(hotSearch.xpath("text()").extract_first())
            print(hotSearch.xpath("@href").extract_first())
            # print(hotSearch.extract())
            
            smzdmspiderItem = SmzdmspiderItem()
            smzdmspiderItem['href'] = hotSearch.xpath("@href").extract_first()
            smzdmspiderItem['name'] = hotSearch.xpath("text()").extract_first()
            yield smzdmspiderItem