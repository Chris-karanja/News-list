from flask import render_template
from app import app
from request import get_sources

 #views
@app.route('/')
def index():
    ''' returns index page and its data '''
    
    #getting movie sources
    news_sources = get_sources('sources')
    print(news_sources)

    return render_template('index.html', sources = news_sources)