import atheris
import io
import sys

with atheris.instrument_imports():
    from PIL import Image, ImageFile

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES=True

@atheris.instrument_func
def TestOneInput(data):
    dataBytesIO = io.BytesIO(data)
    try:
        im = Image.open(dataBytesIO)
        a = (im.format, im.size, im.mode)
        return a

    except Exception as e:
        return

atheris.Setup(sys.argv, TestOneInput)

atheris.Fuzz()




