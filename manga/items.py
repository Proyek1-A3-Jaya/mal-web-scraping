# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import hashlib


class MangaInformation(scrapy.Item):
    title = scrapy.Field()  # Judul manga
    rank = scrapy.Field()  # Rank manga
    rating = scrapy.Field()  # Rating manga
    manga_mal_url = scrapy.Field()  # URL ke detail manga pada website MyAnimeList
    manga_cover_url = scrapy.Field()  # URL ke gambar yang sudah didownload

    # Untuk pipeline gambar
    image_urls = scrapy.Field()
    images = scrapy.Field()

    # Untuk keterangan left-side
    authors = scrapy.Field()
    altTittle = scrapy.Field()
    volumes = scrapy.Field()
    chapters = scrapy.Field()
    status = scrapy.Field()
    published = scrapy.Field()
    genres = scrapy.Field()
    themes = scrapy.Field()
    demographic = scrapy.Field()
    serialization = scrapy.Field()

    # Untuk keterangan right-side
    type = scrapy.Field()
    season = scrapy.Field()
    popularity = scrapy.Field()
    members = scrapy.Field()
