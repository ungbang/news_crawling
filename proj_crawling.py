import requests 
from bs4 import BeautifulSoup

keyword = input("주제 : ")
page = int(input("원하는 페이지 수 : "))


for i in range(0,page) :
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=32&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={i*10+1}")
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    links = soup.select(".news_tit") #결과는 리스트

    for link in links:
        title = link.text # 태그 안에 텍스트 요소를 가져온다.
        url = link.attrs['href'] #href의 속성값을 가져온다.
        print(title,url)
    i+= 10