# 💡 Daily Inspiration: Random Quote Generator

A clean, modern web application built with Python, Flask, HTML, and CSS that serves up random inspirational quotes and allows users to submit their own.

## 🚀 Features
* **Random Quote Display:** Generates a new random quote from the database on every page load or button click.
* **Add Your Own:** Includes a clean, user-friendly form to add custom quotes and authors directly to the list.
* **Modern UI:** Features a responsive, centered card layout with a gradient background, shadow effects, and hover transitions.

## 🛠️ Technology Stack
* **Backend:** Python 3, Flask framework
* **Frontend:** HTML5, CSS3
* **Development Environment:** Visual Studio Code

## 📁 Project Structure
```text
quote-generator/
│
├── app.py               # The main Flask application and routing logic
├── .gitignore           # Tells Git which files to ignore (e.g., __pycache__)
├── README.md            # Project documentation
│
├── templates/           
│   └── index.html       # The main HTML layout and form
│
└── static/
    └── style.css        # All CSS styling and UI design
```

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/quote-generator.git](https://github.com/yourusername/quote-generator.git)
   cd quote-generator
   ```

2. **Install requirements:**
   Make sure you have Python installed, then install Flask:
   ```bash
   pip3 install flask
   ```

3. **Run the application:**
   ```bash
   python3 app.py
   ```

4. **View in browser:**
   Open your web browser and navigate to `http://127.0.0.1:5000`

## 🔮 Future Enhancements (Ideas)
* Connect a SQLite or PostgreSQL database so newly added quotes save permanently.
* Add an external API (like the ZenQuotes API) to fetch thousands of quotes dynamically.
* Implement a feature to "like" or favorite specific quotes.
