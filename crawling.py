from selenium import webdriver
from bs4 import BeautifulSoup
from khaiii import KhaiiiApi
from tf_idf import Tf_idf
import math

api = KhaiiiApi('../khaiii/khaiii/build/lib/libkhaiii.so.0.4', '../khaiii/khaiii/build/share/khaiii')

max_depth = 4
url = 'http://sev.iseverance.com/'
filter_domain='http://sev.iseverance.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('../chrome/chromedriver_linux64/chromedriver',chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.set_page_load_timeout(5)

visited_pages = set()
keywords = []
df_dict={}  # total word df
homepages=[]    # total pages visited


def getPage(tag, urls):
    try:
        driver.get(urls)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    except:
        return []

    if soup.find('html', {'lang': 'ko'}) is None:
        return []
    contents = soup.find_all(tag)

    return contents


def getLink(urls):
    sources_tag_a = getPage('a', urls)
    links = []
    for link in sources_tag_a:
        if 'href' in link.attrs:
            if link.attrs['href'] not in visited_pages and 'http' in link.attrs['href'] \
            and filter_domain in link.attrs['href'] and 'pdf' not in link.attrs['href'] \
            and 'hwp' not in link.attrs['href'] and 'zip' not in link.attrs['href']:
                newPage = link.attrs['href']
                visited_pages.add(newPage)
                links.append(newPage)

    return links

def update_df_dict(page_df_dict,df_dict):
    for word in page_df_dict.keys():
        if word in df_dict.keys():
            df_dict[word]+=1
        else:
            df_dict[word]=1
    pass

def search(urls, depth):
    print(len(keywords),urls)
    depth += 1
    if depth > max_depth:
        return

    links = getLink(urls)
    keyword = set()
    if urls not in visited_pages:
        links.insert(0,urls)

    for n in links:
        page_norm = []
        contents = getPage('div', n)
        for c in contents:
            text_contents = c.get_text().replace('\n', ' ').replace('\xa0', ' ').strip()
            if text_contents != '' and 'function' not in text_contents:  # keyword = search word 판단부분
                keyword.add(text_contents)
                for word in api.analyze(text_contents):
                    temp = []
                    for morph in word.morphs:
                        if 'NN' in morph.tag:
                            temp.append(morph.lex)
                        if len(temp):
                            page_norm.append(temp)
        temp_cl=Tf_idf(page_norm,n)
        temp_df_dict=temp_cl.get_wordFreq_page()    # get word's tf from page
        homepages.append(temp_cl)
        update_df_dict(temp_df_dict,df_dict) # update total word's df
        keywords.append(keyword)
        search(n, depth)

def cal_tf_idf(homepages):
    for page in homepages:
        page.get_tf_idf(df_dict,len(keywords))
    pass

def get_target_page(homepages,input_words):
    m=10000
    for page in homepages:
        score=0
        for word in input_words:
            if word in page.word_rank:
                score+=page.word_rank[word]
            else:
                score+=200
        if score<m:
            m=score
            target_page=page.url
    return target_page

def file_write(homepages,df_dict):
    with open('result.txt','w') as fp:
        for page in homepages:
            fp.write(page.url)
            fp.write('\n')
            # for line in page.text:
            #     fp.write(' '.join(line))
            #     fp.write('\n')
            for x in page.sort_dict():
                fp.write(''.join('%s %s' %x))
                fp.write(' %d' %page.word_rank[x[0]])
                fp.write(' %d' %page.tf_dict[x[0]])
                fp.write(' %d' %df_dict[x[0]])
                fp.write('\n')

search(url, 0)
cal_tf_idf(homepages)
for page in homepages:
    page.get_word_rank()
file_write(homepages,df_dict)

while(1):
    list1=[]
    while(1):
        temp=input("input keywords: ")
        if temp!='exit':
            list1.append(temp)
        else:
            break
    print(get_target_page(homepages,list1))
print("FINISH")