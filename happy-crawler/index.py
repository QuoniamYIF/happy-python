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

def lookup(index,keyword):
    # for entry in index:
    #     if entry[0] == keyword:
    #         return entry[1]
    # return []
    if keyword in index:
        return index['keyword']
    else:
        return None

def add_to_index(index, keyword, url):
    # 使用Python字典替换原有方法
    # for entry in index:
    #     if entry[0] == keyword:
    #         entry[1].append(url)
    #         return
    # index.append([keyword, [url]])
    if keyword in index:
        index[keyword].append(url)
        # return
    else:
        index[keyword] = [url]

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

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
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append(page)
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
    return index, graph

def computer_ranks(graph):
    d = 0.8 #damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] * len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return

url = crawl_web('http://www.douban.com')
print url