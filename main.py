from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import generator


app = FastAPI()



app.mount("/certs", StaticFiles(directory="temp/cert"), name="cert")

@app.get("/hello")
def hello():
    print("hello")
    return "hello"

@app.get("/test/v1/{name}/{roll}")
async def gen_qr(name,roll):
    print("hello")
    cert_url = generator.generate(name, roll)
    return cert_url


@app.get("/gen/v1/")
async def gen_qr(name: str, roll: int):
    cert_url = generator(name, roll)
    return cert_url