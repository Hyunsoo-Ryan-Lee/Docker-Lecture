from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"From: {os.environ.get('ENV', 'DEFAULT_ENV')}"}

@app.get("/{parameter}")
async def read_params(parameter : str):
    
    env_val = os.environ.get(parameter, '')
    
    if env_val:
        return {parameter : env_val}
    
    return {parameter : f"There are no ENV with name {parameter}"}