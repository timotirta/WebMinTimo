from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import re
import whoosh.index as index
from whoosh.fields import Schema, TEXT, ID
import os, os.path
from whoosh.qparser import QueryParser

def ambilCrawl(S,D,E):
	Q = []
	Q.append(S)
	depth = 0
	while len(Q) != 0 and depth != 50:
		u = Q.pop()
		try:
			du = urllib.request.urlopen(u).read()
		except HTTPError:
			continue
			raise
		D.append(du)
		L = BeautifulSoup(du, 'html.parser',from_encoding="iso-8859-1")
		for link in L.find_all('a'):
			v = link.get('href')
			if v != None:
				if v[:4] == "http" and v != None:
					#print(v)
					E.append(v)
				if (not (v in D or v in Q) and v[:4] == "http"):
					Q.append(v)
		depth+=1


schemaku = Schema(title=ID(stored=True),content=TEXT(stored=True))

Dku = []
Eku = []
webnya = "http://detik.com"
ambilCrawl(webnya,Dku,Eku)

if not os.path.exists("tempatII"):
    os.mkdir("tempatII")

ix = index.create_in("tempatII", schemaku)
ix = index.open_dir("tempatII")

writer = ix.writer()

for i in range(len(Eku)):
	if i>50:
		break
	try:
		html = urllib.request.urlopen(Eku[i])
		soup = BeautifulSoup(html, 'html.parser')
		writer.add_document(title=Eku[i], content=soup.prettify())
		print("Document ditambahkan yaitu :  "+Eku[i])
	except HTTPError:
		continue
		raise

writer.commit()
ix = index.open_dir("tempatII")
katacari = input("Masukan Kata cari : ")

with ix.searcher() as searcher:
    qry = QueryParser("content", schema=ix.schema).parse(katacari)
    hasil = searcher.search(qry)
    for a in hasil:
        print(a["title"])