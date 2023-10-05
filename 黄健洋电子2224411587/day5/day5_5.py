import random
import os
from PIL import Image
os.chdir('img')
for i in range(50):
    while True:
        nums=random.randint(0,99)
        try:
            path=str(nums)+'.png'
            pathnew=str(nums)+'.jpg'
            img=Image.open(path)
            img.convert('RGB')
            img.save(pathnew)
            os.remove(path)
            break
        except:
            pass