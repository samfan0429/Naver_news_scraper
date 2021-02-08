import requests
from bs4 import BeautifulSoup
import math
import re
import itertools
import output

def printList(work):
    for s in work:
        print(s)

class Scraper():
    def __init__(self):
        self.active = False

    def activate(self,UInput):
        self.active = True
        # self.printInfo(UInput)
        url = UInput.searchKey # .split(' ')
        # print(url)
        # start = UInput.start_date
        # end = UInput.end_date
        name = UInput.name

        out_file = open(name+'.tsv', 'w',-1,'utf-8')
        out_file.write('Title\t Company\t Date \t URL\n')

        hasNext = True

        raw = requests.get(url)
        

        while hasNext:   
            raw = requests.get(url)
            html = BeautifulSoup(raw.text, "html.parser")
            articles = html.find_all('div', attrs={'class':'news_wrap api_ani_send'})

            # print(articles)
            for ar in articles:
                # 제목 값
                title = ar.find('a', attrs={'class':'news_tit'})['title']
                # print(title)

                # 언론사 값
                sourceVal = ar.find('a', attrs={'class':'info press'})
                if sourceVal is None:
                    sourceVal = ar.find('span', attrs={'class':'info press'})
                source = sourceVal.text
                # print(source)

                # 등록일 값
                date = ar.find('span', attrs={'class':'info'}).text
                # print(date)

                # 링크 값
                href = ar.find('a', attrs={'class':'news_tit'})['href']

                res = (title, source, date,href)
                out_file.write('\t'.join(res))
                out_file.write('\n')

            nextUrl = html.find('a', attrs={'class':'btn_next'})
            if nextUrl['aria-disabled']=='false':
                url='https://search.naver.com/search.naver'+nextUrl['href']
            else:
                hasNext = False
        
        self.active=False

    def formURL(self,search):
        url = 'https://search.naver.com/search.naver?&where=news&query='
        # for i in range(len(search)):
        #     url+=search[i]
        #     if not i==len(search)-1:
        #         url+='+'
        return url+search

    def printInfo(self,UInput):
        print(UInput.searchKey)
        print(UInput.start_date)
        print(UInput.end_date)
        print(UInput.name)