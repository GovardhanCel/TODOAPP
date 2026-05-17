## Quick Start - Run Locally (Without Docker)

**This is the simplest way to get the app running locally for development.**

### Prerequisites
- Node.js 18+ installed
- PostgreSQL 15 installed locally (or use a cloud database)

### Step 1: Set Up Backend

```bash
# Navigate to backend directory
cd /Users/admin/TODOAPP/backend

# Install dependencies
npm install --legacy-peer-deps

# Create .env file with database config
cat > .env << EOF
DATABASE_URL="postgresql://postgres:password@localhost:5432/tododb"
JWT_SECRET="dev-secret-key-change-in-production"
NODE_ENV="development"
PORT=5000
CORS_ORIGIN="http://localhost:3000"
WEBSOCKET_PORT=5001
EOF

# Start the backend server
npm run dev
```

Backend will be available at: **http://localhost:5000**

### Step 2: Set Up Frontend (In a NEW terminal)

```bash
# Navigate to frontend directory
cd /Users/admin/TODOAPP/frontend

# Install dependencies
npm install --legacy-peer-deps

# Create .env file
cat > .env << EOF
REACT_APP_API_URL=http://localhost:5000
REACT_APP_WEBSOCKET_URL=ws://localhost:5001
EOF

# Start the frontend dev server
npm start
```

Frontend will open at: **http://localhost:3000**

### Step 3: Set Up Database

**Option A: Using PostgreSQL Docker Container (recommended)**
```bash
docker run -d \
  --name todoapp-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=tododb \
  -p 5432:5432 \
  postgres:15-alpine
```

**Option B: Using local PostgreSQL**
- Install PostgreSQL: https://www.postgresql.org/download/
- Create database:
  ```sql
  CREATE DATABASE tododb;
  CREATE USER postgres WITH PASSWORD 'password';
  ALTER ROLE postgres WITH SUPERUSER;
  ```

### Verify It's Working

- **Frontend**: http://localhost:3000 (React app)
- **Backend**: http://localhost:5000/health (should return `{"status":"OK", ...}`)
- **Database**: Port 5432 (PostgreSQL)

### Stop Services

```bash
# In each terminal, press Ctrl+C

# Or stop the database container:
docker stop todoapp-db
```

---

**This is the preferred setup for local development!** 🚀
