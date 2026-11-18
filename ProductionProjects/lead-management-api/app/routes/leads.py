from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/leads", tags=["Leads"])

FAKE_LEADS_DB = [
    {"id": 1, "name": "Acme Corp", "status": "new"},
    {"id": 2, "name": "Globex Inc", "status": "contacted"},
]


@router.get("/", status_code=status.HTTP_200_OK)  # HTTP method GET (all leads)
def get_leads():
    return FAKE_LEADS_DB


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
def create_lead(lead_data: dict):
    return {"id": 2, **lead_data}


@router.put("/{lead_id}", status_code=status.HTTP_200_OK)  # HTTP method PUT
def replace_lead(lead_id: int, lead_data: dict):
    return {"id": lead_id, **lead_data}


@router.patch("/{lead_id}", status_code=status.HTTP_200_OK)  # HTTP method PATCH
def update_lead_status(lead_id: int, partial_data: dict):
    return {"id": lead_id, "updated_fields": partial_data}


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)  # HTTP method DELETE
def delete_lead(lead_id: int):
    return None
