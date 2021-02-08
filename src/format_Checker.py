import re
import datetime

def checkDate(dateInput):
    r = re.compile('\d{4}.\d{2}.\d{2}')
    # print(bool(r.match(dateInput)))
    if not r.fullmatch(dateInput):
        # print('no match')
        return False

    nums = dateInput.split('.')
    for s in nums:
        for c in s:
            if not c.isdigit():
                return False

    return True

def EndEarlier(start_date,end_date):
    start = datetime.datetime.strptime(start_date, '%Y.%M.%I')
    end = datetime.datetime.strptime(end_date, '%Y.%M.%I')

    if start > end:
        # print("Date surpassed")
        del(start)
        del(end)
        return False

    del(start)
    del(end)
    return True

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def checkFileName(name):
    if not name:
        return False

    for c in name:
        if c.isspace() or not isEnglish(c) :
            return False

    return True

def check(dic):
    keys = dic['keys'].get()
    # start_date = dic['start_date'].get()
    # end_date = dic['end_date'].get()
    file_name = dic['name'].get()

    if not keys:
        return False

    # if checkDate(start_date)==False or checkDate(end_date)==False:
    #     return False

    # if not EndEarlier(start_date,end_date):
    #     return False
    
    if not checkFileName(file_name):
        return False

    return True