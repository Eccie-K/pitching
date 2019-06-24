from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_headlines
from ..models import Source, Articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting source of news
    

    title = 'Home - News Sources'

    return render_template('index.html', title = title, general = general_news, sports = sports_news, entertainment = entertainment_news )
