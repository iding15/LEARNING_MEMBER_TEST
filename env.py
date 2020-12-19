import model
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# **서버에 접근 불가 상태**
# def getId(sttn):
#     op_sttn = model.operationName["역목록"]
#     sttn_CB = model.pick_path(model.end_point,op_sttn)
#     querySet = {
#         "serviceKey":model.key,
#         "subwayStationName":sttn
#     }

#     responseSet = {
#         "subwayroutename":"노선명",
#         "subwayStationName":"지하철역명",
#         "subwaystationid":"지하철역ID"
#     }
#     url = model.get_url(sttn_CB, querySet)
#     print(url)
#     df = model.mk_df(url, responseSet)
#     return df

# if __name__ == "__main__":
#     df = getId("서울역")
#     print(df)

url = "http://subway.koreatriptips.com"

def znum(num):
    if num<10:
        return str(0)+str(num)
    if num>=10:
        return str(num)
l_href = []
for i in list(range(1,34)):
    href = "/subway-station/SES"+znum(i)+".html"
    l_href.append(url+href)

home = requests.get(url+'/subway-station.html')
houp = BeautifulSoup(home.content, "html.parser")
mhoup = houp.select(".list-unstyled")
l_hext = []
for mh in mhoup:
    l_hext.append(mh.text)
l_hext = l_hext[0].split('\n')
del l_hext[0]
del l_hext[-1]
l_hext = l_hext[0:21]
# print(l_hext)
l_info = []
for num in range(len(l_href)):
    try:
        webpage = requests.get(l_href[num])
        soup = BeautifulSoup(webpage.content, "html.parser")
    except:
        continue

    msoup = soup.select(".list-unstyled")
    l_text = []
    for ms in msoup:
        l_text.append(ms.text)

    l_text = l_text[0].split('\n')
    del l_text[0]
    del l_text[-1]

    str_chunk = str(msoup[0])
    pattern = re.compile('[\w]+[.]html')
    l_find = pattern.findall(str_chunk)

    l_id = []
    for f in l_find:
        ID = f.replace('.html','')
        l_id.append(ID)

    idInfo = {}
    for t, i in zip(l_text, l_id):
        idInfo[t] = i
    l_info.append(idInfo)

while {'': 'station'} in l_info:
    l_info.remove({'': 'station'})
# print(len(l_info))
info = {}
for h,i in zip(l_hext,l_info):
    info[h]=i

# print(info)
def showLine():
    return print(l_hext)
def searchLine(line):
    return list(info[line].keys())
def search_with_id(station):
    for h in l_hext:
        if station in searchLine(h):
            return info[h][station]

d_daily = {"평일":"01", "토요일":"02", "일요일":"03"}
d_updown = {"상행":"U", "하행":"D"}

def showDaily():
    return print(d_daily)
def showUpdown():
    return print(d_updown)

def setDaily(day):
    return d_daily[day]
def setUpdown(updown):
    return d_updown[updown]