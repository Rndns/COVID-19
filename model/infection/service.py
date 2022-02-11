import d0208_project_mini04.model.infection.vo as vo
import requests
import json


class KoreaService:
    def __init__(self):
        self.url = ''

    def getKoreaInfo(self, start, end):
        self.url = 'http://openapi.seoul.go.kr:8088/447552726d62696238376b6c795167/json/TbCorona19CountStatus/'
        self.url += start + '/' + end + '/'
        html = requests.get(self.url).text
        res = json.loads(html)
        a = res['TbCorona19CountStatus']
        list = a['row']
        datas = []
        for i in list:
            datas.append(
                vo.CovidInfection(i['T_DT'], i['T_HJ'], i['N_HJ'], i['TY_CARE'], i['RECOVER'], i['DEATH']))

        return datas


class SeoulService:
    def getSeoulInfo(self, start, end):
        self.url = 'http://openapi.seoul.go.kr:8088/447552726d62696238376b6c795167/json/TbCorona19CountStatus/'
        self.url += start + '/' + end + '/'
        html = requests.get(self.url).text
        res = json.loads(html)
        a = res['TbCorona19CountStatus']
        list = a['row']
        datas = []
        for i in list:
            datas.append(
                vo.CovidInfectionDetail(i['S_DT'], i['S_HJ'], i['SN_HJ'], i['S_CARE'], i['S_RECOVER'], i['SN_RECOVER'], i['S_DEATH']))
        return datas


class RegionService:
    def getRegionInfo(self, date):
        self.url = 'http://openapi.seoul.go.kr:8088/447552726d62696238376b6c795167/json/TbCorona19CountStatusJCG/1/1/'
        self.url += date
        html = requests.get(self.url).text
        res = json.loads(html)
        a = res['TbCorona19CountStatus']
        list = a['row']
        datas = []
        for i in list:
            datas.append(
                vo.CovidInfection(i['S_DT'], i['S_HJ'], i['SN_HJ'], i['S_CARE'], i['S_RECOVER'], i['SN_RECOVER'], i['S_DEATH']))
        return datas
