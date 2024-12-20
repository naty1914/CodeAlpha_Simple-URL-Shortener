from flask import redirect, render_template, request
from app import app, db
from models import URL
import string
import random


def generate_short_url():
    """Generate a random short URL"""
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters)for _ in range(6))
    return short_url


@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    """Handle URL shortening requests"""
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        short_url = generate_short_url()
        new_url = URL(short_url=short_url, original_url=original_url,
                      date_created=db.func.current_timestamp())
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', short_url=short_url,
                               original_url=original_url)
    return render_template('index.html')


@app.route('/<short_url>')
def redirect_url(short_url):
    """Redirect to the original URL"""
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)
