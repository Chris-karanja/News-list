from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_source_news
from ..models import Source,Source_News


 #views
@main.route('/')
def index():
    ''' returns index page and its data '''
    
    #getting movie sources
    news_sources = get_sources('sources')
    #print(news_sources)

    return render_template('index.html', sources = news_sources)

@main.route('/articles/<id>')
def source_news(id):
    ''' returns artices from a certain source '''
    news = get_source_news(id)
    title = f"{id} | All Articles"

    return render_template('source_news.html', title = title, news = news)
