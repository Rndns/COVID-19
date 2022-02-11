# vaccinestatNew vo
class VaccineStat:
    def __init__(self, S_VC_DT, FIR_SUB, FIR_INC1, FIR_INC, FIR_INC_RATE, SCD_INC1, SCD_INC, SCD_INC_RATE, ADD_INC1,
                 ADD_INC, ADD_INC_RATE, ADD_SUB):
        self.S_VC_DT = S_VC_DT  # 접종일
        self.FIR_SUB = FIR_SUB  # 접종대상자
        self.FIR_INC1 = FIR_INC1  # 당일1차접종자 수
        self.FIR_INC = FIR_INC  # 1차접종 누계
        self.FIR_INC_RATE = FIR_INC_RATE  # 1차접종률
        self.SCD_INC1 = SCD_INC1  # 당일2차접종자 수
        self.SCD_INC = SCD_INC  # 2차접종 누계
        self.SCD_INC_RATE = SCD_INC_RATE  # 2차 접종률
        self.ADD_INC1 = ADD_INC1  # 당일 추가 접종자 수
        self.ADD_INC = ADD_INC  # 추가접종 누계
        self.ADD_INC_RATE = ADD_INC_RATE  # 추가접종률
        self.ADD_SUB = ADD_SUB  # 추가접종대상자

    def __str__(self) -> str:
        data = ''
        data += '접종일:' + self.S_VC_DT + '\n'
        data += '접종대상자:' + self.FIR_SUB + '\n'
        data += '당일1차접종자 수:' + self.FIR_INC1 + '\n'
        data += '1차접종 누계:' + self.FIR_INC + '\n'
        data += '1차접종률:' + self.FIR_INC_RATE + '\n'
        data += '당일2차접종자 수:' + self.SCD_INC1 + '\n'
        data += '2차접종 누계:' + self.SCD_INC + '\n'
        data += '2차 접종률:' + self.SCD_INC_RATE + '\n'
        data += '당일 추가 접종자 수:' + self.ADD_INC1 + '\n'
        data += '추가접종 누계:' + self.ADD_INC + '\n'
        data += '추가접종률:' + self.ADD_INC_RATE + '\n'
        data += '추가접종대상자:' + self.ADD_SUB + '\n'
        return data
