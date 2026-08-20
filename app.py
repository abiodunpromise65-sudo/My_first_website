import os
from flask import Flask, render_template

app = Flask(__name__)

# Sample Python lessons dataset
LESSONS = [
    {
        "id": 1,
        "title": "Variables & Data Types",
        "code": "x = 10\nname = 'Python'\nis_fun = True\nprint(f'{name} score: {x}')",
        "explanation": "Variables store data values. Python automatically detects variable types."
    },
    {
        "id": 2,
        "title": "Conditionals & Logic",
        "code": "age = 18\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "explanation": "Use 'if', 'elif', and 'else' statements to control program flow based on conditions."
    },
    {
        "id": 3,
        "title": "Functions",
        "code": "def greet(user):\n    return f'Hello, {user}!'\n\nmessage = greet('Coder')\nprint(message)",
        "explanation": "Functions are reusable blocks of code defined with the 'def' keyword."
    }
]

@app.route("/")
def home():
    return render_template("index.html", lessons=LESSONS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
