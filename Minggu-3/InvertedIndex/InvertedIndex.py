
#untuk fetching
from bs4 import BeautifulSoup
import urllib.request
#untuk create schema
import os, os.path
import whoosh.index as index
from whoosh.fields import Schema, TEXT, ID
#untuk search
from whoosh.qparser import QueryParser

#creating schema and indexing
schema = Schema(title=ID(stored=True),content=TEXT(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")

ix = index.create_in("index", schema)
ix = index.open_dir("index")

writer = ix.writer()

lis_link=list()
lis_link.append("http://pythonforbeginners.com")
lis_link.append("http://www.python.org")
lis_link.append("https://docs.microsoft.com/en-us/dotnet/csharp/")
lis_link.append("https://www.tutorialspoint.com/cplusplus/index.htm")
for i in range(len(lis_link)):
    html_page = urllib.request.urlopen(lis_link[i])
    soup = BeautifulSoup(html_page, 'html.parser')
    writer.add_document(title=lis_link[i], content=soup.prettify())
    print("success add document "+str(i+1))


writer.commit()

#searching
ix = index.open_dir("index")

with ix.searcher() as searcher:
    q = QueryParser("content", schema=ix.schema).parse("beginners")
    results = searcher.search(q)
    for x in results:
        print(x["title"])