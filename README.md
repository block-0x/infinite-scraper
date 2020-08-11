# 無制限SCRAPERをつくる

## setting

### Splashインストール

1. [docker](https://www.docker.com/) をインストール
　
2. dockerイメージをpull

```bash
# Linux
sudo docker pull scrapinghub/splash
# Mac
docker pull scrapinghub/splash
```
　
3. コンテナを作成・起動

```bash
# Linux
sudo docker run -it -p 8050:8050 scrapinghub/splash
# Mac
docker run -it -p 8050:8050 scrapinghub/splash
```

http://localhost:8050/ にアクセスして起動確認

### html scraping

ページのhtmlを取得

```
$ python html_scraper.py
```

### png scraping

```
$ python png_scraper.py
```

### jpeg scraping

```
$ python jpeg_scraper.py
```

### har scraping

```
$ python har_scraper.py
```