from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/hi/{name}")
async def sayhi(name: str):
    return PlainTextResponse(f"hi {name}")
