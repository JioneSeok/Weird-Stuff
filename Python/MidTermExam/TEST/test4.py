import pandas as pd
IncomeTax = pd.read_csv("C:/Users/jwseo/OneDrive/바탕 화면/종합소득세_주요항목_신고_현황Ⅱ_시·군·구.csv",encoding = 'cp949')


IncomeTax['2020'] = IncomeTax['2020'].astype(int)
IncomeTax['2020.2'] = IncomeTax['2020.2'].astype(int)
IncomeTax['2020.8'] = IncomeTax['2020.8'].astype(int)

RealIncome = (IncomeTax['2020.2']+IncomeTax['2020.8'])

print(RealIncome)
