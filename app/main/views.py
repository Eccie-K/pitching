from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Pitch


@main.route('/')
def index():
    
   
    return render_template('index.html')
    
@main.route('/addpost', methods = ['GET' 'POST'])
def addpost():
    title = request.Form['title']
    content = request.Form['content']
    author = request.Form['author']
    
    return render_template('index.html',title = title,content = content,author = author)







  
