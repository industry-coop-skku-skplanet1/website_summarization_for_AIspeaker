import parsing
from bs4 import BeautifulSoup
from selenium import webdriver
from khaiii import KhaiiiApi
import copy

def find_contents(parser,search_word):
    api = KhaiiiApi('../khaiii/khaiii/build/lib/libkhaiii.so.0.4', '../khaiii/khaiii/build/share/khaiii')
    result = ""

    search_word_with_NLP = copy.deepcopy(search_word)

    for str_sword in search_word:
        try:
            analyzed_word=api.analyze(str_sword)
        except:
            continue
        for word in analyzed_word:
            for morph in word.morphs:
                if 'NN' in morph.tag:
                    search_word_with_NLP.append(morph.lex)



    search_word_with_NLP = tuple(search_word_with_NLP)

    for title_line in parser.contents:
        titles = tuple_extract(title_line)
        if set(titles) & set(search_word_with_NLP) == set(search_word_with_NLP):
            result += str(parser.contents[title_line])+'\n'

    if result == "":
        return "Fail to Find"
    else:
        return result


def tuple_extract(argt):
    result = []
    for x_tuple in argt:
        if type(x_tuple) == type(""):
            result.append(x_tuple)  # 1st-dimension tuple
        else:
            for word in x_tuple: # 2nd-or high dimension tuple
                result.append(word)

    return result


'''
url = 'http://www.snuh.org/guide/convenience/internal/conveninList.do'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('../chrome/chromedriver_linux64/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.set_page_load_timeout(100)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
parser = parsing.Tag_parser(soup)
'''
