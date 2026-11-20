Setting up Request Bodies

Request Body: A JSON payload attached to the body of an HTTP "POST", "PUT", or "PATCH" request.

Used when a client needs to send complex, secured data to the server (e.g. creating a new lead with name, email, company, status, etc.).
  - If you don't use a request body and instead put the request into a URL, it becomes messy, unsecure, and hits the URL length limits.

How to define the exact shape of a request body: 
  - To define the exact shape, you use a Pydantic BaseModel.
      - When a parameter in your route function is typed as a Pydantic model (instead of basic types (e.g. ints or strings)), FastAPI automatically knows to read from the JSON request body rather than the URL path or query string.

Architecture breakdown for project 1:
- app/schemas/lead.py: defines the data shapes (contracts) for incoming and outgoing lead data.
- app/routes/leads.py: imports schemas and uses them to validate the incoming request bodies.
Endpoint	Request Body Schema	Required Fields	Optional Fields (with defaults)
POST /leads/	LeadCreate	name (str), email (str)	status (str = "new")
PATCH /leads/{lead_id}	LeadUpdate	None	name, email, status

What I Did:
- created app/schemas/lead.py to define request body models:
from pydantic import BaseModel


#inherits from Pydantic's BaseModel (name and email have no default values, making them required unlike status
class LeadCreate(BaseModel): 
    name: str
    email: str
    status: str = "new"

class LeadUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    status: str | None = None

- updates app/routes/leads.py
  - imported LeadCreate and LeadUpdate from app/schemas/lead.py, and then replaced dict on POST, PUT, and PATCH routes:
from app.schemas.lead import LeadCreate, LeadUpdate
...
@router.post("/", status_code=status.HTTP_201_CREATED)  # HTTP method POST
def create_lead(lead_in: LeadCreate): #FastAPI sees that LeadCreate is a BaseModel, so it automatically parses the incoming JSON request body and validates it
    new_lead = {
        "id": len(FAKE_LEADS_DB) + 1,
        **lead_in.model_dump(), #Converts the validated Pydantic object into a standard Python dictionary so we can unpack it with "**"
    }
    FAKE_LEADS_DB.append(new_lead)
    return new_lead

    
