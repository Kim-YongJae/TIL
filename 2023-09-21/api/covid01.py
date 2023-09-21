import requests


# 공공데이터포털 -> "질병관리청_코로나19 국내발생현황 조회" 검색 -> 오픈 api 첫번째 항목 -> 활용신청
# 일반 인증키 (encoding decoding 상관없음)
service_key = '발급받은 키를 입력해주세요'
# 요청주소 + 필수항목으로 신청
url = f'http://apis.data.go.kr/1790387/covid19CurrentStatusKorea/covid19CurrentStatusKoreaJason?ServiceKey={service_key}'

resp = requests.get(url)
# print(resp.text)
# print(resp.json())
# print(type(resp.json()))

result = resp.json()['response']['result'][0]
print(f'일일확진 : {result["cnt_confirmations"]}')
print(f'일일사망 : {result["cnt_deaths"]}')
