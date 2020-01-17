# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver


class Tag_parser :
    def __init__(self):
        self.tags = []
        self.titles = {}
        self.contents = {}
        self.stopwords = ['<!','script','function','#']
        ###
        self.url = 'http://hosp.ajoumc.or.kr/MedicalInfo/LeaveHospitalGuide.aspx'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('./chrome/chromedriver_linux64/chromedriver', chrome_options=chrome_options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(5)
        driver.get(self.url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        self.recursiveChildren(soup)

    def isstopWord(self,args):
        for word in self.stopwords:
            if word in args or '\n' == args or str(type(args)) == "<class 'bs4.element.Comment'>":
                return True

        return False

    def imgTagparse(self,args):
        return args.attrs['alt']

    def recursiveChildren(self,x):
        for child in x.recursiveChildGenerator():
            if self.isstopWord(child):
                continue
            name = getattr(child, "name", None)

            if name == 'img':
                child = self.imgTagparse(child)
                name = None


            if name is not None:
                self.tags.append(name)
            else:
                if child.isspace() or len(self.tags) == 0 : # lear node, don't print spaces or non-tag
                    continue
                else:
                    if 'h' in self.tags[-1]:  # or 'span' in self.tags[-1]:  # append headline
                        self.titles[self.tags[-1]] = child
                    else:
                        if str(self.titles.values()) in self.contents.keys():  # to protect dict from overlapping
                            self.contents[str(self.titles.values())] += child
                        else:
                            self.contents[str(self.titles.values())] = child  # set contents {title : contents}
                if len(self.tags):
                    self.tags.pop(-1)


    def h_tag_parser(self):
        pass


t = Tag_parser()

for title in t.contents :
    print('title is ', title ,"contents is ", t.contents[title] )
