class CovidInfection:
    def __init__(self, T_DT, T_HJ, N_HJ, TY_CARE, RECOVER, DEATH):
        self.T_DT = T_DT
        self.T_HJ = T_HJ
        self.N_HJ = N_HJ
        self.TY_CARE = TY_CARE
        self.RECOVER = RECOVER
        self.DEATH = DEATH

    def __str__(self):
        data = '날짜 : ' + self.T_DT + '\n'
        data += '총 확진 : ' + self.T_DT + '명\n'
        data += '추가 확진 : ' + self.T_DT + '명\n'
        data += '치료중 : ' + self.T_DT + '명\n'
        data += '퇴원 : ' + self.T_DT + '명\n'
        data = '사망 : ' + self.T_DT + '명\n'
        return data


class CovidInfectionDetail:
    def __init__(self, S_DT, S_HJ, SN_HJ, S_CARE, S_RECOVER, SN_RECOVER, S_DEATH):
        self.S_DT = S_DT
        self.S_HJ = S_HJ
        self.SN_HJ = SN_HJ
        self.S_CARE = S_CARE
        self.S_RECOVER = S_RECOVER
        self.SN_RECOVER = SN_RECOVER
        self.S_DEATH = S_DEATH

    def __str__(self):
        data = '날짜 : ' + self.S_DT + '\n'
        data += '총 확진 : ' + self.S_HJ + '명\n'
        data += '추가 확진 : ' + self.SN_HJ + '명\n'
        data += '치료중 : ' + self.S_CARE + '명\n'
        data += '총 퇴원 : ' + self.S_RECOVER + '명\n'
        data += '추가 퇴원 : ' + self.SN_RECOVER + '명\n'
        data += '사망 : ' + self.S_DEATH + '명\n'
        return data

