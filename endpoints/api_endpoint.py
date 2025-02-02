from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
serial_data = {}


# Define the schema for POST requests
class SerialData(BaseModel):
    serial: str
    value: str


# Endpoint to handle POST requests on fi_conficence
@app.post("/fi_confidence")
async def add_serial(data: SerialData):
    serial_data[data.serial] = data.value
    return {"message": f"Data for serial {data.serial} saved."}


# Endpoint to handle GET requests for /serial/{serial_id}
@app.get("/serial/{serial_id}")
async def get_serial(serial_id: str):
    if serial_id in serial_data:
        return {"serial": serial_id, "value": serial_data[serial_id]}
    else:
        raise HTTPException(status_code=404, detail="Serial not found")
