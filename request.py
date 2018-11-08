from app import app
import urllib.request,json
from app.models import source

Source = source.Source
Source_News = source.Source_News

#get api key
api_key = app.config['SOURCE_API_KEY']

#get base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(source):
    ''' json response to url request '''
    
    get_sources_url = base_url.format(source,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
       
        sources_results = None
       
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    
    
    return sources_results
    
def process_sources(source_list):
    ''' 
    processes result and transform them to a list of objects 
    
    Args:
    source_results: a list of source objects 
    
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        
        source_object = Source(id,name,description,url,category,language,country)
       
        source_results.append(source_object)
    
    
    return source_results

def get_source_news(news_source):
    ''' json to request to display news from a source id '''
    get_source_news_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_source_news_url) as url:
        source_news_data = url.read()
        source_news_response = json.loads(source_news_data)
         source_news_results = None
        if source_news_response['articles']:
            source_news_results = process_source_news(source_news_response['articles'])
    return source_news_results

# process results from get_source_news
def process_source_news(fetched_articles):
    ''' method to process json formatted article data '''

    source_news_list = []

    for article in fetched_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        if urlToImage:
            source_news_object = Source_News(author,title,description,url,urlToImage,publishedAt)
            source_news_list.append(source_news_object)
    return source_news_list 


    