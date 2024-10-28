from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/home')
def get_home():
    return 'Ola!'