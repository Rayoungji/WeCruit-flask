from flask import Flask,request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

co_text = []
info_text = []
link_text = []
sDesc_text = []
side_text = []

@app.route('/')
def index():
    return "This is index page"

@app.route('/scrap')
def getInfo():
    temp = request.args.get('page')
    result = scraping(temp);
    return result


def scraping(temp):
    print(temp)
    request_parameter = {'page': temp}
    url = "http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0"
    response = requests.get(url, params=request_parameter)
    print(response.url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    cos = soup.select('div.filterListArea > ul.filterList > li > div.co > div.coTit > a')
    print(len(cos))
    for co in cos:
        co_text.append(co.text)

    infos = soup.select('div.filterListArea > ul.filterList > li > div.info > div.tit > a')
    print(len(infos))
    for info in infos:
        info_text.append(info['title'])

    links = soup.select('div.filterListArea > ul.filterList > li > div.info > div.tit > a')
    print(len(links))
    for link in links:
        link_text.append(link['href'])

    sDescs = soup.select('div.filterListArea > ul.filterList > li > div.sDesc > span')
    print(len(sDescs))
    for sDesc in sDescs:
        sDesc_text.append(sDesc.text)

    sides = soup.select('div.filterListArea > ul.filterList > li > div.side')
    print(len(sides))
    for side in sides:
        date_cleansing(side)

    result = {"enterprise": co_text, "announcement": info_text, "link": link_text, "education": sDesc_text, "deadline": side_text}
    return result

def date_cleansing(side):
    side = side.text.split("\n")[3]
    side_text.append(side)
