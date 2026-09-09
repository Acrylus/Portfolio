# Acrylus Portfolio

Personal portfolio built with Next.js and a small FastAPI backend.

## Project structure

- `app/frontend` - Next.js application and public assets
- `app/backend` - FastAPI application

## Run the frontend

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). Add the supplied portrait as `app/frontend/public/profile.jpg` to display it on the profile page.

## Run the backend

```bash
cd app/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The initial API exposes `GET /health` at [http://localhost:8000/health](http://localhost:8000/health).

## Routes

- `/` or `/profile` - initial profile and introduction
- `/blog` - notebook post listing
- `/vibe` - Bab music page with `Always` by Atlantic Starr
- `/login` - admin-only login screen foundation

The Vibe player uses `app/frontend/public/music/always-atlanticstarr.mp3` and the Spotify code at `app/frontend/public/code/always.svg`.
