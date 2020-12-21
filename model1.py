import requests
from urllib.parse import urlencode,unquote,quote_plus
from bs4 import BeautifulSoup
import pandas as pd



main_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315"

end_point = "http://openapi.data.go.kr/openapi/service/rest/Covid19/"
operationName = {
    "코로나19 감염현황":"Covid19InfStateJson"
}
# print(operationName)

def pick_path(end_point, name):
    CB_url = end_point+name
    return CB_url


CB_url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
key = "YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D"
key = requests.utils.unquote(key)

querySet = {
    "serviceKey":key,
    "numOfRows":"10",
    "pageNo":"1",
    "startCreateDt":"20200310",
    "endCreateDt":"20200315",
}
responseSet = {
    "statedt":"기준일",
    "statetime":"기준시간",
    "decidecnt":"총 확진자 수",
    "deathcnt":"총 사망자 수",
    "carecnt":"치료중 환자 수",
    "clearcnt":"격리해제 수",
    "examcnt":"검사진행 수",
    "accexamcnt":"누적 검사 수",
    "accexamcompcnt":"누적 검사 완료 수",
    "accdefrate":"누적 확진률",    
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
    
    return df

def moveColumn(df, want):
    df = df[want]
    return df

if __name__=="__main__":
    url = get_url(CB_url, querySet)
    df = mk_df(url, responseSet)
    
    print(df)
