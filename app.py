import os
from flask import Flask, render_template
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# Route handlers
@app.route('/')
def home():
    """Homepage route - displays event overview and highlights"""
    return render_template('home.html')

@app.route('/register')
def register():
    """Registration route - shows registration form"""
    return render_template('register.html')

@app.route('/time')
def time():
    """Tijdschema route - toont het volledige programma"""
    return render_template('time.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500