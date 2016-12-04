def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_next_target(page):
    start_link = page.find('<a href=') 
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
    
def get_all_links(page):
    urlList = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            urlList.append(url)
            page = page[endpos:]
        else: 
            return urlList

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            union(tocrawl, get_all_links(get_page(page)))
    return crawled

url = crawl_web('http://www.douban.com')
print url