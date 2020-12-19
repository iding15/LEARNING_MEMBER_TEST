# 통계 데이터 현황

## ~~중소기업 일자리 플랫폼 채용 통계 데이터~~
~~<http://apis.data.go.kr/B190021/api/employmentInfo/employmentInfoByStdYm?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&numOfRows=10&pageNo=1&stdYm=201902>~~
-서버의 상태가 좋지 못해서 다른 데이터로 대체합니다. 04 html오류-

## ~~인천공항 국가 별 항공 통계-여객~~
~~<http://openapi.airport.kr/openapi/service/AviationStatsByAirline/getTotalNumberOfFlight?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&from_month=201405&to_month=201405&periodicity=0&pax_cargo=Y&domestic_foreign=I>~~
-SERVICE ACCESS DENIED ERROR. 99번 에러가 계속 뜹니다.-

## 코로나 현황 데이터
<http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315>
-아직 등록되지 않은 키라고 뜸 12.19, 18:11

## 지하철 시간표 데이터
<http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&subwayStationId=SUB228&dailyTypeCode=03&upDownTypeCode=U>
-진행하려고 했던 통계자료들이 정상적으로 받아와지지 않아서 지하철 시간표 데이터로
대체하겠습니다. start: 12.19, 18:13

<http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getKwrdFndSubwaySttnList?serviceKey=YGMVpil%2FAHi%2FwBtNL1n90yhai6K4kIez7xRbCUDpiYWzd4cuhNahumycXmM%2F7jWmILuERvt9hTzE1YBo%2BDnDmg%3D%3D&subwayStationName=%EC%84%9C%EC%9A%B8%EC%97%AD>
-지하철 역을 검색해서 ID를 받아오는 api의 접근 권한이 차단되어 해당 ID를 받아올 수 없음..

-대신 해당 open API를 이용해 서비스 하고 있는 다른 웹의 정보를 크롤링 해 지하철 ID와 관련한 데이터 받아옴.