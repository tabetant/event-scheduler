
# 📅 Event Scheduler App

A full-stack web application that lets you schedule, track, and search for events.  
Built with **FastAPI** (Python) as the backend and **vanilla HTML + JavaScript** as the frontend — all served together in a single repository.

---

## ✅ Features

- Add, edit, and delete events
- Track event status: Upcoming, Attending, Maybe, Declined
- Search events by title, location, and status
- Clean, responsive UI with status color badges
- SQLite database for fast local storage
- All-in-one deployable backend and frontend

---

## 📁 Project Structure

```
event-scheduler/
│
├── backend/
│   ├── main.py               # FastAPI application with endpoints and static file serving
│   ├── events.db             # SQLite database (auto-created)
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── index.html            # Fully styled HTML + JavaScript app
│
├── render.yaml               # Deployment config for Render
└── README.md
```

---

## 🚀 Running Locally

### 1. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the FastAPI server
```bash
uvicorn main:app --reload
```

Then open your browser and go to:
```
http://127.0.0.1:8000
```

This serves the frontend and handles API requests.

---

## 🌐 Deployment (Render)

### 1. Create a GitHub repo and push this folder

### 2. Sign in to [https://render.com](https://render.com) and:
- Create a **Web Service**
- Point it to your GitHub repo
- Set the start command:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 10000
```

### 3. Add `render.yaml` if you want automatic deploy config

---

## 🧠 Future Features (Ideas)

- User login and authentication (JWT)
- Invite participants to events via email
- AI-powered suggestions (e.g., auto-filling descriptions)
- Calendar view with FullCalendar.js
- Export to `.csv` or `.ics`

---

Made with ❤️ for productivity!
