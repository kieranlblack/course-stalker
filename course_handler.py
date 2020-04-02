from config import config
from bs4 import BeautifulSoup
import requests

url = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched'

def _get_page(params):
    req = requests.get(url, params)

    if req.status_code != 200:
        print('Something went wrong getting the page')

    return BeautifulSoup(req.content, 'html5lib')

def get_seat_counts(course):
    soup = _get_page({
        "term_in": config['term'],
        "crn_in": course.crn
    })

    tds = soup.find_all('td', {"class": "dddefault"})[1:7]

    if len(tds) <= 0:
        return (-1, -1, -1, -1, -1, -1)

    tds_text = list(map(lambda x: x.get_text(), tds))
    
    return (tds_text[2], tds_text[0], tds_text[1], tds_text[5], tds_text[3], tds_text[4])

def update_class_info(course):
    soup = _get_page({
        "term_in": config['term'],
        "crn_in": course.crn
    })

    headers = soup.find_all('th', {"class": "ddlabel"})[:1]
    headers_text = headers[0].get_text()
    headers_split = headers_text.split('-')

    course.title = headers_split[2][1:-1]
    course.section = headers_split[3][1:]
