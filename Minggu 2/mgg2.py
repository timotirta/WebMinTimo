from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import re

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

Qku = []
Eku = []
webnya = "http://detik.com"
ambilCrawl(webnya,Qku,Eku)
print (Qku)
print (Eku)
