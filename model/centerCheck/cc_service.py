import d0208_project_mini04.model.centerCheck.cc_vo as vo
import requests
import json

class centerCheckService:
    def getCenterByList(self):
        url = 'https://api.odcloud.kr/api/15077586/v1/centers?'
        page = '1'
        perPage = '1000'
        serviceKey = 'a3Sl0s2ff%2BMsnNlEPVn3zjdV6oELp8lb5pxdqY5jBvUc%2FK8HIjEDqAa9CkIY2dZx6Wswp3zqL7IHbSU%2ByhyjDA%3D%3D'
        url += 'page=' + page
        url += '&perPage=' + perPage
        url += '&serviceKey=' + serviceKey
        html = requests.get(url).text  # url에 요청
        res = json.loads(html)
        data = res['data']

        seoul = []
        for i in data:
            if i['sido'] == '서울특별시':
                seoul.append(i)
        return seoul


    def getCenterById(self, id:int):
        seoul = self.getCenterByList()
        for i in seoul:
            if i['id']==id:
                return i
