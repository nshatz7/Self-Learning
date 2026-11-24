#defines the data shapes (contracts) for incoming and outgoing lead data

from pydantic import BaseModel


#inherits from Pydantic's BaseModel (name and email have no default values, making them required unlike status
class LeadCreate(BaseModel): 
    name: str
    email: str
    status: str = "new"

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "name": "Stark Industries",
                    "email": "tony@starkindustries.com",
                    "status": "new",
                }
            ]
        }
    )

class LeadUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    status: str | None = None

class LeadResponse(BaseModel): #defines exact fields allowed in outgoing JSON responses
    id: int
    name: str
    email: str
    status: str
