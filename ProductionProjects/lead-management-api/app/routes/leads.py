from fastapi import APIRouter, status

router = APIRouter(prefix="/leads", tags=["Leads"])


@router.get("/", status_code=status.HTTP_200_OK) #HTTP method GET
def get_leads():
    return [{"id": 1, "name": "Acme Corp", "status": "new"}]


@router.post("/", status_code=status.HTTP_201_CREATED) #HTTP method POST
def create_lead(lead_data: dict):
    return {"id": 2, **lead_data}


@router.put("/{lead_id}", status_code=status.HTTP_200_OK) #HTTP method PUT
def replace_lead(lead_id: int, lead_data: dict):
    return {"id": lead_id, **lead_data}


@router.patch("/{lead_id}", status_code=status.HTTP_200_OK) #HTTP method PATCH
def update_lead_status(lead_id: int, partial_data: dict):
    return {"id": lead_id, "updated_fields": partial_data}


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT) #HTTP method DELETE
def delete_lead(lead_id: int):
    return None
