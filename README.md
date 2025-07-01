# portfolio
# 🧑‍💻 Pratheesha E - Portfolio

Welcome to my personal portfolio website built using **Flask** and hosted on **Render**. This site showcases my skills, projects, resume, and contact information in a modern and responsive format.

🌐 Live Site: [nandha-kumar-s-portfolio.onrender.com](https://nandha-kumar-s-portfolio.onrender.com)

---

## 📂 Project Structure

portfolio/
├── app.py # Main Flask app
├── requirements.txt # Dependencies
├── static/ # CSS, images, favicon
│ ├── images/
│ └── style.css
├── templates/ # HTML files (Jinja2)
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ ├── projects.html
│ ├── resume.html
│ ├── contact.html
│ └── 404.html
└── render.yaml (optional)

yaml
Copy
Edit

---

## 🚀 Features

- ⚡ Responsive and mobile-friendly design
- 🧠 Flask + Bootstrap integration
- 📄 Resume download & embedded view
- 🛠️ Project showcase with images
- 📬 Contact information with links
- 🌐 Deployed on [Render](https://render.com/)

---

## 📦 Installation (Run Locally)

```bash
# Clone the repository
git clone https://github.com/nandhakumars444/portfolio.git
cd portfolio

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
Then open http://localhost:5000 in your browser.

🛠 Deployment on Render
Make sure gunicorn is in requirements.txt

Use this start command on Render:

nginx
Copy
Edit
gunicorn app:app
You can optionally add a render.yaml for automatic deployment.

👨‍🎓 About Me
I'm Nandha Kumar S, an Electronics and Communication Engineering graduate passionate about IoT, AI, and software development. This portfolio reflects my journey, academic work, and passion projects.

📫 Contact Me
✉️ Email: nandhakumars444@gmail.com

💼 LinkedIn: linkedin.com/in/nandhakumars444

💻 GitHub: github.com/nandhakumars444


📝 License
This project is open source and available under the MIT License.

yaml
Copy
Edit

---

Would you like me to:
- Commit this directly to your GitHub repo?
- Include a license file (`MIT`) if you want to make it fully open source?

Let me know!