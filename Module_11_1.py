import PIL
from PIL import Image, ImageDraw, ImageFilter
im = Image.open('rTt18IHcFS4.jpg')
print(im.format, im.size, im.mode)

cord = (10, 200, 640, 300) # лево, верх, право, низ
new_im = im.crop(cord)
print(new_im.size)

im_res = new_im.resize((500,200))
im_res.show()

im_gray = im.convert("L")
edges = im_gray.filter(ImageFilter.FIND_EDGES)
edges.show()





