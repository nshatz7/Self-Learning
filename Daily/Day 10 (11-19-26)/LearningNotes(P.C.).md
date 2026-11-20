Setting up Query Parameters
Query Parameter: key-value pair appended to the end of a URL after a question mark (?). If there are multiple query parameters, they are separated by an ampersand (&).
Architecture Breakdown for Project 1:
URL Requested	status	skip	limit	Result
GET /leads/	None	0	10	Returns up to the first 10 leads
GET /leads/?status=new	"new"	0	10	Returns only leads with "status": "new"
GET /leads/?skip=1&limit=1	None	1	1	Skips the 1st lead and returns the 2nd
GET /leads/?status=new&limit=5	"new"	0	5	Returns up to 5 "new" leads

What I Did:
- Updated "FAKE_LEADS_DB"
- Updated "get_leads" function:
