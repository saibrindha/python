from pathlib import Path
from zipfile import ZipFile


zipper = ZipFile('assignment.zip','w')
path = Path()
for p in path.rglob("*.py"):
    zipper.write(p)
zipper.close()

with ZipFile('assignment.zip') as zp:
    print(zp.namelist())
    info = zp.getinfo('prime.py')
    print(f'{info.file_size}-->{info.compress_size}')
    
    zp.extract('prime.py')
   