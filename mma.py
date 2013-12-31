import requests
import re

base_url = 'http://a.mimis5.com/'
download_page = base_url + 'forumdisplay.php?fid=41&amp;page='

max_page = 2

def get_all_links():
    for i in range(1, max_page):
        list_page = requests.get(download_page + str(i))
        if list_page.status_code == 404:
            break
        items = re.findall(r'<a href="(viewthread.*?)">(.*?)</a>', list_page.text)
        for item in items:
            c_page = requests.get(base_url + item[0])
            if c_page.status_code != 404:
                ed2k_link = re.findall(r'(ed2k:.*?\|\/)', c_page.text)
                if len(ed2k_link) > 0:
                    print ed2k_link[0]


    print 'finished'

get_all_links()
