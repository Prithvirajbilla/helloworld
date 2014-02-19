from __future__ import print_function
import BeautifulSoup

import re
def remove_html_tags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

thehtmlstring = ' '.join(open("as.html").readlines())
soup = BeautifulSoup.BeautifulSoup(thehtmlstring)

tags = []
for anchor in soup.findAll('h3'):
	name = remove_html_tags(str(anchor.contents[0]))
	if name=="Zimbu":
		tags+=["Zimbu"]
		break
	name = name.lower()
	name = name.replace(" ","_")
	name =name.replace("/","_")
	tags+=[name]
code = []
for anchor in soup.findAll('pre'):
        code = code+[ " ".join([remove_html_tags(str(i)) for i in  anchor.contents])]
print( len(tags),len(code))
from subprocess import call
for i in range(len(tags)):
	call(["touch",tags[i]])
	print(tags[i])
	f=open(tags[i],"w")
	f.write(code[i])
	f.close()
#	print(code[i], file=open(tags[i]))

