# Project 1 - Phase 1 (project setup and architecture)

---

## Setup Steps

### 1. Initialize Directory Structure
Created root and subdirectories to establish the project layout:
```bash
mkdir -p src tests config docs
```

### 2. Configure Python Packages
Created `__init__.py` files across all module directories to enable package imports:
```bash
touch src/__init__.py tests/__init__.py
```

### 3. Set Up Configuration Files
Created essential configuration and settings files for environment-specific logic.

### 4. Configure Environment & Project Metadata
Prepared environment and dependency manifests:
* **`.gitignore`**: Configured exclusions for virtual environments (`.venv/`), bytecode (`__pycache__/`), and environment variables (`.env`).
* **`.env.example`**: Created a sanitized template for required environment variables.
* **`requirements.txt`**: Defined baseline dependencies and version constraints.

### 5. Install Dependencies
Created/activated the virtual environment and installed all required packages:
```bash
pip install -r requirements.txt
```

### 6. Commit and Push Architecture
Initialized Git version control, committed the scaffolded architecture, and pushed the base commit to the remote GitHub repository:
```bash
git init
git add .
git commit -m "chore: scaffold project structure and configuration"
git branch -M main
git remote add origin <REMOTE_REPOSITORY_URL>
git push -u origin main
```
