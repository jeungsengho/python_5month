import sys                          # 파일 관련 모듈

from PyQt5.QtWidgets import *       # 윈도우 창에 관련된 위젯 모듈
from PyQt5 import uic               # Qt Designer로 만든 창 관련 모듈

import requests                               
from bs4 import BeautifulSoup as bs

form_class = uic.loadUiType("weather.ui")[0] # Qt Designer로 만든 창 읽어오기

class MyWindow(QMainWindow, form_class):        # 상속처리
    def __init__(self) :        # 생성자
        super().__init__()      # 부모의 생성자를 이용
        self.setupUi(self)      # ui 읽어오기
        self.pushButton.clicked.connect(self.btn_clicked)
                                # 단추 클릭을 인식하여 btn_clicked 매서드 호출

    def btn_clicked(self):
        html = requests.get('https://weather.naver.com/')
        soup = bs(html.text)

        self.lineEdit.setText(soup.select('strong.current')[0].text.strip()[5:])
        self.lineEdit_2.setText(soup.select('p.summary > span.weather')[0].text.strip())


app = QApplication(sys.argv)
window = MyWindow()     # 윈도우 창 객체 생성
window.show()           # 윈도우 창 띄우기
app.exec_()             # 창을 계속 열린 상태로 유지
# 원래 파이썬은 실행을 하고 종료가 된다.
# 윈도우는 특성상 창이 계속 열린 상태를 유지해야만 한다.