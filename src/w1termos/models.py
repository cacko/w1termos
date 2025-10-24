from pydantic import BaseModel, AwareDatetime

class NowResponse(BaseModel):
    temp: float
    timestamp: AwareDatetime

class DeviceResponse(BaseModel):
    name: str
    id: str
    
class DevicesResponse(BaseModel):
    devices: list[DeviceResponse]
    timestamp: AwareDatetime