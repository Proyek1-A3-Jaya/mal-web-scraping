# MyAnimeList Web Scraping
Tugas proyek 1 untuk melakukan scraping rank manga pada website MAL menggunakan scrapy

Project links:
- [Source code UI](https://github.com/Proyek1-A3-Jaya/mal-web-scraping-result)
- [Website Hasil](https://proyek1-a3-jaya.github.io/mal-web-scraping-result/)

## Cara Menjalankan Scraping Pada Sistem Lokal

1. Clone repositori ini
2. Buat dan aktifkan venv pada projek
3. Install library dengan mengetikkan perintah ```pip install -r requirements.txt```.
4. Jalankan spider dengan mengetikkan perintah ```scrapy crawl manga-spider```
5. Hasil dari scraping akan disimpan pada folder assets.

## Cara Menjalankan Scraping Menggunakan Interactive Python (ipython)

1. Setelah melakukan perintah di atas, install library untuk development dengan mengetikkan perintah ```pip install -r requirements_dev.txt```
2. Jalankan scrapy shell dengan mengetikan perintah ```scrapy shell```
3. Lakukan request ke website dengan mengetikkan perintah ```fetch('url yang akan discraping')```
4. Lakukan scraping sesuai keinginan. Lihat [dokumentasi ini](https://docs.scrapy.org/en/latest/topics/shell.html#example-of-shell-session)
