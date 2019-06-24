from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting source of news
    news_sources = get_sources()
    title = 'Home - News Sources'
    return render_template('index.html', title=title, sources = news_sources )

@main.route('/article/<id>')
def article(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_articles(id)

    return render_template('articles.html', article = article)

