import os
from PIL import Image
try:
    os.mkdir('img')
except:
    pass
os.chdir('img')
for i in range(100):
    path=str(i)+'.png'
    image = Image.new('RGB', (500, 500))
    image.save(path)
