import scrapy
import logging
from scrapy.http import Request, Response
from manga.settings import PROJECT_ROOT
from manga.items import MangaInformation

class MangaScraper(scrapy.Spider):
    name = "manga-spider"
    allowed_domains = ['myanimelist.net']
    start_urls = ["https://myanimelist.net/topmanga.php"]

    # ? Mendefinisikan maksimal halaman yang akan diambil ( tiap halaman terdapat 10 manga ) serta counter
    MAX_PAGE = 1
    counter = 1

    def parse(self, response: Response):

        # ? Melakukan looping untuk setiap manga pada ranking
        for mangas in response.css('tr.ranking-list'):
            # ? Membuat class item untuk menyimpan hasil
            manga_information = MangaInformation()

            # ? Mengambil rank, title, dan link detail dari manga
            manga_information['rank'] = mangas.css('span.lightLink.top-anime-rank-text::text').get()
            manga_information['title'] = mangas.css('a.hoverinfo_trigger.fs14.fw-b::text').get()
            manga_information['manga_mal_url'] = mangas.css('a.hoverinfo_trigger.fs14.fw-b::attr(href)').get()

            # ? Mengambil data lebih lanjut dari link detail manga
            yield scrapy.Request(url=manga_information['manga_mal_url'], callback=self.parse_manga_detail, cb_kwargs={ 'manga_information': manga_information })

        # ? Mengambil link ke halaman selanjutnya, akan terus berjalan sampai tidak ada halaman lagi atau sudah memenuhi maksimal halaman
        next_page = response.css("a.link-blue-box.next::attr(href)").get()
        if next_page != None and self.counter < self.MAX_PAGE:
            self.counter += 1
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback = self.parse)

    def parse_manga_detail(self, response: Response, manga_information: MangaInformation):
        # ? Mengambil url gambar cover manga
        left_side = response.css('div.leftside')
        manga_image_url = left_side.css('div:first-child a img::attr(data-src)').get()

        # Menyimpan hasil ke dalam variable
        manga_information['manga_cover_url'] = ''
        manga_information['image_urls'] = [manga_image_url]

        yield manga_information
