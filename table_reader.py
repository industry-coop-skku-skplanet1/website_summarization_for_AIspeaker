from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import lxml.html as lh
import pandas as pd
import numpy as np
from itertools import product
from khaiii import KhaiiiApi
import gensim

model=gensim.models.Word2Vec.load('./ko.bin')
api = KhaiiiApi('../khaiii/khaiii/build/lib/libkhaiii.so.0.4', '../khaiii/khaiii/build/share/khaiii')

def table_to_2d(table_tag):
    rowspans = [] 
    rows = table_tag.find_all('tr')

    colcount = 0
    for r, row in enumerate(rows):
        cells = row.find_all(['td', 'th'], recursive=False) 
        colcount = max(
            colcount,
            sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans)) 
        rowspans += [int(c.get('rowspan', 1)) or len(rows) - r for c in cells]
        rowspans = [s - 1 for s in rowspans if s > 1]

    table = [[None] * colcount for row in rows]


    rowspans = {}
    for row, row_elem in enumerate(rows):
        span_offset = 0
        for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
            col += span_offset
            while rowspans.get(col, 0):
                span_offset += 1
                col += 1
            rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
            colspan = int(cell.get('colspan', 1)) or colcount - col
            span_offset += colspan - 1
            value = cell.get_text().strip().replace('\xa0','').replace('\n','').replace('\r','').replace(',','')
            for drow, dcol in product(range(rowspan), range(colspan)):
                try:
                    table[row + drow][col + dcol] = value
                    rowspans[col + dcol] = rowspan
                except IndexError:
                    pass

        rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}

    return table

def table_parser(table):
    temp_table=[]
    for row in table:
        temp_row=[]
        for block in row:
            temp_block=[]
            # 1
            # try:
            #     for word in api.analyze(block):
            #         for morph in word.morphs:
            #             if 'NN' in morph.tag:
            #                 temp_block.append(morph.lex)
            # except:
            #     temp_block.append(' ')
            # 2
            if block is not None:
                block=block.split(' ')
            else:
                block=[]
            for word in block:
                temp_block.append(word)
            temp_row.append(temp_block)
        temp_table.append(temp_row)
    return temp_table

def r_or_c(table):
    #
    if not table:
        temp_table=[]
        return temp_table
    #
    r_score_table=[]
    c_score_table=[]
    #get row similarity score
    for row in table:
        temp_row=[0 for i in range(len(row))]
        for b in range(len(row)):
            block=row[b]
            score=0
            for b1 in range(b+1,len(row)):
                block1=row[b1]
                for w in range(len(block)):
                    word=block[w]
                    for w1 in range(len(block1)):
                        word1=block1[w1]
                        try:
                            score=model.wv.similarity(word,word1)
                            if score>temp_row[b]:
                                temp_row[b]=score
                            if score>temp_row[b1]:
                                temp_row[b1]=score
                        except:
                            m=0
        r_score_table.append(temp_row)
    # print("===row scores===")
    # print(r_score_table)
    #get col similarity score
    for col in range(len(table[0])):
        temp_col=[0 for i in range(len(table))]
        for b in range(len(table)):
            block=table[b][col]
            score=0
            for b1 in range(b+1,len(table)):
                block1=table[b1][col]
                for w in range(len(block)):
                    word=block[w]
                    for w1 in range(len(block1)):
                        word1=block1[w1]
                        try:
                            score=model.wv.similarity(word,word1)
                            if score>temp_col[b]:
                                temp_col[b]=score
                            if score>temp_col[b1]:
                                temp_col[b1]=score
                        except:
                            pass
        c_score_table.append(temp_col)

    # print("===col scores===")        
    # print(c_score_table)
    # get row and col total similarity score
    total=0
    b_count=0
    for row in r_score_table:
        for block in row:
            if block!=0:
                total+=block
                b_count+=1
    if b_count!=0:
        r_score=total/b_count
    else:
        r_score=0

    total=0
    b_count=0
    for col in c_score_table:
        for block in col:
            if block!=0:
                total+=block
                b_count+=1
    if b_count!=0:
        c_score=total/b_count
    else:
        c_score=0

    # if r_score>c_score:
    #     print("this table is col-base")
    # else:
    #     print("this table is row-base")


    return table_2_list(table,r_score<=c_score)

def table_2_list(table,row_base):
    temp_table=[]
    if row_base:
        for row in table:
            temp_row=[]
            for block in row:
                temp_row.append(' '.join(block))
            temp_table.append('/'.join(temp_row))
    else:
        for col in range(len(table[0])):
            temp_col=[]
            for row in table:
                temp_col.append(' '.join(row[col]))
            temp_table.append('/'.join(temp_col))
    return temp_table

# def get_all_tables(url):
#     tables=[]
#     html=urlopen(url)
#     bsObject=BeautifulSoup(html,"html.parser")
#     for conv in bsObject.find_all('table'):
#         temp_table=table_parser(table_to_2d(conv))
#         table=r_or_c(temp_table)
#         tables.append(table)
#     return tables

def get_all_tables(soup):
    tables=[]
    try:
        for conv in soup.find_all('table'):
            temp_table=table_parser(table_to_2d(conv))
            table=r_or_c(temp_table)
            tables.append(table)
        return tables
    except Exception as ex:
        print(ex)


#print(get_all_tables("http://hosp.ajoumc.or.kr/MedicalInfo/VisitionGuide.aspx"))

# html=urlopen("http://hosp.ajoumc.or.kr/MedicalInfo/VisitionGuide.aspx")
# bsObject=BeautifulSoup(html,"html.parser")

# count=0
# for conv in bsObject.find_all('table'):
#     count+=1
#     print(count,"th table==")
#     table=table_parser(table_to_2d(conv))
#     print(r_or_c(table))
#     print("\n")



    #t1=np.array(table_to_2d(conv))
    #print(t1)
	#df = pd.DataFrame(t1[1:,1:], index=t1[1:,0], columns=t1[0,1:])
	#print(df)