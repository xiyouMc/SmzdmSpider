from smzdmSpider.items import SmzdmspiderItem, HotSearchItem, Tags
# from smzdmSpider.items import HotSearchItem
import scrapy


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    start_urls = ['https://www.smzdm.com/']

    def parse(self, response):
        # print response.body
        selector = scrapy.Selector(response)
        hotSearchsSelector = selector.xpath(
            '//form[@id="search-form"]/div[@class="hot-words"]/a')
        for hotSearch in hotSearchsSelector:
            print(hotSearch.xpath("text()").extract_first())
            print(hotSearch.xpath("@href").extract_first())
            # print(hotSearch.extract())

            smzdmspiderItem = SmzdmspiderItem()
            smzdmspiderItem['href'] = hotSearch.xpath("@href").extract_first()
            smzdmspiderItem['name'] = hotSearch.xpath("text()").extract_first()
            yield smzdmspiderItem

        tagsSelector = selector.xpath(
            '//div[@id="category"]/ul[@class="category-ul"]/li[@class="category-item"]/h3/a'
        )
        for tag in tagsSelector:
            tags = Tags()
            tags['href'] = tag.xpath("@href").extract_first()
            tags['name'] = tag.xpath("text()").extract_first()
            yield tags