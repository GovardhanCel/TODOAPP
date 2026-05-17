# Backend API Server

Advanced TODO app backend built with Express.js and TypeScript.

## Setup

```bash
npm install
npm run migrate:dev
npm run dev
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh JWT token

### Todos
- `GET /api/todos` - Get user's todos
- `POST /api/todos` - Create new todo
- `PATCH /api/todos/:id` - Update todo
- `DELETE /api/todos/:id` - Delete todo

### Teams
- `GET /api/teams` - List user's teams
- `POST /api/teams` - Create new team
- `GET /api/teams/:id/members` - Get team members
- `POST /api/teams/:id/members` - Add team member

## Environment Variables

- `DATABASE_URL` - PostgreSQL connection string
- `JWT_SECRET` - Secret key for JWT tokens
- `CORS_ORIGIN` - Frontend origin for CORS
- `PORT` - Server port (default: 5000)
- `WEBSOCKET_PORT` - WebSocket port (default: 5001)
