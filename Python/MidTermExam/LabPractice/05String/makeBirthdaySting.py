def makeBirthdayString(intuserId):
    userId = str(intuserId)
    year = userId[0:2]
    month = userId[2:4]
    day = userId[4:6]
    return "19"+year+'년 ' + month+'월 ' + day + '일'

print(makeBirthdayString(990914))