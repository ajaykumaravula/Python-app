# main.py
import os
  
from fastapi import FastAPI

app = FastAPI()
appenv = os.environ['APPENV']
@app.get("/")
async def root():
    return {
        "message": "World",
        "APPENV": appenv
        }