from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -------------------------------
# DATABASE INITIALIZATION
# -------------------------------

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # Workers table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS workers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        area TEXT,
        experience TEXT
    )
    """)

    # Bookings table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT,
        phone TEXT,
        location TEXT,
        workers INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


# Run database initialization
init_db()


# -------------------------------
# HOME PAGE
# -------------------------------

@app.route('/')
def home():
    return render_template("index.html")


# -------------------------------
# WORKER REGISTRATION
# -------------------------------

@app.route('/register_worker', methods=['GET','POST'])
def register_worker():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        area = request.form['area']
        experience = request.form['experience']

        conn = sqlite3.connect("database.db")
        conn.execute(
        "INSERT INTO workers (name, phone, area, experience) VALUES (?,?,?,?)",
        (name, phone, area, experience)
        )

        conn.commit()
        conn.close()

        return redirect("/workers")

    return render_template("worker_register.html")


# -------------------------------
# SHOW ALL WORKERS
# -------------------------------

@app.route('/workers')
def workers():

    conn = sqlite3.connect("database.db")
    workers = conn.execute("SELECT * FROM workers").fetchall()
    conn.close()

    return render_template("workers.html", workers=workers)


# -------------------------------
# HIRE WORKERS PAGE
# -------------------------------

@app.route('/hire', methods=['GET','POST'])
def hire():

    if request.method == 'POST':

        client = request.form['client']
        phone = request.form['phone']
        location = request.form['location']
        workers = request.form['workers']
        date = request.form['date']

        conn = sqlite3.connect("database.db")

        conn.execute(
        "INSERT INTO bookings (client, phone, location, workers, date) VALUES (?,?,?,?,?)",
        (client, phone, location, workers, date)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("hire.html")


# -------------------------------
# SHOW ALL BOOKINGS
# -------------------------------

@app.route('/bookings')
def bookings():

    conn = sqlite3.connect("database.db")
    bookings = conn.execute("SELECT * FROM bookings").fetchall()
    conn.close()

    return render_template("bookings.html", bookings=bookings)


# -------------------------------
# RUN SERVER
# -------------------------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
