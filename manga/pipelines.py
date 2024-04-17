# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import hashlib

from itemadapter import ItemAdapter
from contextlib import suppress
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes
from manga.items import MangaInformation

class MangaInformationPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        item = MangaInformation(item)
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        image_filename = f"manga_cover/{image_guid}{'_' + item['title'] if item['title'] != None else ''}.jpg"

        return image_filename

    def item_completed(self, results, item, info):
        with suppress(KeyError):
            ItemAdapter(item)[self.images_result_field] = [x for ok, x in results if ok]

        adapter = ItemAdapter(item)
        if adapter.get('images'):
            item['manga_cover_url'] = '://assets/' + item['images'][0]['path']
        return item