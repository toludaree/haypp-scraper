# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class HayppItem(Item):
    brand_name = Field()
    product_type = Field()
    format = Field()
    strength = Field()
    flavour_facts = Field()
    nicotine_strength_mg_pouch = Field()
    nicotine_strength_mg_g = Field()
    pouches_per_can = Field()
    weight_per_pouch_gram = Field()
    content_per_can_gram = Field()
    producer = Field()
    category = Field()
    flavour_pg = Field()
    strength_definition = Field()
    manufacturer = Field()
    nicotine_mg_portion = Field()
    amount_of_bags_can = Field()
