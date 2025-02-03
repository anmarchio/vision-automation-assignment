from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
serial_data = {
    "00929": "first answer",
    "140521": "second answer",
    "126713": "third answer"
}


class SerialData(BaseModel):
    serial: str
    value: str


# Endpoint to handle POST requests on count/{number}
@app.post("/count/{number}")
async def add_serial(number: str):
    return {"message": f"Counted {number} objects that exceed confidence level."}


# Endpoint to handle GET requests for /serial/{serial_id}
@app.get("/serial/{serial_id}")
async def get_serial(serial_id: str):
    print(f"ID incoming: {serial_id}")
    if serial_id in serial_data:
        return {"serial": serial_id, "value": serial_data[serial_id]}
    else:
        raise HTTPException(status_code=404, detail="Serial not found")
