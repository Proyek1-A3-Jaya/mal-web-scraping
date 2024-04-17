import logging
import json
from operator import itemgetter
from manga.settings import IMAGES_STORE
from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)


class SortJson:
    """
    Extension yang dibuat secara manual untuk menyortir file json

    Dibuat oleh: Yobel El'Roy Doloksaribu - @k31p
    """

    def __init__(self, item_count):
        self.item_count = item_count
        self.items_scraped = 0

    @classmethod
    def from_crawler(cls, crawler):
        # get the number of items from settings
        item_count = crawler.settings.getint("MYEXT_ITEMCOUNT", 1000)

        # instantiate the extension object
        ext = cls(item_count)

        # connect the extension object to signals
        crawler.signals.connect(ext.feed_slot_closed, signal=signals.feed_slot_closed)

        # return the extension object
        return ext

    def feed_slot_closed(self, slot):
        with open(IMAGES_STORE + "/manga_data.json", "r") as filebuf:
            json_file = json.load(filebuf)
            sorted_rank = json.dumps(
                sorted(json_file, key=itemgetter("rank")), indent=2
            )
            filebuf.close()

        with open(IMAGES_STORE + "/manga_data.json", "w") as filebuf:
            filebuf.write(sorted_rank)
            filebuf.close()
