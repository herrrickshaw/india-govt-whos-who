import sys,re
from bs4 import BeautifulSoup
s=BeautifulSoup(open(sys.argv[1],'rb').read(),'html.parser')
for sc in s(['script','style','header','nav','footer']): sc.decompose()
m=s.find('main') or s.find(id=re.compile('content|main',re.I)) or s.find(class_=re.compile('content|main',re.I)) or s.body
txt=m.get_text('\n',strip=True)
txt=re.sub(r'\n{2,}','\n',txt)
print(txt[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
