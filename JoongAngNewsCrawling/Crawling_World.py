
# pip install selenium   # 세로 셋팅하는 모듈은 이렇게 표시해두는게 차후에 좋음
# pip install bs4
# pip install pymysql

from selenium import webdriver as wd

# pymysql 대신에 이젠 DBMgr 가져옴
from DBMgr import DBHelper as Db
import time
import sys
from TableInfo import TableInfo

# 사전에 필요한 정보를 로드 --> 디비혹은 쉘, 베치 파일에서 인자로 받아서 세팅
db       = Db()
main_url = [
    'https://news.joins.com/world/northame/list/', 'https://news.joins.com/world/china/list/',
    'https://news.joins.com/world/japan/list/', 'https://news.joins.com/world/eu/list/'
]

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 --> 옵션 부여하여 (프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래돌리면 --> 임시파일들이 쌓인다!! --> 템프 파일 삭제

# 사이트 접속 (get)
for url in main_url:
    driver.get(url)

    type_links = []
    news_links = []

    for page in range(1, 3): #17):
        try:
            # 자바스크립트 구동하기
            driver.get(url+'%s' % page)
            print("%s 페이지 이동" % page)

            # 기사별로 link가 두개씩 담겨있는게 있어서 최초의 링크 하나만을 가져오게 지정해줌
            lists = driver.find_elements_by_css_selector('strong.headline.mg')
            for list in lists:
                link = list.find_element_by_css_selector('a').get_attribute('href')
                news_links.append(link)
                updated = driver.find_element_by_css_selector( 'span.byline>em:nth-child(2)' ).text
                print( updated )
                ref = driver.find_element_by_css_selector( 'span.byline>em:nth-child(1)' ).text
                print( ref )
            print(news_links)

        except Exception as e1:
            print('오류',e1)

    for link in news_links:
        driver.get(link)
        time.sleep( 3 )
        type_num = 2
        title = driver.find_element_by_id( 'article_title' ).text
        print( title )
        content = driver.find_element_by_id( 'article_body' ).text
        print( content )
        updated = updated
        ref = ref
        url = link
        print(link)


        db.db_insertCrawlingData( type_num, title, updated, url, content, ref)



#종료
driver.close()
driver.quit()
# import sys
sys.exit()

