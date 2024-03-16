from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import hashlib
import validators
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database setup
def create_connection():
    conn = sqlite3.connect('url_shortener.db')
    return conn

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY, original_url TEXT UNIQUE, short_url TEXT UNIQUE)''')
    conn.commit()
    conn.close()

create_table()

# Shorten URL function
def shorten_url(url):
    return hashlib.sha1(url.encode()).hexdigest()[:8]

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Shorten URL route
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    if not validators.url(original_url):
        flash('Invalid URL!')
        return redirect(url_for('home'))

    short_url = shorten_url(original_url)

    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        flash('URL already shortened!')
        return redirect(url_for('home'))

    flash('URL shortened successfully!')
    return render_template('index.html', original_url=original_url, short_url=short_url)


# Redirect to original URL route
@app.route('/<short_url>')
def redirect_to_original(short_url):
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute("SELECT original_url FROM urls WHERE short_url=?", (short_url,))
        result = c.fetchone()
        if result:
            original_url = result[0]
            conn.close()
            return redirect(original_url)
        else:
            conn.close()
            flash('URL not found!')
            return redirect(url_for('home'))
    except:
        flash('An error occurred!')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
