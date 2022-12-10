
import atheris
import io

with atheris.instrument_imports():
    from PIL import Image

arg = ['/Users/mikashanela/Desktop/CS182/example2.py', '/Users/mikashanela/Desktop/CS182/cat.png', 
'/Users/mikashanela/Desktop/CS182/deer.png', '/Users/mikashanela/Desktop/CS182/fox.png', '/Users/mikashanela/Desktop/CS182/rabbit.jpg']

@atheris.instrument_func
def TestOneInput(data):
        
    dataBytesIO = io.BytesIO(data)
    im = Image.open(dataBytesIO)
    a = (im.format, im.size, im.mode)
    return a
  
atheris.Setup(arg, TestOneInput)
atheris.Fuzz()
