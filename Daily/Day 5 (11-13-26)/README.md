# Day 5: Self-Learning Log

## Agenda

* **LeetCode Practice**
  * **#128:** Longest Consecutive Sequence
  * **#448:** Find All Numbers Disappeared in an Array
* **Core Focus:** Identifying streak roots using $O(1)$ set membership; in-place array sign marking.
* **Secondary Focus:** PCAP studying (all modules: exam traps and full overview).
* **Production Code:** Project 1 — Backend development (FastAPI fundamentals).

---

## Conclusion & Outcomes

### Completed Tasks
* Solved both LeetCode problems and documented them with full `README` files.

### Learning Outcomes
* **PCAP Studying:** Covered exam traps (compiled a cheat sheet), top code patterns, and a quick-fire review checklist.
* **Production Code (FastAPI):** Learned core fundamentals including decorators, route handlers, `APIRouter`, dependency injection, middleware, and request lifecycles.

---

## Core Daily Question

> **Question:** Should I identify streak roots using $O(1)$ set membership or in-place array sign marking?

**Answer:**
**In-place array sign marking** is the ideal first choice because it optimizes both time and space complexity (O(N) time, O(1) auxiliary space), whereas O(1) set membership trades high space complexity (O(N)) for fast lookups. However, because in-place sign marking requires very strict input constraints (such as positive integers bounded by the array's length), **$O(1)$ set membership** will be the most practical and commonly used approach in general scenarios.
