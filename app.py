from flask import Flask, render_template, request
import sqlite3
from scheduler import start_scheduler

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            url TEXT,
            target_price INTEGER,
            alerted INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        target_price = int(request.form["price"])

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products (url, target_price) VALUES (?, ?)",
            (url, target_price)
        )
        conn.commit()
        conn.close()

        return "Tracking started! You will get WhatsApp alert."

    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    start_scheduler()
    app.run()
