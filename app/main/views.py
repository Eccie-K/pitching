from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source, get_articles
from ..models import Source, Articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting source of news
    newsSource = get_source()
    title = 'Home - News Sources'
    print(newsSource)

    return render_template('index.html', title = title, source = newsSource )

@main.route('/artcle/<string:id>')
def source(id):
        '''
        View source page function that shows source and details
        '''
        articles = get_articles(id)
        print(articles)
        return render_template('articles.html', articles = articles )


