from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('Users/hoyeon/crawler_test/chromedriver')

url = 'https://www.fragrantica.com/designers/'
driver.get(url)
time.sleep(1) # 셀레니움은 브라우저를 직접 실행하고 어떤 버튼을 클릭하는 등, 사용자의 행동을 재현하는 패키지이다. 따라서 url로 명시된 페이지가 로드될 때 까지 기다리는 시간을 준 것.

'''
클릭해야할 링크 버튼 별 xPATH 정리

메인페이지 - perfume : "//*[@id="offCanvasLeft"]/ul/li[5]/a"


'A Bath Ape' : '//*[@id="main-content"]/div[1]/div[1]/div[3]/div[1]/a/text()' => 1, 1, 3, 1
'A beautiful Life Brand' : //*[@id="main-content"]/div[1]/div[1]/div[3]/div[2]/a/text() => 1, 1, 3, 2
'A Dozen Roses; : '//*[@id="main-content"]/div[1]/div[1]/div[3]/div[3]/a/text()' => 1, 1, 3, 3

.
.
.
designer_link =             : //*[@id="main-content"]/div[1]/div[1]/div[3]/div[489]/a' => 1, 1, 3, 489, a
designer_name = 'Azzaro' : '//*[@id="main-content"]/div[1]/div[1]/div[3]/div[489]/a/text()' => 1, 1, 3, 489, a, text()
designers/designer_name.lower()+'.html' => move to 
designer_image : //*[@id="main-content"]/div[1]/div[1]/div[3]/div[489]/img => 1, 1, 2, 489 + /img              | - range(1, 490)

                                                                                                               
        azzaro / actuer link xpath : //*[@id="brands"]/div[3]/div[1]/div[3]/h3/a => 3, 1, 3, a                 |     
        azzaro / azzaro 9 link xpath : //*[@id="brands"]/div[4]/div[1]/div[3]/h3/a => 4, 1, 3, a               | - range(1, )
                                    : //*[@id="brands"]/div[5]/div[1]/div[3]/h3/a => 5, 1, 3, a                |
                                    
                                    .
                                    .
                                    .
                                    
        azzaro / wated tonic  xpath : //*[@id="brands"]/div[116]/div[1]/div[3]/h3/a => 116, 1, 3, a
        
            azzaro / acteur / actuer_image xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img => 1, 1, 2, 1, 1, div, div, img
                                    _accord_1st_xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div => 1, 1, 2, 1, 2, div, div[1], div
                                    _accord_2nd_xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div =>> 1, 1, 2, 1, 2, div, div[2], div
                                    .
                                    .
                                    .
                                                      ://*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/div => 1, 1, 2, 1, 2, div, div5, div
                 
        

** 이처럼 perfume > designers > products by designer > .html page for each product
이를 바탕으로 pseudo code를 작성해보면, 

for 디자이너 링크 리스트 방문 반복문 :
    try(프로덕트의 갯수가 디자이너마다 다 다르므로 out of range 발생 시 예외 처리로 핸들링하기 위함!):
        for 프로덕트 별 html 페이지 방문 반복 :
            프로덕트의 이미지, 이름, 어코드(5개), producer 가져오기!
        
'''
