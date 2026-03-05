from flask import Flask, render_template, request
from flask_socketio import SocketIO
from datetime import datetime
import sqlite3

# ===== Flask Setup =====
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)

# ===== Connected Users =====
connected_users = {}

# ===== Database Setup =====
conn = sqlite3.connect("chat.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    time TEXT,
    type TEXT
)
""")
conn.commit()


# ===== Routes =====
@app.route("/")
def index():
    return render_template("index.html")


# ===== Helper to send chat history =====
def send_history():
    c.execute("SELECT username, message, time, type FROM messages ORDER BY id")
    history = [{"username": row[0], "message": row[1], "time": row[2], "type": row[3]} for row in c.fetchall()]
    socketio.emit("chat_history", history)


# ===== Socket Events =====

# User joins
@socketio.on("join")
def join(username):
    if request.sid not in connected_users:
        connected_users[request.sid] = username
        # Save join message in DB
        c.execute("INSERT INTO messages (username, message, time, type) VALUES (?, ?, ?, ?)",
                  (username, f"{username} joined the chat", datetime.now().strftime("%H:%M"), "system"))
        conn.commit()
        # Emit system message
        socketio.emit("system_message", f"{username} joined the chat")

    # Send updated user list and chat history
    socketio.emit("user_list", list(connected_users.values()))
    send_history()


# User disconnects
@socketio.on("disconnect")
def disconnect():
    username = connected_users.pop(request.sid, None)
    if username:
        # Save leave message in DB
        c.execute("INSERT INTO messages (username, message, time, type) VALUES (?, ?, ?, ?)",
                  (username, f"{username} left the chat", datetime.now().strftime("%H:%M"), "system"))
        conn.commit()
        socketio.emit("system_message", f"{username} left the chat")
        socketio.emit("user_list", list(connected_users.values()))
        send_history()


# User sends a message
@socketio.on("send_message")
def send_message(data):
    msg = {
        "username": data["username"],
        "message": data["message"],
        "time": datetime.now().strftime("%H:%M"),
        "type": "user"
    }
    # Save message to DB
    c.execute("INSERT INTO messages (username, message, time, type) VALUES (?, ?, ?, ?)",
              (msg["username"], msg["message"], msg["time"], msg["type"]))
    conn.commit()
    send_history()


# Delete all chat
@socketio.on("delete_all")
def delete_all():
    c.execute("DELETE FROM messages")
    conn.commit()
    send_history()


# ===== Main =====
if __name__ == "__main__":
    socketio.run(app, debug=True)
