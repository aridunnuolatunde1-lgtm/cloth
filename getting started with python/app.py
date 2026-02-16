from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('clothing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/snake')
def snake():
    # For simplicity, we'll just run the snake game as a separate process
    # In a real app, you'd integrate it better
    import subprocess
    subprocess.Popen(['python', 'main.py'])
    return "Snake game launched! Check your console or separate window."

if __name__ == '__main__':
    app.run(debug=True)
