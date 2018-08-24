# 디비 처리, 연결, 헤제, 검색어 가져오기, 데이터 삽입

import pymysql as my

class DBHelper:
    '''
    맴버변수: 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    맴버 함수
    '''
    def db_init(self):
        self.conn = my.connect(
                            host='localhost',
                            user='root',
                            password='1234',
                            db='Newsdb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)
    def db_free(self):
        if self.conn:
            self.conn.close


    def db_insertCrawlingData( self, type_num, title, updated, url, content, ref):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `news` 
            (type_num, title, updated, url, content, ref)
              values(%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (type_num, title, updated, url, content, ref))
        self.conn.commit()

# 디비쪽 확인하고 싶다면
# 단독으로 수행시에만 작동 --> 테스트코드를 삽입해서 사용 --> 메인에서 다 끌어다 쓸떄는 이부분이 작동 안됨
if __name__ =='__main__':
    db=DBHelper()
    # print( db.db_selectKeyword())
    print( db.db_insertCrawlingData('1', '2', '3', '4', '5', '6'))
    db.db_free()
