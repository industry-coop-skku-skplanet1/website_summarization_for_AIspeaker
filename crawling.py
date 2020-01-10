from selenium import webdriver
from bs4 import BeautifulSoup
from khaiii import KhaiiiApi
from tf_idf import Tf_idf


api = KhaiiiApi('../khaiii/khaiii/build/lib/libkhaiii.so.0.4', '../khaiii/khaiii/build/share/khaiii')

max_depth = 1
url = 'http://hosp.ajoumc.or.kr/HospitalGuide/ParkingInfo.aspx'

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
            if link.attrs['href'] not in visited_pages and 'http' in link.attrs['href']:
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
    print(len(keywords))

    depth += 1
    if depth > max_depth:
        return

    links = getLink(urls)
    keyword = set()
    #
    if urls not in visited_pages:
        links.insert(0,urls)
    #

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
        #
        temp_cl=Tf_idf(page_norm,n)
        temp_df_dict=temp_cl.get_wordFreq_page()    # get word's tf from page
        homepages.append(temp_cl)
        update_df_dict(temp_df_dict,df_dict) # update total word's df
        #print(n,temp_cl.tf_dict)
        #
        keywords.append(keyword)
        search(n, depth)

def cal_tf_idf(homepages):
    for page in homepages:
        page.get_tf_idf(df_dict,len(keywords))
    pass


search(url, 0)
cal_tf_idf(homepages)
f=open("result.txt",'w')
for page in homepages:
    #print(page.url,page.sort_dict())
    f.write(page.url)
    f.writelines(page.sort_dict())
f.close()
print("FINISH")