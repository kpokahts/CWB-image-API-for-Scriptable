import requests
import re

def get_radar():
    res = requests.get('https://www.cwb.gov.tw/Data/js/obs_img/Observe_radar_rain.js')
    content = res.text
    image_url = re.findall(r'([\w\/]+.png)', content)[0]
    full_url = f'https://www.cwb.gov.tw/Data/radar_rain/{image_url}'

    return full_url