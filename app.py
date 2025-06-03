import mysql.connector
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import re
import bleach
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App setup
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)
print("Using MySQL credentials:")
print("Host:", os.getenv("MYSQL_HOST"))
print("User:", os.getenv("MYSQL_USER"))
print("Password:", repr(os.getenv("MYSQL_PASSWORD")))

# MySQL Connection
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = bleach.clean(data.get('name', '').strip())
    email = bleach.clean(data.get('email', '').strip())
    message = bleach.clean(data.get('message', '').strip())

    if not name or not email or not message:
        return jsonify({'message': 'All fields are required'}), 400

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return jsonify({'message': 'Invalid email address'}), 400

    try:
        sql = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        db.commit()
        return jsonify({'message': 'Message saved successfully'}), 200
    except Exception as e:
        print(f"MySQL Error: {e}")
        return jsonify({'message': 'Failed to save message'}), 500

if __name__ == '__main__':
    app.run(debug=True)