# 상품 정보를 담는 클래스
class TableInfo:
    # 맴버변수 (실제 컬럼보다는 작게 세팅했음)
    title = " "
    content = " "
    type = " "
    updated = " "
    url = " "
    ref = " "


    # 생성자
    def __init__(self, type_num, title, url, updated, ref, content):
        self.title = title
        self.content = content
        self.type_num = type_num
        self.updated = updated
        self.url = url
        self.ref = ref
