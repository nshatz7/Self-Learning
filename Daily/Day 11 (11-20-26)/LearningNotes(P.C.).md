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

- updates app/routes/leads.py
  - imported LeadCreate and LeadUpdate from app/schemas/lead.py, and then replaced dict on POST, PUT, and PATCH routes
