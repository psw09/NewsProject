import requests
from bs4 import BeautifulSoup
import time

header = {'User-agent' : 'Mozila/2.0'}

#last_page = 10page(start=91)

page_num = 1

for i in range(1, 3, 1): #1page = 1, 2page = 11
    print(f"{page_num}페이지 입니다==================================================================================================")
    # response = requests.get(f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101#&date=%2000:00:00&page={i}", headers=header)
    response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101", headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find("ul", {"class":"type06"})
    time.sleep(0.5)
    # articles = soup.select(".type06")
    print(articles)
    # for article in articles:
    #     links = article.select("dt")
    #     print(links)


    # articles = soup.select('.info_group') #아니면 "div.info_group" #뉴스 기사 div 10개 추출
    # for article in articles:
    #     links = article.select("a.info") #리스트
    #     # print(links)
    #     if len(links) >= 2: #링크가 2개 이상이면
    #         url = links[1].attrs['href'] # 두 번째 링크의 href를 추출함
    #         # print(url)
    #         response = requests.get(url, headers=header)
    #         html = response.text
    #         soup = BeautifulSoup(html, 'html.parser')
    #         title = soup.select_one("#articleTitle") #네이버뉴스 제목
    #         date = soup.select_one(".t11") #네이버뉴스 기사작성시간
    #         office = soup.find('div', 'press_logo').find('img')['title'] #언론사 이름
    #         content = soup.select_one("#articleBodyContents") #네이뉴스 본문
    #         journalists = soup.select(".journalistcard_summary_name") #기자 이름
    #         for journalist in journalists:
    #             if len(journalist) >= 1:
    #                 print(title.text, date.text, office, journalist.text, content.text)
    #                 time.sleep(0.5)
    #                 # print(soup)
                
    # page_num = page_num + 1         
