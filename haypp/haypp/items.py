# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from itemloaders.processors import Join, MapCompose


def strip(d:str):
    return d.strip()


class HayppItem(Item):
    # Facts
    brand_name = Field(input_processor=MapCompose(strip),
                       output_processor=Join())
    product_type = Field(input_processor=MapCompose(strip),
                         output_processor=Join())
    format = Field(input_processor=MapCompose(strip),
                   output_processor=Join())
    strength = Field(input_processor=MapCompose(strip),
                     output_processor=Join())
    flavour_facts = Field(input_processor=MapCompose(strip),
                          output_processor=Join())
    nicotine_strength_mg_pouch = Field(input_processor=MapCompose(strip),
                                       output_processor=Join())
    nicotine_strength_mg_g = Field(input_processor=MapCompose(strip),
                                   output_processor=Join())
    pouches_per_can = Field(input_processor=MapCompose(strip),
                            output_processor=Join())
    weight_per_pouch_gram = Field(input_processor=MapCompose(strip),
                                  output_processor=Join())
    content_per_can_gram = Field(input_processor=MapCompose(strip),
                                 output_processor=Join())
    producer = Field(input_processor=MapCompose(strip),
                     output_processor=Join())

    # Description
    category = Field(output_processor=Join())
    flavour_pg = Field(output_processor=Join())
    strength_definition = Field(output_processor=Join())
    manufacturer = Field(output_processor=Join())
    nicotine_mg_portion = Field(output_processor=Join())
    amount_of_bags_can = Field(output_processor=Join())
