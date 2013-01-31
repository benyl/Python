#! /usr/bin/env python

import sys

print '#--------------------------------------'
print '# postgreSQL'
print '#--------------------------------------'

queryStr = 'at'
sqlStr = "SELECT mid, title, genre FROM movie WHERE title LIKE \'%{0}%\' OR genre LIKE \'%{0}%\'".format(queryStr)

print sqlStr

import psycopg2, sys
import psycopg2.extras

con = None

try:
    con = psycopg2.connect(database='testdb', user='test', password='test') 
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sqlStr)          
    rows = cur.fetchall()
    for row in rows:
        print row['mid'], row['title'], row['genre'] 

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    if con:
        con.close()
