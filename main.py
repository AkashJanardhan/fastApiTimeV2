from fastapi import FastAPI
from datetime import datetime
import httpx

app = FastAPI()

@app.get("/time")
def read_time():
    return {"current_time": datetime.now().isoformat()}

@app.get("/")
def read_time():
    return "Enter /movie/<moviename> to get deatils ----  Enter /time to get time - test new change"

@app.get("/movie/{title}")
async def get_movie_details(title: str):
    api_key = "7d3f1ea5"
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()
