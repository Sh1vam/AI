from PIL import Image
def image():
    try:
        x=input("Enter png file name to convert to icon present in this folder : ")
        img = Image.open(x+'.png')
        img.save( x + ' .ico')
    except OSError:
        print("Image file extension is only valid")
        image()
    finally:
        print("done")
        image()
image()

