import re
html_open = open('d:/python/sample.html','r')
file = html_open.read()

file1=re.sub('<.*?>','',file)
file_write=open('d:/python/sample.txt','x')
file_write.write(file1)

html_open.close()