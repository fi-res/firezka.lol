from fastapi import FastAPI
from fastapi.responses import Response, FileResponse

app = FastAPI()

@app.get('/')
def get():
	return 'Скоро все будет, потом сделаю'

@app.get("/chupep.jpg")
async def chupep():
    return FileResponse("chupep.jpg")
