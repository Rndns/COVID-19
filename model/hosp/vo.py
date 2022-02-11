#hosp vo
class Hosp:
    def __init__(self, yadmNm, sidoCdNm, sgguCdNm, recuClCd, addr, ratPsblYn, pcrPsblYn, mgtStaDd, XPos, XPosWgs84, YPos, YPosWgs84, ykihoEnc):
        self.yadmNm = yadmNm
        self.sidoCdNm = sidoCdNm
        self.sgguCdNm = sgguCdNm
        self.recuClCd = recuClCd
        self.addr = addr
        self.ratPsblYn = ratPsblYn
        self.pcrPsblYn = pcrPsblYn
        self.mgtStaDd = mgtStaDd
        self.XPos = XPos
        self.XPosWgs84 = XPosWgs84
        self.YPos = YPos
        self.YPosWgs84 = YPosWgs84
        self.ykihoEnc = ykihoEnc

    def __str__(self) -> str:
        data = ''
        data += '요양기관명: ' + self.yadmNm + '\n'
        data += '시도명: '+self.sidoCdNm+'\n'
        data += '시군구명: ' + self.sgguCdNm + '\n'
        data += '요양종별코드: ' + self.recuClCd + '\n'
        data += '주소: ' + self.addr + '\n'
        data += 'RAT가능여부: ' + self.ratPsblYn + '\n'
        data += 'PCR가능여부: ' + self.pcrPsblYn + '\n'
        data += '운영시작일자: ' + self.mgtStaDd + '\n'
        data += 'x좌표: ' + self.XPos + '\n'
        data += '세계지구x좌표: ' + self.XPosWgs84 + '\n'
        data += 'y좌표: ' + self.YPos + '\n'
        data += '세계지구y좌표: ' + self.YPosWgs84 + '\n'
        data += '암호화된요양기호: ' + self.ykihoEnc + '\n'
        return data