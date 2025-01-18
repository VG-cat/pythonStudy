import requests
from lxml import etree
from retrying import retry
class jinjiang(object):
    def __init__(self):
        self.url = "http://www.xjzx.site:5000/news/2"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        response = requests.get(url, timeout=5, headers=self.headers)
        # t1=unicodedata.normalize('NFC',response.content.decode("gbk"))
        assert response.status_code == 200
        return etree.HTML(response.content.decode('utf-8'))
    def parse_url(self, url):
        try:
            html = self._parse_url(url)
        except Exception as e:
            print(e)
            html = None
        return html
    def get_contect_list(self, html):
        content_list = []
        div_list = html.xpath("//div[@class='detail_con fl']//p/text()")
        return div_list

    def save_content(self, content):
        print(content)
        with open('../yuncitu/test.txt', 'a', encoding='utf-8') as f:
            f.write(content)
    def run(self):
        html = self.parse_url(self.url)
        content_list = self.get_contect_list(html)
        for content in content_list:
            self.save_content(content)
if __name__ == '__main__':
    jin = jinjiang()
    jin.run()
