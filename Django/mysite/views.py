#!/usr/bin/env python  
#-*-coding:utf-8-*-

from django.http import HttpResponse
from django.template import Context,Template
from django.shortcuts import render_to_response
import datetime

def hello1(request):
   now = datetime.datetime.now()
   html = "<html><body><h3>Hello World!</h3>It is now %s </body></html>" % now
   return HttpResponse(html)

# hello world using template
def hello2(request):
    now=datetime.datetime.now()
    html="<html><body><h3>Hello World!</h3>It is now {{current_time}}</body></html>"
    t=Template(html)  
    c=Context({'current_time':now})  
    ret=t.render(c)      
    return HttpResponse(ret)

# use render_to_response()
def hello(request):
    current_time=datetime.datetime.now()
    video = "http://www.youtube.com/embed/bqpPEbopBsQ"
    #locals() returns a dict with parameter name and values
    #in here is the same as {'current_time':current_time}
    return render_to_response('hello.html',locals())

# return string with fixed width, filled space with &nbsp;
def fixedwidth(value, arg):
    '''
    Truncates or pads a string to be a certain length
    
    Argument: Desired length of string
    '''

    try:
        length = int(arg)
    except ValueError: # invalid literal for int()
        return value # Fail silently
    if not isinstance(value, basestring):
        value = str(value)

    if len(value) > (length):
        value = value[:length - 3]
        value += '...'
    elif len(value) < length:
        for _ in range((length - len(value))/2):
            value = " " + value
            value = value + " "
        if ((length - len(value))%2):
            value = value + " "
    
    return value.replace(" ", "&nbsp;")
    #return value
    
def dbForm1(request):
    keyword=request.GET.get('keyword','')
    queryFlag = True if keyword !='' else False
    
    mid = fixedwidth('mid', 10)
    title = fixedwidth('title', 40)
    genre = fixedwidth('genre', 20)
    
    if queryFlag:
        queryStr = "SELECT mid, title, genre FROM movie " + \
                 "WHERE title LIKE \'%{0}%\' OR genre LIKE \'%{0}%\';".format(keyword)
        import psycopg2, psycopg2.extras
        
        con = None
        rows = {}
        try:
            con = psycopg2.connect(database='testdb', user='test', password='test')
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute(queryStr)
            rows = cur.fetchall()
            for row in rows:
                text = fixedwidth(row['mid'], 10)
                href = '<a href="http://localhost:8000/dbForm2/?mid={0}">'.format(row['mid']) \
                       + str(row['mid']) + '</a>'
                
                row['mid'] = text.replace(str(row['mid']), href)
                row['title'] = fixedwidth(row['title'], 40)
                row['genre'] = fixedwidth(row['genre'], 20)

        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            sys.exit(1)
            
        finally:
            if con:
                con.close()

    return render_to_response('dbForm1.html',locals())

def dbForm2(request):
    mid=request.GET.get('mid','')
    queryFlag = True if mid !='' else False
    
    bid = fixedwidth('bid', 10)
    bname = fixedwidth('bname', 40)
    baddress = fixedwidth('baddress', 40)
    num_copies = fixedwidth('num_copies', 10)
    
    if queryFlag:
        queryStr = "SELECT bid, bname, baddress, count(*) as num_copies \
          FROM copy JOIN branch USING (bid) WHERE mid = {0} AND copyid NOT IN \
          (SELECT DISTINCT copyid FROM rented WHERE returndate IS NULL) \
          GROUP BY bid, bname, baddress;".format(mid)
        import psycopg2, psycopg2.extras
        
        con = None
        rows = {}
        try:
            con = psycopg2.connect(database='testdb', user='test', password='test')
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute(queryStr)
            rows = cur.fetchall()
            for row in rows:
                text = fixedwidth(row['bid'], 10)
                href = '<a href="http://localhost:8000/dbForm3/?bid={0}&baddress={1}">'\
                       .format(row['bid'],(row['baddress']+", new york").replace(" ", "+")) \
                       + str(row['bid']) + '</a>'
                row['bid'] = text.replace(str(row['bid']), href)
                row['bname'] = fixedwidth(row['bname'], 40)
                
                text = fixedwidth(row['baddress'], 40)
                href = '<a href="https://maps.google.com/maps?q={0}">'.format(row['baddress']+", new york") \
                       + str(row['baddress']) + '</a>'
                row['baddress'] = text.replace(row['baddress'].replace(" ", "&nbsp;"), href)
                row['num_copies'] = fixedwidth(row['num_copies'], 10)

        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            sys.exit(1)
            
        finally:
            if con:
                con.close()
                
    return render_to_response('dbForm2.html',locals())

def dbForm3(request):
    bid=request.GET.get('bid','')
    baddress=request.GET.get('baddress','')
    queryFlag = True if bid !='' else False
    
    mid = fixedwidth('mid', 10)
    title = fixedwidth('title', 40)
    genre = fixedwidth('genre', 20)
    num_copies = fixedwidth('num_copies', 10)
    rows = {}
    if queryFlag:
        queryStr = "SELECT mid, title, genre, count(*) as num_copies \
          FROM movie JOIN copy USING (mid) WHERE bid = {0} AND copyid NOT IN \
		  (SELECT DISTINCT copyid FROM rented WHERE returndate IS NULL) \
          GROUP BY mid, title, genre;".format(bid)
        import psycopg2, psycopg2.extras
        
        con = None
        rows = {}
        try:
            con = psycopg2.connect(database='testdb', user='test', password='test')
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute(queryStr)
            rows = cur.fetchall()
            for row in rows:
                text = fixedwidth(row['mid'], 10)
                href = '<a href="http://localhost:8000/dbForm2/?mid={0}">'.format(row['mid']) \
                       + str(row['mid']) + '</a>'
                
                row['mid'] = text.replace(str(row['mid']), href)
                row['title'] = fixedwidth(row['title'], 40)
                row['genre'] = fixedwidth(row['genre'], 20)
                row['num_copies'] = fixedwidth(row['num_copies'], 10)

        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
            sys.exit(1)
            
        finally:
            if con:
                con.close()
                
    return render_to_response('dbForm3.html',locals())