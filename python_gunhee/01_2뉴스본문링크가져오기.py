import requests
from bs4 import BeautifulSoup
import time

header = {'User-agent' : 'Mozila/2.0'}

page_num = 1

last_page = 20
day = 20211004 # ex20211005*(YYYY1005)
category = 101 #sid1 = 뉴스_전체_카테고리(경제 == 101, 사회 == 102, 세계 ==104)
classify = 259 #sid2 = 경제_카테고리 기준(증권 == 258, 금융 == 259, 부동산 == 260, 산업 == 261, 글로벌 == 262, 경제일반 == 263)


for i in range(1, last_page, 1):
    print(f"{page_num} 페이지 입니다==========================================================================================")
    response = requests.get(f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2={classify}&sid1={category}&date={day}&page={i}", headers=header)
    # response = requests.get(f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=259&sid1=101&date={day}&page={i}", headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # articless = soup.select_one("div", {"class" : "list_body newsflash_body"})
    articless = soup.select_one("#main_content")
    articles = articless.select("li")
    for article in articles:
        links = article.select("a")
        if len(links) >= 1:
            url = links[0].attrs['href']
            response = requests.get(url, headers=header)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select_one("#articleTitle")
            date = soup.select_one(".t11")
            office = soup.find('div', 'press_logo').find('img')['title']
            content = soup.select_one("#articleBodyContents")
            journalists = soup.select(".journalistcard_summary_name")
            for journalist in journalists:
                if len(journalist) >= 1:
                    print(title.text, date.text, office, journalist.text, content.text)
                    time.sleep(0.2)          
    page_num = page_num + 1
            

            

            
    

