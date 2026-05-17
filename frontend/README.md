# Frontend React Application

Modern React 18 TODO app frontend with TypeScript.

## Setup

```bash
npm install
npm start
```

## Project Structure

```
src/
├── components/     # Reusable UI components
├── pages/          # Page components
├── hooks/          # Custom React hooks
├── stores/         # Zustand state management
├── utils/          # Utility functions
└── App.tsx         # Root component
```

## Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests

## Environment Variables

Create a `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_WEBSOCKET_URL=ws://localhost:5001
```
