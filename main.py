from PIL import Image
from urllib.request import urlopen
import time
def type(str):
    x = len(str)
    for i in range(0, x):
        print((str)[i], end='')
        time.sleep(0.03)
    print('')





type("Welcome to Photo Editing!")
time.sleep(1)
type("To choose a photo to edit, please input the URL that leads to your picture! (Make sure it doesn't lead to a website with the picture!)")
print("★ Input 1 for help")
url = input()
if url == '1':
    print('L')
else:
    img = Image.open(urlopen(url))
    img.show()
