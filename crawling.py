from selenium import webdriver
from bs4 import BeautifulSoup
from khaiii import KhaiiiApi
from tf_idf import Tf_idf
import parsing
import contents_print

api = KhaiiiApi('./khaiii/khaiii/build/lib/libkhaiii.0.4.dylib', './khaiii/khaiii/build/share/khaiii')

max_depth = 1
url = 'http://hosp.ajoumc.or.kr/Index.aspx'
filter_domain='hosp.ajoumc.or.kr'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chrome/chromedriver_linux64/chromedriver',chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.set_page_load_timeout(100)

visited_pages = set()
keywords = []
df_dict={}  # total word df
homepages=[]    # total pages visited
parser_dict = {}

def getPage(tag, urls, flag):  # flag : true(contents mode) false(soup mode)
    try:
        driver.get(urls)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    except:
        return []

    if flag:
        if soup.find('html', {'lang': 'ko'}) is None:
            return []

        contents = soup.find_all(tag)
        return contents
    else:
        return soup

def getLink(urls):
    sources_tag_a = getPage('a', urls,True)
    links = []
    for link in sources_tag_a:
        if 'href' in link.attrs:
            if link.attrs['href'] not in visited_pages and 'http' in link.attrs['href'] \
            and filter_domain in link.attrs['href'] and 'pdf' not in link.attrs['href'] \
            and 'hwp' not in link.attrs['href'] and 'zip' not in link.attrs['href'] and 'login' not in link.attrs['href'] \
            and 'Login' not in link.attrs['href']:
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

def search(urls, depth,pre_parser):

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
        parser = parsing.Tag_parser(getPage('None',n,False),pre_parser)

        ''' test code
        for i in parser.contents:
            print('Title : ',i,"  contents : ",parser.contents[i])
        '''
        parser_dict[n] = parser

        contents = list(parser.contents.keys())

        for c in list(contents):
            for text_contents in list(c):
                for text in text_contents:
                    if text != '' and 'function' not in text:  # keyword = search word 판단부분
                        keyword.add(text)
                        for word in api.analyze(text):
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
        pre_parser = parser
        search(n, depth,parser)

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


search(url, 0,'')
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
    target_page_url = get_target_page(homepages, list1)

    for i in parser_dict[target_page_url].contents:
        print(i," : ",parser_dict[target_page_url].contents[i])
    print(contents_print.find_contents(parser_dict[target_page_url],list1))
print("FINISH")