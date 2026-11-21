import os, time
from flask import Flask, jsonify, render_template, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
DB = os.getenv("DATABASE_URL", "postgresql://portaluser:change-this-password@localhost:5432/results")
DEMO = [
    ("STU1001","Ananya","B.E. Computer Science","Semester 3",86.5,"PASS"),
    ("STU1002","Karthik","B.E. Computer Science","Semester 3",78.0,"PASS"),
    ("STU1003","Meera","B.E. Information Technology","Semester 3",91.0,"PASS"),
    ("STU1004","Arun","B.E. Computer Science","Semester 3",42.0,"PASS"),
]
def connect():
    return psycopg2.connect(DB, connect_timeout=3)
def init_db():
    error = None
    for _ in range(15):
        try:
            with connect() as c:
                with c.cursor() as q:
                    q.execute('''CREATE TABLE IF NOT EXISTS student_results (
                    register_no VARCHAR(20) PRIMARY KEY, student_name VARCHAR(100) NOT NULL,
                    programme VARCHAR(120) NOT NULL, semester VARCHAR(30) NOT NULL,
                    percentage NUMERIC(5,2) NOT NULL, result_status VARCHAR(10) NOT NULL)''')
                    q.executemany('''INSERT INTO student_results VALUES (%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (register_no) DO NOTHING''', DEMO)
            return
        except psycopg2.Error as e:
            error=e; time.sleep(2)
    raise RuntimeError(f"PostgreSQL initialisation failed: {error}")
@app.get("/")
def home():
    return render_template("index.html")
@app.get("/health")
def health():
    try:
        with connect() as c:
            with c.cursor() as q: q.execute("SELECT 1")
        return jsonify(status="healthy", database="connected"), 200
    except psycopg2.Error:
        return jsonify(status="unhealthy", database="unavailable"), 503
@app.get("/api/results")
def results():
    reg=request.args.get("register_no","").strip().upper()
    if not reg: return jsonify(error="Enter a register number."), 400
    try:
        with connect() as c:
            with c.cursor(cursor_factory=RealDictCursor) as q:
                q.execute("SELECT * FROM student_results WHERE register_no=%s",(reg,))
                row=q.fetchone()
        if row is None: return jsonify(error="No demo result found."), 404
        row["percentage"]=float(row["percentage"])
        return jsonify(row)
    except psycopg2.Error:
        return jsonify(error="Database temporarily unavailable."), 503
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=False)
