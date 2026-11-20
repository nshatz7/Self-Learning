#validates incoming requests using query parameters and request bodies (imports schemas)

from fastapi import APIRouter, HTTPException, status
from app.schemas.lead import LeadCreate, LeadUpdate #Pydantic BaseModel's for request bodies

router = APIRouter(prefix="/leads", tags=["Leads"])

FAKE_LEADS_DB = [
    {"id": 1, "name": "Acme Corp", "status": "new"},
    {"id": 2, "name": "Globex Inc", "status": "contacted"},
    {"id": 3, "name": "Initech", "status": "new"},
    {"id": 4, "name": "Umbrella Corp", "status": "qualified"},
]


@router.get("/", status_code=status.HTTP_200_OK)  # HTTP method GET (all leads)
def get_leads(
    status: str | None=None, #declares optional query parameter; lets status value be "None"
    #declares two integer query parameters with default values; if user sends "?limit=abc", FastAPI still automatically validates the type and returns a 422 error ("abc" can't be converted to an integer)
    skip: int = 0, 
    limit: int = 10,
):
    return FAKE_LEADS_DB
    if status is not None:
        results = [lead for lead in results if lead["status"] == status] #filters list in memory if a "status" query parameter was passed
    return results[skip : skip + limit] #list slicing used for pagination (skip = starting index, skip+limit = stopping index)
    


@router.get("/{lead_id}", status_code=status.HTTP_200_OK)  # HTTP method GET (single lead)
def get_lead_by_id(lead_id: int):
    for lead in FAKE_LEADS_DB:
        if lead["id"] == lead_id:
            return lead

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )


@router.post("/", status_code=status.HTTP_201_CREATED)  # HTTP method POST
def create_lead(lead_in: LeadCreate): #FastAPI sees that LeadCreate is a BaseModel, so it automatically parses the incoming JSON request body and validates it
    new_lead = {
        "id": len(FAKE_LEADS_DB) + 1,
        **lead_in.model_dump(), #Converts the validated Pydantic object into a standard Python dictionary so we can unpack it with "**"
    }
    FAKE_LEADS_DB.append(new_lead)
    return new_lead
    

@router.put("/{lead_id}", status_code=status.HTTP_200_OK)
def replace_lead(lead_id: int, lead_in: LeadCreate):
    for index, lead in enumerate(FAKE_LEADS_DB):
        if lead["id"] == lead_id:
            updated_lead = {"id": lead_id, **lead_in.model_dump()}
            FAKE_LEADS_DB[index] = updated_lead
            return updated_lead

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )


@router.patch("/{lead_id}", status_code=status.HTTP_200_OK)
def update_lead(lead_id: int, lead_in: LeadUpdate):
    for lead in FAKE_LEADS_DB:
        if lead["id"] == lead_id:
            updates = lead_in.model_dump(exclude_unset=True) #Secret weapon for PATCH requests: If the client only sends {"status":"qualified"}, strips out name and email instead of overwriting with None
            lead.update(updates)
            return lead

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(lead_id: int):
    for index, lead in enumerate(FAKE_LEADS_DB):
        if lead["id"] == lead_id:
            FAKE_LEADS_DB.pop(index)
            return None

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lead with ID {lead_id} not found",
    )
