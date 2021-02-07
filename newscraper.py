import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import re
import itertools

def debugDic(dic):
    vals = dic.values()
    for v in vals:
        print(v.get())

def scrape(dic):
    debugDic(dic)
    # out_file = open('kakao.tsv', 'w',-1,'utf-8')
    # out_file.write('Title\t Company\t Date\n')

    # urlPrefix = 'https://search.naver.com/search.naver?&where=news&query=%EC%B9%B4%EC%B9%B4%EC%98%A4%20%22%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%84%BC%ED%84%B0%22&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=3660000651041&nso=so:r,p:all,a:all&mynews=0&related=1&start='
    # urlSuffix= '1&refresh_start=0'
    # params = {
    # "where": 'news',

    # # 네이버 기사 검색 값
    # "query": '매틱 네트워크 스테이킹',

    # # 페이지네이션 값
    # "start": 0,

    # # "nso": 'so:r,p:1y,a:all'
    # }

    # # nso: so: r, p: 1y, a: all -> 최근 1년
    # # nso: so: r, p: 6m, a: all -> 최근 6개월
    # # nso: so: r, p: 1d, a: all -> 1일
    # # 없으면 전체 검색

    # # headers={'User-Agent': 'Mozilla/5.0'} -> 안티 크롤링 회피
    # # raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, params=params)
    # # html = BeautifulSoup(raw.text, "html.parser")

    # # # 검색결과 html body
    # # articles = html.select("#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li")

    # # # 전체 기사 수
    # # # totalCount = html.select("#main_pack > div.api_sc_page_wrap > div > div")#[0].text.split(' / ')[1][:-1]
    # # parsed = html.find(lambda tag: tag.name == 'div' and tag.get('class') == ['sc_page_inner'])
    # # children = parsed.findChildren("a" , recursive=False)
    # # for child in children:
    # #     print(child)
    # # print(parsed)
    # counter = 0

    # for i in range(100):
    #     url = urlPrefix
    #     if i == 0:
    #         url+=urlSuffix
    #     else:
    #         url+=(str(i)+urlSuffix)    
    #     raw = requests.get(url)
    #     html = BeautifulSoup(raw.text, "html.parser")
    #     articles = html.find_all('div', attrs={'class':'news_wrap api_ani_send'})

    #     # print(articles)
    #     for ar in articles:
    #         counter+=1
    #         # 제목 값
    #         title = ar.find('a', attrs={'class':'news_tit'})['title']
    #         # print(title)

    #         # # 검색된 기사의 url을 가져와서 다시 html을 get
    #         # articleUrl = ar.find("a")["href"]
    #         # innerRaw = requests.get(articleUrl, headers={'User-Agent': 'Mozilla/5.0'})

    #         # # 가져온 기사 html중 '기사', '@' string을 모두 가져온다
    #         # innerHtml = BeautifulSoup(innerRaw.text, "html.parser")
    #         # reporter = innerArticles = innerHtml(text=re.compile("기자"))
    #         # reporterEmail = innerArticles = innerHtml(text=re.compile("@"))

    #         # # 언론사 값
    #         sourceVal = ar.find('a', attrs={'class':'info press'})
    #         if sourceVal is None:
    #             sourceVal = ar.find('span', attrs={'class':'info press'})
    #         source = sourceVal.text
    #         print(source)

    #         # # 등록일 값
    #         date = ar.find('span', attrs={'class':'info'}).text
    #         # print(date)

    #         res = (title, source, date)
    #         out_file.write('\t'.join(res))
    #         out_file.write('\n')