from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import generator

app = FastAPI()
@app.get("/test/v1/")
async def gen_qr(email: str):
    print(email)
    cert_url = generator.generate(email)
    if cert_url is not None:
        response = RedirectResponse(url='/certs/'+cert_url)
        return response
   

app.mount("/certs", StaticFiles(directory="temp/cert"), name="cert")
app.mount("/", StaticFiles(directory="website"), name="web")

@app.get("/hello")
def hello():
    print("hello")
    return "hello"




@app.get("/gen/v1/")
async def gen_qr(name: str, roll: int):
    cert_url = generator.generate(name, roll)
    return cert_url
