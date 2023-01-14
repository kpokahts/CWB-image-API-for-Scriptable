from fastapi import FastAPI
from crawl import get_radar
import uvicorn

app = FastAPI()

@app.get("/get_radar")
def root():
    return get_radar()

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True, port=5566)