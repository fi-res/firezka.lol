from fastapi import FastAPI
from fastapi.responses import Response, FileResponse

app = FastAPI()

@app.get('')
def get():
	return '6-7'

@app.get("/chupep.jpg")
async def chupep():
    return FileResponse("chupep.jpg")
