from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import psycopg2
import requests
import json
from xml.etree.ElementTree import parse
import xmltodict

connection = psycopg2.connect(
    host="127.0.0.1", dbname="kopis", user="wodydtns", password="flsdl@qkqn7", port="5432")
serviceKey = '3604a804533344128087dbc6e6f4cae9'

# year_list = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
# month_list = ['01', '02', '03', '04', '05',
#               '06', '07', '08', '09''10', '11', '12']
# stdate = []
# for i in year_list:
#     for j in month_list:
#         new_str = []
#         new_str.append(i)
#         new_str.append(j)
#         new_str = ''.join(new_str)
#         stdate.append(new_str)
# print(stdate)

try:
    url = f"http://www.kopis.or.kr/openApi/restful/prfstsTotal?service={serviceKey}&ststype=day&stdate=202207"

    request = Request(url)

    response_body = urlopen(request, timeout=60).read()

    decode_data = response_body.decode('utf-8')
    print(len(decode_data))
    xml_parse = xmltodict.parse(decode_data)
    xml_dict = json.loads(json.dumps(xml_parse))
    json_datas = xml_dict.get('prfsts')
    json_data = json_datas.get('prfst')
    print(json_data)
    cur = connection.cursor()
    cur.executemany(
        "INSERT INTO ticket_by_temp (prfdt,prfprocnt,prfdtcnt,amount,nmrs) VALUES ( %(prfdt)s, %(prfprocnt)s,%(prfdtcnt)s,%(amount)s,%(nmrs)s  )", json_data)
    connection.commit()
    connection.close()
    print('complete')
except:
    print('exception')
