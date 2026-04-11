# Pull Request

## Summary
<!-- Describe what this PR does and why. Reference any related issues. -->


## Type of Change
- [ ] Feature
- [ ] Bug Fix
- [ ] Refactor
- [ ] Docs / Config

## Domain
- [ ] Frontend (`frontend/`)
- [ ] Backend (`backend/`)

---

## Pre-Merge Checklist

### All PRs
- [ ] Code follows the established Swagger API contract
- [ ] Functionality is tested locally
- [ ] No hardcoded secrets or passwords

### Frontend Only
- [ ] Loading states (spinners) are handled
- [ ] Error states (toasts) are handled
- [ ] Runs clean on `cd frontend && npm run dev` (port 5173)

### Backend Only
- [ ] Correct HTTP status codes are returned (e.g. 400 vs 401)
- [ ] Runs clean on the backend dev server

---

## Reviewer Assignment
<!-- Tag your mandatory domain peer reviewer:
     Frontend PRs → tag @Maggie
     Backend PRs  → tag @Abby or @Happiness  -->

## File Isolation Confirmation
- [ ] This PR does **not** touch files outside its domain directory (`frontend/` or `backend/`)
