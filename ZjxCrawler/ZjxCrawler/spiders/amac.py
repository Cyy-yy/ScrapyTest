import logging
import scrapy
from ZjxCrawler.items import ZjxcrawlerItem

logger = logging.getLogger(__name__)


class AmacSpider(scrapy.Spider):
    name = 'amac'
    allowed_domains = ['amac.org.cn']
    base_url = "https://www.amac.org.cn//portal/front/mutualFund/findMutualFundHousePage"
    page_num = 1
    start_urls = [base_url+f"?pageNo={page_num}&pageSize=10"]

    def parse(self, response):
        rtn = response.json()["data"]["data"]["dataList"]
        item = ZjxcrawlerItem()
        for row in rtn:
            item["fund_name"] = row["houseName"]
            item["address"] = row["registerAddr"]
            logger.warning(item)
            yield item
        if self.page_num < 10:
            self.page_num += 1
            url = self.base_url + f"?pageNo={self.page_num}&pageSize=10"
            yield scrapy.Request(url, callback=self.parse)

