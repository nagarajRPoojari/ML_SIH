from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.main import Pipeline
from pipeline.component import Data
    
app = FastAPI()
pipeline=Pipeline()

@app.get("/")
def read_root():
    return {"message": "Hello, API endpoint!"}

@app.post("/predict")
def predict(data:Data):
    res=pipeline.main(data.user.dict() , data.all_data)
    
    
    return {"message":res}

