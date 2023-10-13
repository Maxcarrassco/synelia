# synelia
This is an assessment for synelia SE job.

# Environment Requirement
- nodejs v18.x
- python v3.x
- MySQL v8.x

# Environment Tested On
- Ubuntu 22.04 AMD Processor

# How to run this project
### Clone the project and move (cd) into the project's directory
```bash
git clone https://github.com/Maxcarrassco/synelia && cd synelia
```
### Move into the backend directory, create and activate your virtual environment, and install the backend dependencies
```bash
# move into the backend directory
cd backend
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
# install dependencies
pip install -r requirement.txt
```
### Create your environment file (.env) and place your database connection string in it
```bash
# inside the backend directory
touch .env
# inside .env file
DB_URL=mysql://{YOUR_DB_USER_NAME}:{YOUR_DB_PASSWORD}@{HOST}:{PORT}/{DBNAME} # ensure to create a database
```
### Command to start the API Server
```bash
# inside the backend directory
python3 -m api.v1.app
```

### Access API DOC
```bash
localhost:8000
```

### Open a new tab, move into the frontend directory, and install the frontend dependencies
```bash
cd frontend
npm install
```

### Command to start the frontend development server
```bash
npm run dev --open
```

