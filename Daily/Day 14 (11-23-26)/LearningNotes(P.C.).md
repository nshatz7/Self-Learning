- What I Did:
- updated api/v1/leads.py to import "Depends" and "Query"
- created reusable "pagination_params" dependancy:
def pagination_params( #dependancy that FastAPI automaticallly inspects its parameters (skip and limit) and reads them from the query string
    skip: int = Query(default=0, ge=0, description="Number of records to skip"), #"default" and "ge" sets up gaurdrails
    limit: int = Query(default=10, ge=1, le=100, description="Max records to return"),
) -> dict[str, int]:
    return {"skip": skip, "limit": limit}
- Injected paginaiton_params into get_leads:
