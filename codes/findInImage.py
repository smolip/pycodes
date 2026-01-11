from PIL import Image

imagePath = 'image.png'
newImagePath = 'image2.png'
im = Image.open(imagePath)

def whiteOrBlack (im):
    newimdata = []
    whitecolor = (255,255,255)
    blackcolor = (0,0,0)
    for color in im.getdata():
        if color == whitecolor:
            newimdata.append( whitecolor )
        else:
            newimdata.append( blackcolor )
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

whiteOrBlack(im).save(newImagePath)