# My_Flask_portfolio
# 🧑‍💻 Ali Haider – Full Stack Portfolio (Flask + MySQL)

This is a professional portfolio website built with:

- 🔥 Flask (Python)
- 🎨 HTML, CSS (Tailwind + custom styling)
- 📬 Contact Form (stores submissions in MySQL)
- 🛠️ Backend connected to a MySQL database
- 🚀 Ready for deployment on Render

---

## 🌟 Features

- 📄 Clean, responsive portfolio layout with animations
- 💬 Contact form with form validation and feedback
- 🗃️ Stores messages securely in a MySQL database
- 🔐 Environment variables handled using `.env`
- ✉️ (Optional) Email notifications via SMTP

---

## 📁 Project Structure

├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend layout
├── static/
│ └── styles.css # Custom styling
├── .env.template # Sample environment config
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🔧 Setup Instructions (Local)

### ✅ Prerequisites

- Python 3.x
- MySQL (XAMPP, MySQL Workbench, etc.)

### 📦 1. Install dependencies

```bash
pip install -r requirements.txt
CREATE DATABASE portfolio;

USE portfolio;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Rename .env.template to .env and update with your credentials:

env
Copy
Edit
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=portfolio

▶️ 4. Run the server
bash
Copy
Edit
python app.py
Open browser: http://localhost:5000

🌍 Deployment
You can deploy this project on Render or Heroku.

If deploying on Render:

Use the same Start Command: python app.py

Set environment variables in the dashboard (copy from .env)

For live databases, consider using PlanetScale for a free MySQL server.

📬 Contact
Feel free to reach out if you’re interested in collaboration or have feedback!

📧 alihaider524@gmail.com

🔗 LinkedIn
🔗 GitHub

🔒 License
This project is licensed for educational and portfolio use. All rights reserved.

yaml
Copy
Edit

---

### ✅ To use:

1. Create a file called `README.md` in your project root.
2. Paste the content above.
3. Commit and push:

```bash
git add README.md
git commit -m "Add professional README"
git push origin main
