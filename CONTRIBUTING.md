# Contributing to TODO App

## Development Workflow

### 1. Branching Strategy

- `main` - Production branch (protected)
- `develop` - Development branch
- `feature/*` - Feature branches (e.g., `feature/user-authentication`)
- `bugfix/*` - Bug fix branches (e.g., `bugfix/login-error`)

### 2. Creating a Feature Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### 3. Commit Message Format

Use conventional commits:

```
type(scope): subject

body

footer
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(auth): add JWT authentication

- Implement JWT token generation
- Add authentication middleware
- Secure all API endpoints

Closes #123
```

### 4. Creating a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:
- Clear title describing the change
- Description of what and why
- Reference related issues (#123)
- Screenshots if UI changes

### 5. Code Review & Merge

- Address review comments
- Keep commits clean and logical
- Merge using "Squash and merge" for small PRs
- Delete feature branch after merge

## Local Testing

### Run Tests

```bash
# Backend
cd backend
npm test

# Frontend
cd frontend
npm test
```

### Manual Testing

```bash
# Start services
docker-compose up

# Frontend: http://localhost:3000
# Backend: http://localhost:5000
# Database: localhost:5432
```

## Code Style

### Backend (TypeScript)

```bash
cd backend
npm run lint
npm run lint:fix
```

### Frontend (React/TypeScript)

- Use functional components with hooks
- Use proper TypeScript types
- Follow ESLint rules

## Database Migrations

### Create a new migration

```bash
cd backend
npm run migrate:dev -- --name add_new_table
```

### Apply migrations

```bash
npm run migrate
```

### View database

```bash
npm run prisma:studio
```

## Documentation

- Update README files when adding features
- Document API endpoints in code comments
- Keep this CONTRIBUTING.md up to date

## Deployment

### To Staging (develop branch)
Changes are automatically tested and built but not deployed

### To Production (main branch)
Changes are tested, built, and deployed to AKS automatically

## Questions or Issues?

- Open an issue with detailed description
- Use labels (bug, feature, documentation, etc.)
- Mention relevant people @username
