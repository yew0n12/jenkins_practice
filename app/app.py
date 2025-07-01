from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/api')
def api():
    return {"message": "Hello from Flask API!"}

@app.route('/db')
def db_test():
    db_url = os.environ.get('DATABASE_URL')
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        now = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db_time": str(now[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

