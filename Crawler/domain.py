from urllib.parse import urlparse


#GET domain name (naem.example.com)

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''



#GET subdomain name (naem.example.com)

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


#print(get_domain_name('https://thenewboston.com/index.php'))