from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from typing import List, Optional
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join("frontend", "index.html"))

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model (used for creation/updating)
class EventIn(BaseModel):
    title: str
    datetime: str
    location: str
    description: str
    status: str

# Output model (includes ID)
class Event(EventIn):
    id: int

# DB setup
conn = sqlite3.connect("events.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    datetime TEXT,
    location TEXT,
    description TEXT,
    status TEXT
)
""")
conn.commit()

@app.post("/events/")
def create_event(event: EventIn):
    cursor.execute("INSERT INTO events (title, datetime, location, description, status) VALUES (?, ?, ?, ?, ?)",
                   (event.title, event.datetime, event.location, event.description, event.status))
    conn.commit()
    return {"message": "Event created"}

@app.get("/events/", response_model=List[Event])
def list_events():
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    return [Event(id=row[0], title=row[1], datetime=row[2], location=row[3], description=row[4], status=row[5]) for row in rows]

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    return {"message": "Event deleted"}

@app.put("/events/{event_id}")
def update_event(event_id: int, event: EventIn):
    cursor.execute("""
        UPDATE events SET title = ?, datetime = ?, location = ?, description = ?, status = ? WHERE id = ?
    """, (event.title, event.datetime, event.location, event.description, event.status, event_id))
    conn.commit()
    return {"message": "Event updated"}

@app.get("/search/", response_model=List[Event])
def search_events(title: Optional[str] = "", location: Optional[str] = "", status: Optional[str] = ""):
    query = "SELECT * FROM events WHERE title LIKE ? AND location LIKE ? AND status LIKE ?"
    cursor.execute(query, (f"%{title}%", f"%{location}%", f"%{status}%"))
    rows = cursor.fetchall()
    return [Event(id=row[0], title=row[1], datetime=row[2], location=row[3], description=row[4], status=row[5]) for row in rows]
