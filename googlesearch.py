#!/usr/bin/python
import urllib2, urllib, json

###############################################
# google search api that returns a list of urls
def googlesearch(query, size=8, start=0):
    MAX = 8
    
    if(size<1): return []
    if(size>MAX):
        return googlesearch(query, MAX, start) + \
                googlesearch(query, size-MAX, start+MAX)
    
    # urlencode the query
    queryStr = urllib.urlencode({'q': query})
    startStr = urllib.urlencode({'start': start}) # start from 0
    sizeStr = urllib.urlencode({'rsz': size}) # size bewteen 1 and 8
    
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&%s&%s' % \
                (queryStr, startStr, sizeStr)
    try:
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data_string = opener.open(req).read()
    except urllib2.URLError:
            print "------ Error opening " + url + "..... Timed out?"
            return None

    # use json to parse the results
    results = json.loads(data_string)
    
    if(results['responseData'] != None):
        return results['responseData']['results']
    else:
        return []

###############################################
# test googlesearch function
def googlesearch_test():
    query  = raw_input('please input query string: ')
    number = raw_input('how many result you want?  ')
    
    try:
        size = int(number)
    except ValueError: # invalid literal for int()
        print "ValueError: you must input a number."
        return None
        
    result = googlesearch(query, size)
    
    print 'Top %d results:' % len(result)
    for r in result: print ' ', r['url']
    
    
###############################################
# Default "main method" idiom.
if __name__ == "__main__":
    googlesearch_test()

    
###############################################
# google search function version 1
def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

  
###############################################
# google search function version 2
def query_google(query, start):

    import urllib2, urllib
    # http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=querystring&start=1

    # urlencode the query
    query = urllib.quote(query)

    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + query + '&start=' + str(start) + '&rsz=large'

    try:
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data_string = opener.open(req).read()

    except urllib2.URLError:
        print "------ Error opening " + url + "..... Timed out?"
        return None

    # Should use json to parse the results, but instead we're converting the string to dictionary. Duct tape.
    print data_string

    # replace the "null" with "None" for Python
    data_string = data_string.replace(": null,", ": None,")

    # convert the string to a dictionary
    exec("data = " + data_string)

    # simplify the results a bit
    results = data["responseData"]["results"]

    # build list of urls
    urls = []

    for i in results:
        url = i["url"]
        url = url.split("%")[0] # get rid of some garbage from the url. Probably avoidable by using Json.
        urls.append(url)

    return urls