# main.py
import os
  
from fastapi import FastAPI

app = FastAPI()
appenv = os.environ['ARGENV']
@app.get("/hello")
async def root():
    return {
        "message": "World",
        "APPENV": appenv
        }