# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import hashlib

class MangaInformation(scrapy.Item):
    title = scrapy.Field() # Judul manga
    rank = scrapy.Field() # Rank manga
    manga_mal_url = scrapy.Field() # URL ke detail manga pada website MyAnimeList
    manga_cover_url = scrapy.Field() # URL ke gambar yang sudah didownload

    # Untuk pipeline gambar
    image_urls = scrapy.Field()
    images = scrapy.Field()