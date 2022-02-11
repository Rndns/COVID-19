import d0208_project_mini04.model.vaccine.vo as vo
import requests
import json


class vaccineService:
    def getVaccineStatDaily(self):
        url = "http://openapi.seoul.go.kr:8088/7764714f53776a643938506e576b54/json/tvCorona19VaccinestatNew/1/295/"
        html = requests.get(url).text  # url에 요청
        res = json.loads(html)
        data = res['tvCorona19VaccinestatNew']['row']
        list = []

        for i in data:
            list.append(vo.VaccineStat(i['S_VC_DT'], int(i['FIR_SUB']), int(i['FIR_INC1']), int(i['FIR_INC']), i['FIR_INC_RATE'], int(i['SCD_INC1']),
            int(i['SCD_INC']), i['SCD_INC_RATE'], int(i['ADD_INC1']), int(i['ADD_INC']), i['ADD_INC_RATE'], int(i['ADD_SUB'])))

        return list





        # type = data['boxofficeType']
        # date = data['showRange']
        # list = data['dailyBoxOfficeList']
        # res = []
        # for i in list:
        #     res.append(
        #         vo.VaccineStat(type, date, i['S_VC_DT'], i['FIR_SUB'], i['FIR_INC1'], i['FIR_INC'], i['FIR_INC_RATE'], i['SCD_INC1'],
        #                        i['SCD_INC'], i['SCD_INC_RATE'], i['ADD_INC1'], i['ADD_INC'], i['ADD_INC_RATE'], i['ADD_SUB']))
        #
        # return res






        # for p in param:
        #     self.url += p
        # html = requests.get(self.url).text
        # res = json.loads(html)
        # print(date)
        # print(html)
        # data = res['VaccineStatResult']
        # type = data['VaccineStatType']
        # list = data['vaccineStatList']
        # res = []
        #
        # for v in list:
        #     res.append(
        #         vo.VaccineStat(type, date, v['S_VC_DT'], v['FIR_SUB'], v['FIR_INC1'], v['FIR_INC'], v['FIR_INC_RATE'], v['SCD_INC1'],
        #                        v['SCD_INC'], v['SCD_INC_RATE'], v['ADD_INC1'], v['ADD_INC'], v['ADD_INC_RATE'], v['ADD_SUB']))
        #
        # return res

