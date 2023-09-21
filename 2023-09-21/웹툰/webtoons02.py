from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


url = 'https://comic.naver.com/webtoon?tab=tue'
service = webdriver.chrome.service.Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service) #드라이버를 통해 크롬 브라우저를 실행하겠다.

sleep(3)
driver.get(url) #브라우저 실행해서 url요청을 한다.

sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

li_list = soup.select('.component_wrap .item')
print(li_list)

for li in li_list:
    title = li.find('span', class_='ContentTitle__title--e3qXt').text
    star = li.find('span', class_='Rating__star_area--dFzsb').text
    print(f'{star} "{title}"')

driver.close()
