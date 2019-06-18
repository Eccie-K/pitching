from flask import render_template
from list import app

# views
@app.route('/')
def index():
    '''
    View movie page function that returns the movie details page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',title = title)
