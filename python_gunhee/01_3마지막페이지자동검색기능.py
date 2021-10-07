import requests
from bs4 import BeautifulSoup
import time

header = {'User-agent' : 'Mozila/2.0'}

last_page = 20
# i = 1 #초기 paged의 번호
day = 20210929 # ex20211005*(YYYY1005)
category = 101 #sid1 = 뉴스_전체_카테고리(경제 == 101, 사회 == 102, 세계 ==104)
classify = 259 #sid2 = 경제_카테고리 기준(증권 == 258, 금융 == 259, 부동산 == 260, 산업 == 261, 글로벌 == 262, 경제일반 == 263)
page_num = 0 #마지막 페이지 정보를 위한 변수

url = (f"https://news.naver.com/main/list.naver?mode=LS2D&sid2={classify}&sid1={category}&mid=shm&date={day}&page=1")

result = requests.get(url, headers=header)
soup = BeautifulSoup(result.text, "html.parser")
entire_buttons = soup.select_one(".paging") #<div> class="paging" == 페이지 번호 정보가 담긴 class
next_buttons = entire_buttons.select("a.next") #페이지 정보가 담긴 <a>중에서도 "다음"이라는 정보가 담긴 <a> class="next nclicks"를 select함
#next_button 에는 다음_page 넘어가는 url(1개) 담겨있음
minimum_buttons = entire_buttons.select("a") #10페이지 미만의 기사를 체크하기 위한 변수

while True: #while문의 기본 조건을 True로 설정함
    if len(next_buttons) >= 1: 
        page_num = page_num + 10 #한_page에 10개씩 목록이 설정되어 있기 때문에 + 10을 설정함
        for next_button in next_buttons: #attrs를 불러오기 위해서는 for문 필요
            last_url = next_button.attrs['href'] #last_ulr == 11page의 url 정보가 담겨있음
            result = requests.get(f"https://news.naver.com/main/list.naver{last_url}", headers=header)
            soup = BeautifulSoup(result.text, "html.parser")
            entire_buttons = soup.select_one(".paging") #entire_buttons에는 11~21페이지의 url <a>가 담겨있음
            next_buttons = entire_buttons.select("a.next") #여기서 next_button에 <a> class="next nclicks"가 담겨있으면 if로, 없으면 elif 이동
    elif len(next_buttons) == 0 and int(page_num) >= 10:
        last_buttons = entire_buttons.select("a")
        page_num = page_num + len(last_buttons)
        break
    elif len(next_buttons) == 0 and len(minimum_buttons) >= 1:
        page_num = len(minimum_buttons) + 1
        break
    
        
print(page_num) 
