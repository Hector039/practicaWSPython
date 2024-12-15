from fastapi import FastAPI
from main import fetchDataTable, startProcess

app = FastAPI()

@app.get("/")
async def getData():
    try:
        result = fetchDataTable()
        return result
    except Exception as error:
        return {"message": error}

@app.get("/start/{query}")
async def start(query: str = 'residuos'):
    try:
        startProcess(query)
        return {'message': 'Se inició el proceso, espere', 'palabra': query}
    except Exception as error:
        return {"message": error}
    