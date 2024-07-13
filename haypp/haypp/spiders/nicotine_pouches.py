
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from haypp.items import HayppItem
from itemloaders import ItemLoader


class NicotinePouchesSpider(CrawlSpider):
    name = "nicotine_pouches"
    allowed_domains = ["haypp.com"]
    start_urls = ["https://www.haypp.com/uk/nicotine-pouches/"]

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//div[@class='grid']" \
                                "/div[@data-product-source]" \
                                "/div[contains(@class, 'product-card')]/a"
            ),
            callback="parse",
            follow=True
        ),
    )

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
        item.add_xpath("brand_name",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Brand']/td[2]/text()")
        
        item.add_xpath("product_type",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Product type']/td[2]/a/text()")
        item.add_xpath("product_type",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Product type']/td[2]/text()")
        
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
        item.add_xpath("flavour_facts",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Facts')]" \
                       "/following-sibling::div" \
                       "//tr[td='Flavour']/td[2]/text()")
        
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
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Category')]/em/text()")
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Category')]/em[2]/text()")
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Category')]/em/text()")
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Category')]/text()")
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Category')]/text()")
        item.add_xpath("category",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Category')]/text()")
        
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(strong, 'Flavour')]/em/text()")
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(em/strong, 'Flavour')]/em[2]/text()")
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(strong/em, 'Flavour')]/em/text()")
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(strong, 'Flavour')]/text()")
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(em/strong, 'Flavour')]/text()")
        item.add_xpath("flavour_pg",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                        "/ul/li[contains(strong/em, 'Flavour')]/text()")
        
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Strength')]/em/text()")
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Strength')]/em[2]/text()")
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Strength')]/em/text()")
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Strength')]/text()")
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Strength')]/text()")
        item.add_xpath("strength_definition",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Strength')]/text()")
        
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Manufacturer')]/em/text()")
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Manufacturer')]/em[2]/text()")
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Manufacturer')]/em/text()")
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Manufacturer')]/text()")
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Manufacturer')]/text()")
        item.add_xpath("manufacturer",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Manufacturer')]/text()")
        
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Nicotine')]/em/text()")
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Nicotine')]/em[2]/text()")
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Nicotine')]/em/text()")
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Nicotine')]/text()")
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Nicotine')]/text()")
        item.add_xpath("nicotine_mg_portion",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Nicotine')]/text()")
        
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Amount of bags')]/em/text()")
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Amount of bags')]/em[2]/text()")
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Amount of bags')]/em/text()")
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong, 'Amount of bags')]/text()")
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(em/strong, 'Amount of bags')]/text()")
        item.add_xpath("amount_of_bags_can",
                       "//div[contains(@class, 'p-info-section')]" \
                       "/div[contains(text(), 'Description')]" \
                       "/following-sibling::div" \
                       "/ul/li[contains(strong/em, 'Amount of bags')]/text()")

        yield item.load_item()
