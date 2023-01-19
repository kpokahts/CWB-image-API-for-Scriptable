from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import requests
import re
import uvicorn

app = FastAPI()

@app.get("/get_radar")
def get_radar(stn:str):
    if stn not in ['RCSL', 'RCNT', 'RCLY']:
        raise HTTPException(status_code=400, detail='Wrong station')

    res = requests.get('https://www.cwb.gov.tw/Data/js/obs_img/Observe_radar_rain.js')
    content = res.text
    image_url = re.findall(fr'(CV1_{stn}[\w\/]+.png)', content)[0]
    full_url = f'https://www.cwb.gov.tw/Data/radar_rain/{image_url}'

    return full_url


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True, port=5566)