# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from khaiii import KhaiiiApi

class Tag_parser :
    def __init__(self,soup):
        self.tags = []
        self.titles = {}
        self.contents = {}
        self.stopwords = ['<!','script','function','#']
        self.api = KhaiiiApi('./khaiii/khaiii/build/lib/libkhaiii.0.4.dylib', './khaiii/khaiii/build/share/khaiii')
        '''
        self.url = 'http://hosp.ajoumc.or.kr/MedicalInfo/HospitalRoomGuide.aspx'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('./chrome/chromedriver_linux64/chromedriver', chrome_options=chrome_options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(100)
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        '''

        self.recursiveChildren(soup)

    def isstopWord(self,args):
        for word in self.stopwords:
            if word in args or '\n' == args or str(type(args)) == "<class 'bs4.element.Comment'>":  # ignore comment
                return True

        return False

    def imgTagparse(self,args):
        if 'alt' in args.attrs.keys():
            return args.attrs['alt']
        else:
            return ""
    def dictvalue_to_list(self, dicts):
        res_list = []
        for v in dicts.values():
            if v is None:
                v = []
            elif str(type(v)) == "<class 'bs4.element.NavigableString'>" or str(type(v)) == "<class 'str'>":
                v = list(v.strip().split())
            res_list.append(tuple(v))

        return tuple(res_list)

    def extract_words(self,text):
        temp = []
        if text == '': return temp

        for word in self.api.analyze(text):
            for morph in word.morphs:
                if 'NN' in morph.tag:
                    temp.append(morph.lex)

        if len(temp):
            return temp


    def parents_name(self,link,tag):
        name = []
        if(type(link) == type('')) : return False
        for p in link.parents:
            name.append(p.name)

        if(set(tag) & set(name)) : return True
        else : return False




    def recursiveChildren(self,x):
        try:
            for child in x.recursiveChildGenerator():
                if self.isstopWord(child):
                    continue
                name = getattr(child, "name", None)

                if name == 'img':
                    child = self.imgTagparse(child)
                    self.tags.append(name)
                    name = None



                if name is not None:

                    if 'li' == name:
                        ##### insertion to contents dict code
                        self.titles['word_from_contents'] = self.extract_words(child.get_text().strip())
                        self.contents[self.dictvalue_to_list(self.titles)] = [child.get_text().strip()]
                        ######
                    elif 'table' == name:

                        ############  write code here . ########################
                        pass
                    else:
                        self.tags.append(name)
                else:
                    if child.isspace() or len(self.tags) == 0 or child == '':  # lear node, don't print spaces or non-tag
                        continue
                    else:
                        if self.parents_name(child, ['li','table']):
                            continue

                        if 'h' in self.tags[-1] or 'img' in self.tags[-1]:  # or 'span' in self.tags[-1]:  # append headline
                            if 'img' in self.tags[-1] and 'h' in self.tags[-2]: # img tag in headline
                                self.titles[self.tags[-2]] = child
                            elif 'h' in self.tags[-1]: # just headline
                                self.titles[self.tags[-1]] = child
                        else:
                            self.titles['word_from_contents'] = self.extract_words(child)
                            self.contents[self.dictvalue_to_list(self.titles)] = [child.strip()]  # set contents {title : contents}
                            # print(self.titles,' : ', self.contents[self.dictvalue_to_list(self.titles)])


                    if len(self.tags):
                        self.tags.pop(-1)



        except Exception as ex:
            print("error ",ex)
            return




# t = Tag_parser()

'''
for title in t.contents.keys() :
    print('title is ', title ,"contents is ", t.contents[title] )
    #print(list(title))'''