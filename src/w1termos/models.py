from pydantic import BaseModel, AwareDatetime

class NowResponse(BaseModel):
    temp: float
    timestamp: AwareDatetime
