from flask import render_template, request, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # placeholder to handle form submission
        text = request.form.get('text', '')
        return render_template('result.html', text=text)
    return render_template('index.html')
