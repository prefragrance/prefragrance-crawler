from selenium import webdriver

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
service_obj = Service(r"/Users/hoyeon/prefragrance-crawler/chromedriver")

driver = webdriver.Chrome('/Users/hoyeon/prefragrance-crawler/chromedriver', options = chrome_options, service = service_obj)

url = 'https://www.fragrantica.com/designers/'
driver.get('https://www.fragrantica.com/')














'''
#x_path_common = ''


클릭해야할 링크 버튼 별 xPATH 정리

메인페이지 - perfume : "//*[@id="offCanvasLeft"]/ul/li[5]/a"


'A Bath Ape' : '//*[@id="main-content"]/div[1]/div[1]/div[3]/div[1]/a/text()' => 1, 1, 3, 1
'A beautiful Li //*[@id="main-content"]/div[1]/div[1]/div[3]/div[2]/a/text() => 1, 1, 3, 2
'A Dozen Roses; //*[@id="main-content"]/div[1]/div[1]/div[3]/div[3]/a/text()' => 1, 1, 3, 3

                //*[@id="brands"]/div[3]/div[1]/div[3]/h3/a
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
        
            azzaro / acteur / actuer_image xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img => 1, 1, div, 2, 1, 1, div, div, img
                                    _accord_1st_xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div => 1, 1, div, 2, 1, 2, div, div[1], div
                                    _accord_2nd_xpath : //*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div =>> 1, 1, div, 2, 1, 2, div, div[2], div
                                    .
                                    .
                                    .
                                                      ://*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[5]/div => 1, 1, div, 2, 1, 2, div, div5, div
                 
        

** 이처럼 perfume > designers > products by designer > .html page for each product
이를 바탕으로 pseudo code를 작성해보면, 

for 디자이너 링크 리스트 방문 반복문 :
    try(프로덕트의 갯수가 디자이너마다 다 다르므로 out of range 발생 시 예외 처리로 핸들링하기 위함!):
        for 프로덕트 별 html 페이지 방문 반복 :
            프로덕트의 이미지, 이름, 어코드(5개), producer 가져오기!
            
## 이때, out of range 를 예외 처리 조건으로 걸 때는 다음과 같이 작성한다!

try:
    my_list = [1, 2, 3, 4, 5]
    print(my_list[5])
    
except IndexError:
    print('Hello Error!')
        
'''


'''
designer : 

each product:
    product's name
           's img
           's brand
           's accord
            




'''

