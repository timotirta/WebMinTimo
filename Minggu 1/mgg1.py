from bs4 import BeautifulSoup
import urllib.request
webnya = input("Masukan Link : ")
conn = urllib.request.urlopen(webnya)
html = conn.read()
soup = BeautifulSoup(html, 'html.parser')
file = open("Tujuan.html","wb")
file.write(html)
file.close()
ctr=1
print("Hasil : ")
for link in soup.find_all('a'):
	if link.get('href')[:4] == "http":
		print(link.get('href'))
		conn = urllib.request.urlopen(link.get('href'))
		html = conn.read()
		file = open("Hasil"+str(ctr)+".html","wb")
		file.write(html)
		file.close()
		ctr+=1