import model1
import datetime
from datetime import date, timedelta
import pandas as pd

now = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')
yesterday = date.today() - timedelta(1)
yesterday = datetime.datetime.strftime(yesterday,'%Y%m%d')
allBox = {
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
def checkBox(addBox):
    checkBox={"statedt":"기준일","statetime":"기준시간"}
    for i,j in addBox.items():
        checkBox[i] = j

def covid19(wantDt, checkBox):
    querySet = {
    "serviceKey":model1.key,
    "startCreateDt":wantDt[0],
    "endCreateDt":wantDt[1]
    }
    responseSet = checkBox
    CB_url = model1.CB_url
    url = model1.get_url(CB_url, querySet)

    return model1.mk_df(url, responseSet)

def now_covid():
    now = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')
    yesterday = date.today() - timedelta(1)
    yesterday = datetime.datetime.strftime(yesterday,'%Y%m%d')
    ySet = {
    "serviceKey":model1.key,
    "startCreateDt":yesterday,
    "endCreateDt":yesterday,
    }
    nSet = {
    "serviceKey":model1.key,
    "startCreateDt":now,
    "endCreateDt":now,        
    }
    box = {
    "decidecnt":"확진자 수",
    "deathcnt":"사망자 수",
    }
    CB_url = model1.CB_url
    yurl = model1.get_url(CB_url, ySet)
    nurl = model1.get_url(CB_url, nSet)
    d_ = {}
    ndf = model1.mk_df(nurl, box)
    ydf=model1.mk_df(yurl, box)
    d_['확진자 수']=int(ndf['확진자 수'])-int(ydf['확진자 수'])
    d_['사망자 수']=int(ndf['사망자 수'])-int(ydf['사망자 수'])
    return pd.DataFrame(d_, index=[now])
df = covid19([yesterday,now], allBox)
print(df)
df_now = now_covid()
print(df_now)