import get_data
import requests
from urllib.parse import urlencode,unquote,quote_plus
from bs4 import BeautifulSoup
import pandas as pd
import env


main_url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&subwayStationId=SUB228&dailyTypeCode=03&upDownTypeCode=U"

end_point = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/"
operationName = {
    "역목록":"getKwrdFndSubwaySttnList",
    "출구별버스노선":"getSubwaySttnExitAcctoBusRouteList",
    "출구별시설":"getSubwaySttnExitAcctoCfrFcltyList",
    "시간표":"getSubwaySttnAcctoSchdulList"
}
# print(operationName)

def pick_path(end_point, name):
    CB_url = end_point+name
    return CB_url


CB_url = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList"
key = "YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D"
key = requests.utils.unquote(key)

querySet = {
    "serviceKey":key,
    "subwayStationId":"SUB228",
    "dailyTypeCode":"03",
    "upDownTypeCode":"U"
}
responseSet = {
    "subwaystationnm":"지하철역명",
    "arrtime":"도착시간",
    "deptime":"출발시간",
    "endsubwaystationnm":"종점지하철역명"
}

def get_url(CB_url, querySet):
    q='?'
    eq='='
    n='&'
    url=CB_url+q
    for qKey, qValue in querySet.items():
        url=url+qKey+eq+qValue+n
    url=url[:-1]

    l_key = []
    l_value = []
    for qKey, qValue in querySet.items():
        l_key.append(quote_plus(qKey))
        l_value.append(qValue)
    encoded = {}
    for key, value in zip(l_key,l_value):
        encoded[key] = value
    queryParams = q+urlencode(encoded)
    url = CB_url +queryParams
    return url

# url = main_url
# print(url)

def mk_df(url, responseSet):
    req = requests.get(url)
    # print(req.content)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    find_list = list(responseSet.keys())
    # print(find_list)

    basket = {}
    for find in find_list:
        finded_attr=soup.find_all(find)
        # print(finded_attr)
        if basket.get(find) is None:
            basket[find]=[x.text for x in finded_attr]
        else:
            basket[find]=basket[find]+[x.text for x in finded_attr]
    # print(basket)
    df = pd.DataFrame(basket)
    df = df.rename(responseSet,axis='columns')
    df = moveColumn(df, ['지하철역명','종점지하철역명','도착시간','출발시간'])
    return df

def moveColumn(df, want):
    df = df[want]
    return df

def stationTable(station, day, updown):
    querySet = {
        "serviceKey":key,
        "subwayStationId":env.search_with_id(station),
        "dailyTypeCode":env.setDaily(day),
        "upDownTypeCode":env.setUpdown(updown)
    }
    responseSet = {
        "subwaystationnm":"지하철역명",
        "arrtime":"도착시간",
        "deptime":"출발시간",
        "endsubwaystationnm":"종점지하철역명"
    }
    url = get_url(CB_url, querySet)
    df = mk_df(url, responseSet)
    return df

if __name__=="__main__":
    url = get_url(CB_url, querySet)
    df = mk_df(url, responseSet)
    
    print(df)
