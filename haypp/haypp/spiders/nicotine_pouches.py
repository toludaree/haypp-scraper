
from scrapy import Spider
from haypp.items import HayppItem
from itemloaders import ItemLoader


class NicotinePouchesSpider(Spider):
    name = "nicotine_pouches"
    allowed_domains = ["haypp.com"]
    start_urls = ["https://www.haypp.com/uk/nordic-spirit/nordic-spirit-uk-spearmint-slim-normal",
                  "https://www.haypp.com/uk/velo/velo-freeze-x-strong"]

    def parse(self, response):
        item = ItemLoader(item=HayppItem(),
                          response=response,
                          selector=response)

        # Facts
        item.add_xpath("brand_name",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Brand']/td[2]/a/text()")
        item.add_xpath("product_type",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Product type']/td[2]/a/text()")
        item.add_xpath("format",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Format']/td[2]/text()")
        item.add_xpath("strength",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Strength']/td[2]/text()")
        item.add_xpath("flavour_facts",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Flavour']/td[2]/a/text()")
        item.add_xpath("nicotine_strength_mg_pouch",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Nicotine strength (mg/pouch)']/td[2]/text()")
        item.add_xpath("nicotine_strength_mg_g",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Nicotine strength (mg/g)']/td[2]/text()")
        item.add_xpath("pouches_per_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Pouches per can']/td[2]/text()")
        item.add_xpath("weight_per_pouch_gram",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Weight per pouch (gram)']/td[2]/text()")
        item.add_xpath("content_per_can_gram",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Content per can (gram)']/td[2]/text()")
        item.add_xpath("producer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Producer']/td[2]/text()")

        # Description
        item.add_xpath("category", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Category:']/em/text()")
        item.add_xpath("flavour_pg", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Flavour:']/em/text()")
        item.add_xpath("strength_definition", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Strength Definition:']/em/text()")
        item.add_xpath("manufacturer", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Manufacturer:']/em/text()")
        item.add_xpath("nicotine_mg_portion", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Nicotine mg/portion:']/em/text()")
        item.add_xpath("amount_of_bags_can", "//div[contains(@class, 'p-info-section')]/div[contains(text(), 'Description')]/following-sibling::div/ul/li[strong='Amount of bags/can:']/em/text()")

        yield item.load_item()
