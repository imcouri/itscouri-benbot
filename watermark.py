import os
from PIL import Image, ImageDraw, ImageFont
for filename in os.listdir('assets'):
    if filename == '.DS_Store':
        continue
    else:
        assetPath = "assets/" + filename
        print(assetPath)
        assetImage = Image.open(assetPath)
        watermark = Image.open('logo/logo.png')
        newsize = (150, 150)
        wt = watermark.resize(newsize)
        assetImage.paste(wt, (-10, 15),wt)
        assetImage.save("watermarked/" + filename)
        print("watermarked "+filename)







