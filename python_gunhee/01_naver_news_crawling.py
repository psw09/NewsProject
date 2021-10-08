import requests
from bs4 import BeautifulSoup
import time

header = {'User-agent' : 'Mozila/2.0'}

date = 20211007 # ex20211005*(YYYY1005)
category = 101 #sid1 = 뉴스_전체_카테고리(경제 == 101, 사회 == 102, 세계 ==104)
classify = 259 #sid2 = 경제_카테고리 기준(증권 == 258, 금융 == 259, 부동산 == 260, 산업 == 261, 글로벌 == 262, 경제일반 == 263)
last_page_num = 1 #마지막 페이지 정보를 위한 변수
url = (f"https://news.naver.com/main/list.naver?mode=LS2D&sid2={classify}&sid1={category}&mid=shm&date={date}&page=1")

###네이버 뉴스의 마지막 페이지 자동 추출###
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
entire_buttons = soup.select_one(".paging") #<div> class="paging" == 페이지 번호 정보가 담긴 class
next_buttons = entire_buttons.select("a.next") #페이지 정보가 담긴 <a>중에서도 "다음"이라는 정보가 담긴 <a> class="next nclicks"를 select함
#next_button 에는 다음_page 넘어가는 url(1개) 담겨있음
normal_buttons = entire_buttons.select("a") #10페이지 미만의 기사를 체크하기 위한 변수

while True: #while문의 기본 조건을 True로 설정함
    if len(next_buttons) >= 1: #"다음_page"가 하나라도 있으면 while_if문을 돈다
        last_page_num = last_page_num + 10 #한_page에 10개씩 목록이 설정되어 있기 때문에 + 10을 설정함
        for next_button in next_buttons: #attrs를 불러오기 위해서는 for문 필요
            last_page_url = next_button.attrs['href'] #last_ulr == 11page의 url 정보가 담겨있음
            response = requests.get(f"https://news.naver.com/main/list.naver{last_page_url}", headers=header)
            soup = BeautifulSoup(response.text, "html.parser")
            entire_buttons = soup.select_one(".paging") #entire_buttons에는 11~21페이지의 url <a>가 담겨있음
            next_buttons = entire_buttons.select("a.next") #여기서 next_button에 <a> class="next nclicks"가 담겨있으면 if로, 없으면 elif 이동
    elif len(next_buttons) == 0 and int(last_page_num) >= 10: #10page이상일 때는 while의 if문을 돌고 이곳으로 들어와야하므로, int(last_page_num) >= 10이라는 조건을 주었음
        last_buttons = entire_buttons.select("a")
        last_page_num = last_page_num + len(last_buttons)
        break
    elif len(next_buttons) == 0 and len(normal_buttons) >= 1:
        last_page_num = len(normal_buttons) + 1
        break
# print(last_page_num) #마지막 페이지의 수를 last_page_num에 담음

##네이버 뉴스의 본문 추출###
page_num = 1
for i in range(1, last_page_num, 1): #마지막 페이지를 자동추출하고 그것을 last_page_num에 넣어줌
    print(f"{page_num} 페이지 입니다==========================================================================================")
    response = requests.get(f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2={classify}&sid1={category}&date={date}&page={i}", headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    entire_articles = soup.select_one("#main_content")
    articles = entire_articles.select("li")
    for article in articles:
        links = article.select("a")
        if len(links) >= 1:
            url = links[0].attrs['href']
            response = requests.get(url, headers=header)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            news_title = soup.select_one("#articleTitle")
            news_date = soup.select_one(".t11")
            news_press = soup.find('div', 'press_logo').find('img')['title']
            news_content = soup.select_one("#articleBodyContents")
            journalists = soup.select(".journalistcard_summary_name")
            for journalist in journalists: #뉴스기사 중에 속보기사는 기자의 제목이 없는 경우가 있음, 따라서 기자가 없는 경우는 crawling에서 배제시킴 
                if len(journalist) >= 1:
                    print(news_title.text, news_date.text, news_press, journalist.text, news_content.text)
                    time.sleep(0.2)          
    page_num = page_num + 1
            

            

            
    

