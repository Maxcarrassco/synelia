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
```
git clone https://github.com/Maxcarrassco/synelia && cd synelia
```
### Move into the backend directory and install the backend dependencies
```
cd backend
pip install -r requirement.txt
```
### Create your environment file (.env) and place your database connection string in it
```
// inside the backend directory
touch .env
// inside .env file
DB_URL=mysql://{YOUR_DB_USER_NAME}:{YOUR_DB_PASSWORD}@{HOST}:{PORT}/{DBNAME} // ensure to create a database

### Command to start the API Server
```
// inside the backend directory
```
python3 -m api.v1.app
```

### Open a new tab, move into the frontend directory, and install the frontend dependencies
```
cd frontend
npm install
```

### Command to start the frontend development server
```
npm run dev
```

