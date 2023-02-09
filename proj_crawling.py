import requests 
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 >> ")
page = pyautogui.prompt("원하는 페이지 수 : ")

for i in range(0,int(page)) :
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=32&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={i*10+1}")
    print(f"{i+1}페이지 입니다. =====================================================================================")
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    links = soup.select(".news_tit")

    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title,url)
    i+= 10