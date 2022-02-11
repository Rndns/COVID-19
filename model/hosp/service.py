import d0208_project_mini04.model.hosp.vo as vo
import requests
from bs4 import BeautifulSoup

class HospService:
    def __init__(self):
        self.url=''
        self.key = ''

    def getHosp(self):
        self.url = 'http://apis.data.go.kr/B551182/rprtHospService/getRprtHospService?'
        self.key = 'iNUFO91si7WqWFXVJxwYaYdJdCENmMLerJ0DqvFeYzvst6Qt5vMWa81VFCfGWMy4FDg5QCOkCdRytWGrX0hQaA%3D%3D'
        self.url += 'serviceKey=' + self.key
        self.url += '&pageNo=1'
        self.url += '&numOfRows=10'

        html = requests.get(self.url).text
        root = BeautifulSoup(html, 'lxml-xml')
        cnt = root.find('totalCount').text

        self.url = 'http://apis.data.go.kr/B551182/rprtHospService/getRprtHospService?'
        self.key = 'iNUFO91si7WqWFXVJxwYaYdJdCENmMLerJ0DqvFeYzvst6Qt5vMWa81VFCfGWMy4FDg5QCOkCdRytWGrX0hQaA%3D%3D'
        self.url += 'serviceKey=' + self.key
        self.url += '&pageNo=1'
        self.url += '&numOfRows=' + cnt

        html = requests.get(self.url).text
        root = BeautifulSoup(html, 'lxml-xml')
        seoul = []
        hosp = root.find_all('item')
        for i in hosp:
            sido = i.find('addr').text
            if sido.startswith('서울'):
                seoul.append(i)

        return seoul

    def getByName(self, name):
        seoul = self.getHosp()
        res = []
        for i in seoul:
            yadmNm = i.find('yadmNm').text
            if name in yadmNm:
                res.append(i)
        return res

    def getByAddr(self, sggu):
        seoul = self.getHosp()
        res = []
        for i in seoul:
            addr = i.find('addr').text
            if sggu in addr:
                res.append(i)
        return res