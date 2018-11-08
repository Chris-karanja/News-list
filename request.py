from app import app
import urllib.request,json
from app.models import source

Source = source.Source

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