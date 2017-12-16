from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self,base_url,page_url):
         super().__init__()
         self.base_url = base_url
         self.page_url = page_url
         self.links = set()

    def page_links(self):
        return self.links

    def handle_starttag(self, tag, attrs):
        if tag == 'a' :
            for (attributes,value) in attrs:
                if attributes == 'href':
                    url = parse.urljoin(self.base_url,value)
                    print(url)
                    self.links.add(url)

    def error(self, message):
        pass


#finder = LinkFinder('','')
#finder.feed('<html><head><title></title>test</head><body><a href="www.abc.com"></a>Parse</body></html>')


