# Exercise 1: Multi-Tenant Core & Issue Tracking

## Domain Context

TrackFlow is a multi-tenant platform structured around the following hierarchy:

* **Workspaces:** Users belong to one or more Workspaces (organizations).
* **Projects:** Teams create Projects inside a Workspace.
* **Issues:** Users create and manage Issues (tickets/tasks) inside a Project.
* **Comments:** Issues can have Comments attached to them.

---

## Your Task

Design the REST endpoints (`HTTP Method` + `URI Path`) to support the following 7 user actions. Do not worry about request/response JSON bodies yet—focus strictly on URL structure, resource naming, nesting depth, and HTTP verbs.

1. List all projects inside a specific workspace.
2. Create a new issue inside a specific project.
3. Fetch a single issue by its unique ID *(assume issue IDs are globally unique across the entire platform, e.g., `iss_98765`)*.
4. Update only the status and priority of an existing issue *(e.g., changing status from `"todo"` to `"in_progress"`)*.
5. List all issues across an entire workspace that are assigned to a specific user and currently have a `"high"` priority.
6. Add a comment to a specific issue.
7. Archive a workspace *(Note: archiving is a soft-state change, not a permanent deletion of the data)*.

---

## Attempt

1. `GET`
2. `POST`
3. `GET`
4. `PATCH`
5. `GET`
6. `POST`
7. `PATCH`

---

## Solution

1. `GET`
2. `POST`
3. `GET`
4. `PATCH`
5. `GET`
6. `POST`
7. `PATCH`
