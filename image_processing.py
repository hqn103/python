from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def test_image_manipulation():
    img = Image.open('2Gig490.JPG')
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 70)
    #draw.text((480, 180), 'Hello this is working', font=fnt, fill=(255, 255, 255, 255))
    draw.ellipse((100, 100, 80, 80), outline='yellow', width=3)
    del draw
    img.show()
    img.save('/tmp/lamanh01.jpg', 'jpeg')

if __name__ == '__main__':
    test_image_manipulation()
